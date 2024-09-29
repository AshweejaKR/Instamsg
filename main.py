# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 22:38:07 2024

@author: ashwe
"""

import os
import json

from instagrapi import Client

global cl
global username
global password
global users_dict
users_dict = {}

# ********************* login using GUI *********************
# import tkinter as tk
# from tkinter import messagebox, ttk

# def login():
#     global username, password
#     username = uname_entry.get()
#     password = pwd_entry.get()
#     root.destroy()

# root = tk.Tk()
# root.title("Login Page")
# root.geometry("400x300")

# # Username and password labels and entry fields
# uname_label = tk.Label(root, text = "Username:")
# uname_label.pack(pady = 5)
# uname_entry = tk.Entry(root)
# uname_entry.pack(pady = 5)

# pwd_label = tk.Label(root, text = "Password:")
# pwd_label.pack(pady = 5)
# pwd_entry = tk.Entry(root, show = "*")
# pwd_entry.pack(pady = 5)

# # Login button
# login_button = tk.Button(root, text = "Login", command = login)
# login_button.pack(pady = 20)

# # Start the Tkinter event loop
# root.mainloop()
# ***********************************************************

# ********************* login using CMD *********************
def login():
    global username, password
    username = input("Enter username:\n")
    password = input("Enter password:\n")

login()
# ***********************************************************

def insta_login():
    global cl, username, password
    
    try:
        cl = Client()
        x = cl.login(username, password)
        
        if x:
            print("Login Successful")
        else:
            print("Login Failed")
    except Exception as err: print(err)


def get_follower_list():
    global cl, users_dict
    
    filename = str(cl.user_id) + "_follow_list.json"
    try:
        with open(filename, 'r') as file:
            users_dict = json.load(file)
    except FileNotFoundError:
        try:
            followers = cl.user_followers(cl.user_id)
            following = cl.user_following(cl.user_id)
            temp = {}
            temp.update(followers)
            temp.update(following)
        except Exception as err: print(err)

        for i in temp:
            users_dict[i] = temp[i].full_name

        with open(filename, 'w') as file:
            json.dump(users_dict, file)

def send_msg():
    global cl, users_dict
    msg = input("Enter msg to send\n")
    
    for user in users_dict.keys():
        try:
            print(f"sending {msg} to {users_dict[user]} ")
            cl.direct_send(msg, user_ids = [int(user)])
        except Exception as err: print(err)

# login to insta
insta_login()

# getting all followers/following list
get_follower_list()

# sending msg to all 
send_msg()

# logout to insta
cl.logout()
print("Logout done ...! ")











