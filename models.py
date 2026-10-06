import datetime
import os

from peewee import Model, SqliteDatabase, IntegerField, CharField, TextField, DateTimeField

# データベースへの接続設定(models.py と同じフォルダーの bbs.sqlite に保存する)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db = SqliteDatabase(os.path.join(BASE_DIR, "bbs.sqlite"))


# 投稿のモデル(postsテーブルと対応する)
class Post(Model):
    """Post Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    name = CharField()  # 投稿者の名前(短い文字列)
    body = TextField()  # 本文(長い文字列)
    created_at = DateTimeField(default=datetime.datetime.now)  # 何も指定しない場合は現在日時が入る

    class Meta:
        database = db
        table_name = "posts"


# テーブルがなければ作成する
db.create_tables([Post])
