from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship("Post", backref="user", passive_deletes=True)
    comments = db.relationship("Comment", backref="user", passive_deletes=True)
    likes = db.relationship("Like", backref="user", passive_deletes=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    """
    author 字段定义了一个整数类型的列，表示帖子的作者。
    它使用 db.ForeignKey 来创建一个外键关联到 user.id 字段，表示 Post 模型中的每个帖子都有一个对应的用户作为作者。
    
    ondelete="CASCADE" 参数表示当关联的用户被删除时，与之相关的帖子也会被级联删除。
    nullable=False 表示该字段不允许为空。
    """
    comments = db.relationship("Comment", backref="post", passive_deletes=True)
    """
    comments 字段使用 db.relationship 创建一个关系（relationship），表示一个帖子可以有多个评论。
    第一个参数 "Comment" 指定了关联模型的名称，即评论模型的名称。通过这个参数，Post 模型与 Comment 模型建立了一对多的关系。

    backref="post" 参数定义了一个反向引用（backref），它在评论模型中创建了一个名为 post 的属性，
    用于表示该评论所属的帖子。通过这个反向引用，可以方便地从评论模型访问到对应的帖子。

    passive_deletes=True 参数表示当与帖子关联的评论被删除时，数据库会自动进行级联删除。
    这意味着当删除一个帖子时，与之关联的所有评论也会被自动删除，避免了潜在的外键约束错误。
    """
    likes = db.relationship("Like", backref="post", passive_deletes=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    post_id = db.Column(
        db.Integer, db.ForeignKey("post.id", ondelete="CASCADE"), nullable=False
    )


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    post_id = db.Column(
        db.Integer, db.ForeignKey("post.id", ondelete="CASCADE"), nullable=False
    )
