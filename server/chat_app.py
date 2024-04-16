from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
import datetime as dt

Base = declarative_base()

class User(Base):

    __tablename__ = "User"

    username = Column("username", String, primary_key=True, nullable=False)
    password = Column("password", String, nullable=False)
    email = Column("email", String, nullable=False)

    def __int__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"({self.username} {self.password} {self.email})"
    

class Chat(Base):

    __tablename__ = "Chat"

    message = Column("message", String, primary_key=True, nullable=False)
    author = Column("author", String, nullable=False)

    def __int__(self, message, author):
        self.message = message
        self.author = author

    def __repr__(self):
        return f"({self.message} {self.author})"