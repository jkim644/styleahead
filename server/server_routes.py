from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from server_setup import User, Clothing, Base
import json


engine = create_engine("sqlite:///application_database.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

# @app.route("/")
# def default():
#     return redirect("/login/")

# @app.route("/login/", methods=["GET", "POST"])
# def login_controller():
#     if request.method == 'POST':
#         username = request.form['user_login']
#         password = request.form['user_pass']
#         find_user = session.query(User).get(username)
#         if(find_user != None):
#             if(find_user.password == password):
#                 return redirect(url_for('profile', username=username))
#             else: 
#                 return render_template("loginPage.html")
#         else: 
#             return render_template("loginPage.html")
#     else:
#         return render_template("loginPage.html")

# @app.route("/register/", methods=["GET", "POST"])
# def register_controller():
#     if request.method == 'POST':
#         pass1 = request.form['reg_pass1']
#         pass2 = request.form['reg_pass2']
#         if pass1 != pass2:
#             return redirect("/register/")
#         else: 
#             username = request.form['reg_user']
#             email = request.form['reg_email']
#             password = request.form['reg_pass1']
#             new_user = User(username =username, password = password, email = email)
#             try:
#                 session.add(new_user)
#                 session.commit()
#                 return redirect(url_for('profile', username=username))
#             except:
#                 return 'There was a problem accessing the database'
#     else:
#         return render_template("register.html")

# @app.route("/profile/<username>")
# def profile(username):
#     return render_template("chat_page.html", username=username)

# @app.route("/logout/")
# def unlogger():
#     return render_template("logoutPage.html")

# @app.route("/new-message/", methods=["POST"])
# def new_message():
#         message = request.form['message']
#         author = request.form['author']
#         new_message = Chat(message = message, author=author)
#         try:
#                 session.add(new_message)
#                 session.commit()
                
#                 message=[]
#                 request.form['author']
#                 request.form['message']

#                 message.append([request.form["author"], request.form["message"]])
#         except:
#                 return 'There was a problem accessing the database'
#         return redirect(url_for('profile', username=author))



# @app.route("/messages/")
# def messages():
#     # chats = session.query(Chat).all()
#     chats_as_json_objects = []
#     for chat in chats:
#         json_object = {}
#         json_object[chat.author] = chat.message
#         chats_as_json_objects.append(json_object)
#     return json.dumps(chats_as_json_objects)

if __name__ == "__main__":
    app.run()  

