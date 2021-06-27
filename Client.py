from tkinter import ttk
from tkinter import *
import socket
import json
dictionary={}
dictionary2={}
cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cs.settimeout(50)

def main():
    try:
        cs.connect(('127.0.0.1', 4444))
        while True:

            send(cs)
            data = cs.recv(1024).decode()
            see(data)



    except socket.error as e:
        print('exp', e)




def send(cs):

        while True:
            window = Tk()
            window.title("clint1")
            window.geometry("400x300")

            en1 = ttk.Entry(window, width=65)
            en1.grid(row=0)
            en1.focus()

            with open("s.json", "w") as f:
                dictionary["client1"] =en1.get()
                s = json.dumps(dictionary)
                f.write(s)
            b1 = ttk.Button(window, text="go", width=65)
            b1.grid(row=1)
            b1.config(command=lambda: cs.sendall(en1.get().encode()))
            b2 = ttk.Button(window, text="waiting server response", width=65)
            b2.grid(row=2)
            b2.config(command=window.destroy)

            window.mainloop()
            break


def see(data):
    while True:
        with open("s2.json", "w") as f:
            dictionary2["client1"] = data
            s = json.dumps(dictionary2)
            f.write(s)


        with open("s2.json", "r"):
            conten = dictionary2["client1"]

        wind= Tk()
        wind.title("server response 1")
        wind.geometry("400x300")
        b2 = ttk.Button(wind, text="watch server response", width=65)
        l1 = ttk.Label(wind, text="receive message", foreground="black", background="silver", width=65)
        l1.grid(row=3)
        b2.grid(row=2)
        b2.config(command=lambda: l1.configure(font=("none", 8, "bold"), text=conten))
        b3 = ttk.Button(wind, text="I want to send", width=65)
        b3.grid(row=4)
        b3.config(command=wind.destroy)
        print("msg from multithread server-->", conten)


        wind.mainloop()
        break






if __name__=='__main__':
    main()





