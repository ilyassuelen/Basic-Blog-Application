from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

POSTS_FILE = "posts.json"


def load_posts():
    """Loads Blog posts from JSON-File."""
    if not os.path.exists(POSTS_FILE):
        return []
    with open(POSTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_posts(posts):
    """Saves Blog posts in the JSON-File."""
    with open(POSTS_FILE, "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)


@app.route('/')
def index():
    """Homepage - Shows all Blog posts."""
    posts = load_posts()
    return render_template("index.html", posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """Adds a new blog post."""
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        # Loading available Posts
        posts = load_posts()

        # Create ID for Post, adding and save posts in JSON-File
        if posts:
            new_id = max(post["id"] for post in posts) + 1
        else:
            new_id = 1

        new_post = {
            "id": new_id,
            "author": author,
            "title": title,
            "content": content
        }

        posts.append(new_post)
        save_posts(posts)

        return redirect(url_for('index'))

    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)