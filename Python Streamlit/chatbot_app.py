#ChatBot Using Python Streamlit 

import streamlit as st
from datetime import datetime as dt
import random
import os , glob


greetIntent = ["hello" , "hi" , "hey" , "hello there" , "hi there"]
dateIntent = ["date" , "date please" , "tell me date" , "what's today's date"]
timeIntent = ["time" , "time please" , "tell me time" , "what's the time  "]
songIntent = ["play song" , "song please" , "music" ]



st.title("ChatBot WebApp..")
st.header("Python : Streamlit FrameWork ")
st.text(" Using simple conditional Statements : Python ")


form = st.form("chat_form")
msg = form.text_input("Enter Your message : ")
btn = form.form_submit_button("Submit")

msg = msg.lower()

if btn:

    if msg in greetIntent:
        st.write("Hello User ...")
    elif msg in dateIntent:
        date = dt.now().date()
        st.write("Date is : " , date.strftime("%d %b , %Y , %a"))
    elif msg in timeIntent:
        time = dt.now().time()
        st.write("Time is : " , time.strftime("%I :%M : %S , %Y , %p"))
    elif msg in songIntent:
        path = r"C:\Users\RAJNEESH SINGH\Music\MEmu Music"
        os.chdir(path)
        songs= glob.glob("*.mp3")
        os.startfile(random.choice(songs))
    elif msg == "bye" :
        st.write("Bye User")
    else :
        st.write("Invalid Message !! ")