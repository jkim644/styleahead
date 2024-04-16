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
    

class Clothing(Base):

    __tablename__ = "Clothing"

    type = Column("type", String, primary_key=True, nullable=False)
    color = Column("color", String, nullable=False)
    size = Column("size", String, nullable=False)
    tag = Column("size", String, nullable=False)

    def __int__(self, type, color, size, tag):
        self.type = type
        self.color = color
        self.size = size 
        self.tag = tag

    def __repr__(self):
        return f"({self.type} {self.color} {self.size} {self.tag})"