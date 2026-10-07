from flask import Flask, render_template, request, redirect, url_for
from models import Post

app = Flask(__name__)


# 一覧表示(GET)
@app.route("/")
def index():
    q = request.args.get("q", "")  # URL の ?q=○○ の値（なければ空文字）
    posts = Post.select().order_by(Post.created_at.desc())
    if q:  # キーワードがあるときだけ絞り込む
        posts = posts.where((Post.name.contains(q)) | (Post.body.contains(q)))
    return render_template("index.html", posts=posts, q=q)
    # return render_template("index.html", posts=posts)


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


@app.route("/posts/<int:post_id>/edit", methods=["GET", "POST"])
def edit(post_id):
    post = Post.get_by_id(post_id)  # 編集する投稿を取り出す
    if request.method == "GET":  # ページを開いたとき
        return render_template("edit.html", post=post)
    post.name = request.form["name"]  # フォームの値で上書き
    post.body = request.form["body"]
    post.save()  # データベースに保存
    return redirect(url_for("index"))  # 更新したら一覧に戻る


if __name__ == "__main__":
    app.run(port=8000)
