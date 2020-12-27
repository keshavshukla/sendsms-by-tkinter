import requests
from  tkinter import *
import json

from tkinter.messagebox import  showinfo, showerror

def send_sms(number, message, disc=None):
    url = ' https://www.fast2sms.com/dev/bulk'
    params ={
        'authorization':'NbnO7vR6HrZ5mIgF4c9h3KXCztyTlADidfjJpVB8Eo1qGWSPwYGovALbu1CI7UXQBiJtVc2PTDhWsKjH',
        'sender_id': 'FSTSMS',
        'message' : message,
        'language' : 'english',
        'route':'p',
        'numbers':number,

    }

    response=requests.get(url,params=params)
    response.json()
    print(disc)
    return dic.get('return')

def btn_click():
    num=textNumber.get()
    msg=textMsg.get("1.0", END)
    send_sms(num, msg)
    if r:
        showinfo("send success","successfully send")
    else:
        showerror("Error","something went wrong")


# creating GUI
root=Tk()
root.title("message Sender")
root.geometry("400x500")
font=("Helvetica", 22, "bold")

textNumber=Entry(root, font=font)
textNumber.pack(fill=X,pady=20)

textMsg = Text(root)
textMsg.pack(fill=X)

sendBtn = Button(root, text="SEND SMS",command=btn_click)
sendBtn.pack()

root.mainloop()

