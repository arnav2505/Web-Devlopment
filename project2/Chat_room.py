import os
import requests
from flask import Flask, session, redirect, url_for
from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit
from flask_socketio import join_room, leave_room
from flask_socketio import send, emit

app = Flask(__name__) 
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

rooms = {"Crescent":[] , "Crescent friends":[] , "School friends":[] , "Espice Bros":[]}
activity = {'message_text':[] , 'message_counter':0}
usernames =[];
username=""

@app.route("/", methods = ['GET', 'POST'])
def Intro():
    if request.method == 'POST':
        print("hi")
        conf_username = request.form.get('harry')
        print(conf_username)
        if conf_username == "nope1":          
            return redirect("Display_name")
        else :
            username=conf_username;
            return render_template("Intro.html")

    return render_template("Intro.html")

@app.route("/Display_name", methods = ['GET', 'POST'])
def Display_name():
    if request.method == 'POST':
        print("g18")
        username = request.form.get('username1')
        print(request.form)
        return redirect("/Chat_room" , username)
    return render_template("Display_name.html")            

@app.route("/Chat_room", methods = ['GET', 'POST'])
def Chat_room(username):
    return render_template("Chat_room.html" , rooms=rooms , username=username)

@app.route("/New_room", methods = ['GET', 'POST'])
def New_room():
    if request.method == 'POST':
        room2 = request.form.get("room2")
        rooms[room2]=[]
        return redirect("/Chat_room" , username)            
    return render_template("New_room.html" , rooms=rooms)

@socketio.on("join", namespace='/Chat_room')
def on_join(data_room):
    join_room(data_room['selection'])
    activity['message_text'].append(username + ' has entered the room.')
    print(activity['message_text'])
    activity['message_counter'] += 1
    emit("broadcast message", activity, broadcast=True)

    
@socketio.on('leave', namespace='/Chat_room')
def on_leave(data_room):
    leave_room(data_room['selection'])
    activity['message_text'].append(username + ' has left the room.')
    activity['message_counter'] += 1;
    emit("broadcast message", activity, broadcast=True)
    
@socketio.on("submit message", namespace='/Chat_room')
def vote(data):
    message_text = data['message_text']
    activity['message_text'].append(message_text)
    activity['message_counter'] += 1;
    emit("broadcast message", activity, broadcast=True)