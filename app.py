import re
from flask import Flask, render_template, request, redirect, url_for
from models import Post

app = Flask(__name__)


# 一覧表示(GET)
@app.route("/")
def index():
    posts = Post.select().order_by(Post.created_at.desc())
    return render_template("index.html", posts=posts)


@app.route("/posts", methods=["POST"])
def create():
    name = request.form["name"]
    body = request.form["body"]
    Post.create(name=name, body=body)

    return redirect(url_for("index"))


# /posts/1/delete
@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete(post_id):
    post = Post.get_by_id(post_id)
    post.delete_instance()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=8000)
