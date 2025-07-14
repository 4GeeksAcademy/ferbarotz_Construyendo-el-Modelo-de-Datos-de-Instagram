from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
# CODIGO USUARIO

class Usuario (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    post = relationship("Post", back_populates="usuario")
    followers = relationship("Followers", back_populates="usuario")
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            # do not serialize the password, its a security breach
        }

# CODIGO POST

class Post (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    url_imagen: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    texto: Mapped[str] = mapped_column(nullable=False)
    n_likes: Mapped[int] = mapped_column(nullable=False)
    id_usuario: Mapped[int] = mapped_column(nullable=False)

    usuario_id = mapped_column(ForeignKey("usuario.id"))
    usuario = relationship("Usuario", back_populates="post")

    comentario = relationship("Comentario", back_populates="post")


    def serialize(self):
        return {
            "id": self.id,
            "url_imagen": self.url_imagen,
            "texto": self.texto,
            "n_likes": self.n_likes,
            "id_usuario": self.id_usuario,
            # do not serialize the password, its a security breach
        }
    
# CODIGO COMENTARIOS

class Comentario (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_post: Mapped[int] = mapped_column(nullable=False)
    texto: Mapped[str] = mapped_column(nullable=False)

    post_id = mapped_column(ForeignKey("post.id"))
    post = relationship("Post", back_populates="comentario")
   
    def serialize(self):
        return {
            "id": self.id,
            "id_post": self.post_id,
            "texto": self.texto,
            # do not serialize the password, its a security breach
        }
    
# CODIGO FOLLOWERS

class Followers (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[int] = mapped_column(primary_key=True)
    id_followers: Mapped[int] = mapped_column(primary_key=True)

    usuario_id = mapped_column(ForeignKey("usuario.id"))
    usuario = relationship("Usuario", back_populates="followers")

    def serialize(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_followers": self.id_followers,
            # do not serialize the password, its a security breach
        }

