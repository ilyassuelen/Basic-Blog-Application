from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)