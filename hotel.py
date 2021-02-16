# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 02:10:37 2021

@author: vaibhav
"""

from tkinter import*
from PIL import Image,ImageTk 
from customer import Customer_win



class hotelmanagementsystem:
    def __init__(self, root): #constructor
        self.root=root #initialise
        self.root.title("Hotel Management System")
        self.root.geometry("1280x720+0+0")
        
        
   #-------------Title-----------------
   
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",42,"bold"),bg="black",fg ="cyan",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1280,height=100)
        
        
   #-------------Main-Frame-----------
       
        mainframe=Frame(self.root,bd=4,relief=RIDGE)
        mainframe.place(x=0,y=100,width=1280,height=620)
        
        
   #------------MENU------------
   
   
        lbl_menu=Label(mainframe,text="MENU",font=("times new roman",26,"bold"),bg="black",fg ="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=280)
        
        
        
   #----------Button-Frame--------
        
        
        btnframe=Frame(self.root,bd=4,relief=RIDGE)
        btnframe.place(x=0,y=145,width=281,height=193)
        
        
        cust_btn=Button(btnframe,text="CUSTOMER",command=self.cust_details,width=24,font=("times new roman",16,"bold"),bg="black",fg ="white",bd=4,relief=RIDGE,cursor="hand1")
        cust_btn.grid(row=0,column=0)
        
        room_btn=Button(btnframe,text="ROOMS",width=24,font=("times new roman",16,"bold"),bg="black",fg ="white",bd=4,relief=RIDGE,cursor="hand1")
        room_btn.grid(row=1,column=0,)
        
        details_btn=Button(btnframe,text="DETAILS",width=24,font=("times new roman",16,"bold"),bg="black",fg ="white",bd=4,relief=RIDGE,cursor="hand1")
        details_btn.grid(row=2,column=0)
        
        logout_btn=Button(btnframe,text="LOGOUT",width=24,font=("times new roman",16,"bold"),bg="black",fg ="white",bd=4,relief=RIDGE,cursor="hand1")
        logout_btn.grid(row=3,column=0)
        

def cust_details(self):
    self.new_window=Toplevel(self.root)
    self.app=Customer_win(self.new_window)
        
        
        
        
        


if __name__== "__main__": #calling object in main fn
    root=Tk()
    obj=hotelmanagementsystem(root)
    root.mainloop() #closing mainloop
        