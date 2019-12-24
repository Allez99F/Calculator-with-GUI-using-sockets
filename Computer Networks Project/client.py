# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:14:23 2019

@author: Shashidhar
"""
from tkinter import *
import socket
import sys
expression=""

def press(num):
    global expression
    expression = expression+str(num)
    equation.set(expression)

    
def equalpress():
    global expression
    print(expression)
    check = str(expression)	
    s.send(check.encode())
    expression=""
    result = s.recv(1024).decode()
    if result == "ZeroDiv":
        equation.set("You can't divide by 0, try again")
    elif result == "MathError":
        equation.set("There is an error with your math, try again")
    elif result == "SyntaxError":
        equation.set("There is an invalid syntax , please try again")
    elif result == "NameError":
        equation.set("You did not enter an equation, try again")
    else:
        equation.set(result)
    
    
        
def clear1():
    global expression
    expression=""
    equation.set("")


def create_calci():

    gui = Tk()
    
    gui.configure(background = "white")
    
    gui.title("Calculator")
    
    gui.geometry("310x270")
    

    global equation
    equation = StringVar()
    
    expression_field = Entry(gui,textvariable=equation,bg='grey81')
    
    expression_field.grid(columnspan=4, ipadx=70) 
      
    equation.set('') 
      
    button1 = Button(gui,text='1',fg='grey25',bg='burlywood1',command=lambda:press(1),height=1,width=7,pady = 10)
    button1.grid(row=2,column=0)
    
    
    button2 = Button(gui, text=' 2 ', fg='grey25', bg='burlywood1', 
                         command=lambda: press(2), height=1, width=7,pady = 10) 
    button2.grid(row=2, column=1) 
      
    button3 = Button(gui, text=' 3 ', fg='grey25', bg='burlywood1', 
                     command=lambda: press(3), height=1, width=7,pady = 10) 
    button3.grid(row=2, column=2) 
      
    button4 = Button(gui, text=' 4 ', fg='grey25', bg='burlywood1', 
                     command=lambda: press(4), height=1, width=7,pady = 10) 
    button4.grid(row=3, column=0) 
      
    button5 = Button(gui, text=' 5 ', fg='grey25', bg='burlywood1', 
                     command=lambda: press(5), height=1, width=7,pady = 10) 
    button5.grid(row=3, column=1) 
      
    button6 = Button(gui, text=' 6 ', fg='grey25', bg='burlywood1', 
                     command=lambda: press(6), height=1, width=7,pady = 10) 
    button6.grid(row=3, column=2) 
      
    button7 = Button(gui, text=' 7 ', fg='grey25', bg='burlywood1', 
                     command=lambda: press(7), height=1, width=7,pady = 10) 
    button7.grid(row=4, column=0) 
      
    button8 = Button(gui, text=' 8 ', fg='grey25', bg='burlywood1', 
                     command=lambda: press(8), height=1, width=7,pady = 10) 
    button8.grid(row=4, column=1) 

      
    button9 = Button(gui, text=' 9 ', fg='grey25', bg='burlywood1', 
                     command=lambda: press(9), height=1, width=7,pady = 10) 
    button9.grid(row=4, column=2) 
      
    button0 = Button(gui, text=' 0 ', fg='grey25', bg='burlywood1', 
                     command=lambda: press(0), height=1, width=7,pady = 10) 
    button0.grid(row=5, column=0) 
      
    plus = Button(gui, text=' + ', fg='grey25', bg='burlywood1', 
                  command=lambda: press("+"), height=1, width=7,pady = 10) 
    plus.grid(row=2, column=3) 
      
    minus = Button(gui, text=' - ', fg='grey25', bg='burlywood1', 
                   command=lambda: press("-"), height=1, width=7,pady = 10) 
    minus.grid(row=3, column=3) 
      
    multiply = Button(gui, text=' * ', fg='grey25', bg='burlywood1', 
                      command=lambda: press("*"), height=1, width=7,pady = 10) 
    multiply.grid(row=4, column=3) 
      
    divide = Button(gui, text=' / ', fg='grey25', bg='burlywood1', 
                    command=lambda: press("/"), height=1, width=7,pady = 10) 
    divide.grid(row=5, column=3) 
      
    equal = Button(gui, text=' = ', fg='grey25', bg='burlywood1', 
                   command=equalpress, height=1, width=7,pady = 10) 
    equal.grid(row=5, column=2) 
      
    clear = Button(gui, text='Clear', fg='grey25', bg='burlywood1', 
                   command=clear1, height=1, width=7,pady = 10) 
    clear.grid(row=5, column='1') 
    
    sin = Button(gui, text=' sin ', fg='grey25', bg='burlywood1', 
                      command=lambda: press("sin"), height=1, width=7,pady = 10) 
    sin.grid(row=6, column=0)

    cos = Button(gui, text=' cos ', fg='grey25', bg='burlywood1', 
                      command=lambda: press("cos"), height=1, width=7,pady = 10) 
    cos.grid(row=6, column=1)

    tan = Button(gui, text=' tan ', fg='grey25', bg='burlywood1', 
                      command=lambda: press("tan"), height=1, width=7,pady = 10) 
    tan.grid(row=6, column=2)

    log = Button(gui, text=' log ', fg='grey25', bg='burlywood1', 
                      command=lambda: press("log"), height=1, width=7,pady = 10) 
    log.grid(row=6, column=3) 

    dot = Button(gui, text='   .   ', fg='grey25', bg='burlywood1', 
                      command=lambda: press("."), height=1, width=7,pady = 10)
    dot.grid(row = 7 , column = 3)
    sqrt = Button(gui , text ='sqrt' ,fg='grey25', bg = 'burlywood1',
			comman = lambda: press('sqrt'),height=1,width = 7 , pady =10)

    sqrt.grid(row = 7 , column = 0)

    e = Button(gui , text ='e^x' ,fg='grey25', bg = 'burlywood1',
			comman = lambda: press('e'),height=1,width = 7 , pady =10)

    e.grid(row = 7 , column = 1)
 
    x = Button(gui , text ='x^2' ,fg='grey25', bg = 'burlywood1',
			comman = lambda: press('x'),height=1,width = 7 , pady =10)

    x.grid(row = 7 , column = 2)
    
    gui.mainloop()
    
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = (sys.argv[1])
port = int(sys.argv[2])
s.connect((host,port))
create_calci()

    

