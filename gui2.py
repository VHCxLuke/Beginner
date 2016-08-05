# Copyright (C) Values Holding Company, Inc. - All Rights Reserved
# This file contains the graphical configuration of Blue Bird Avionics
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and Confidential
# Written by Luke Redwine <Luke@valuesholding.com>, July 2016
#still worked
#!/usr/bin/env python
from Tkinter import *
from serial import *
import os, sys
import time

LorC = True
a = None
t = None
p = None
f = None
root = Tk()
root.attributes('-zoomed',True)
root.attributes('-fullscreen', True)
w,h = root.winfo_screenwidth(), root.winfo_screenheight()
root.configure(background = 'black')
root.geometry("%dx%d+0+0" % (w,h))
root.focus_set()
root.bind("<q>", lambda e: e.widget.quit())
B = Label(root)
T1 = Label(root)
T2 = Label(root)
def Landing_Mode():
        global LorC
        LorC = False

def Cruise_Mode():
	global LorC
	LorC = True

canvas = Canvas(root, width = 250, bg = 'black', highlightthickness = 0)
canvas.pack(expand = 1, fill = Y, side = TOP, anchor = CENTER)

det = None

var = StringVar()
var.set('Altitude:')
L = Label(root, textvariable = var, font = ("Terminal", 10), bg = 'black', fg = 'white')
L.place(x = 5, y = 5)
A = Label(root)


def Altitude():
	global a
	global A
	global B
	var1 = StringVar()
	var1.set(a)
	A = Label(root, textvariable = var1,text = "   ", font = ("Terminal", 10), bg = 'black', fg = 'white')
	A.place(x = 80, y = 5)
	B = Label(root, text = ' m', font = ("Terminal", 10), bg = 'black', fg = 'white')
	B.place(x = 110, y = 5)

Tvar = StringVar()
Tvar.set('Temp:')
T = Label(root, textvariable = Tvar, font = ("Terminal", 10), bg = 'black', fg = 'white')
T.place(x = 225, y = 5)

def Temperature():
	global t
	global T2
	global T1
	v = 1.8
	t = float(t)
	t  = t * v + 32.00
	t = int(t)
	Tvar1 = StringVar()
	Tvar1.set(t)
	T1 = Label(root, textvariable = Tvar1, font = ("Terminal", 10), bg = 'black', fg = 'white')
	T1.place(x = 270, y = 5)
	Tvar2 = StringVar()
	Tvar2.set('F     ')
	T2 = Label(root, textvariable = Tvar2, font = ("Terminal", 10), bg = 'black', fg = 'white')	
	T2.place(x = 290, y = 5)

def AoA():
	global det
	global canvas
	global f 
	det = canvas.create_rectangle(0,f-7.5,250,f+7.5,fill = 'white')

def yellow2():
	canvas.create_rectangle(12.5,176.5,237.5,226.5, fill = 'yellow1', tags = 'allt')	

def yellow1():
        canvas.create_rectangle(12.5,126.5,237.5,176.5, fill = 'yellow1', tags = 'allt')
	canvas.create_rectangle(0,124,250,129, fill = 'grey', tags = 'allt')

def green():
        global canvas
	canvas.create_rectangle(12.5,226.5,237.5,276.5, fill = 'chartreuse2', tags = 'allt')
        canvas.create_rectangle(0,246.5,250,251.5, fill = 'grey', tags = 'allt')

def red0():
	global canvas
	canvas.create_rectangle(12.5,76.5,237.5,126.5, fill = 'red4')
	canvas.create_polygon(12.5,77,12.5,14,87.5,77, fill = 'red4')
        canvas.create_polygon(237.5,77,237.5,14,162.5,77, fill = 'red4')
	canvas.create_rectangle(0,124,250,129, fill = 'grey')
	canvas.create_polygon(87.5,77,162.5,77,125,104,fill = 'black')
	
def red1():
	global canvas
	canvas.create_rectangle(12.5,76.5,237.5,126.5, fill = 'red', tags = 'allt')
	canvas.create_polygon(87.5,77,162.5,77,125,104,fill = 'black', tags = 'allt')
	canvas.create_rectangle(0,124,250,129, fill = 'grey', tags = 'allt')
	canvas.create_polygon(12.5,77,12.5,14,87.5,77, fill = 'red',tags = 'allt')
	canvas.create_polygon(237.5,77,237.5,14,162.5,77, fill = 'red',tags = 'allt')

def redx():
	canvas.create_rectangle(12.5,376.5,237.5,426.5, fill = 'red4')
        canvas.create_polygon(12.5,426.5,12.5,476.5,87.5,426.5, fill = 'red4')
        canvas.create_polygon(237.5,426.5,237.5,476.5,162.5,426.5, fill = 'red4')
        canvas.create_polygon(162.5,426.5,87.5,426.5,125,400, fill = 'black')
	canvas.create_rectangle(0,374,250,379, fill = 'grey')

def redy():
	canvas.create_rectangle(12.5,376.5,237.5,426.5, fill = 'red',tags = 'allt')
        canvas.create_polygon(12.5,426.5,12.5,476.5,87.5,426.5, fill = 'red',tags = 'allt')
        canvas.create_polygon(237.5,426.5,237.5,476.5,162.5,426.5, fill = 'red',tags = 'allt')
        canvas.create_polygon(162.5,426.5,87.5,426.5,125,400, fill = 'black',tags = 'allt')
        canvas.create_rectangle(0,374,250,379, fill = 'grey',tags = 'allt')


Landing = Button(root, text = "Landing Mode", command = Landing_Mode, bg = 'black', fg = 'white', font = ('Terminal',10))
Landing.place(x = 1, y = 450)
Cruise = Button(root, text = "Cruise Mode", command = Cruise_Mode, bg = 'black', fg = 'white', font = ('Terminal',10))
Cruise.place(x = 210, y = 450)

def grn1():
	canvas.create_rectangle(12.5,226.5,237.5,276.5, fill = 'dark green')
        canvas.create_rectangle(0,246.5,250,251.5, fill = 'grey')

def yel1():
	canvas.create_rectangle(12.5,126.5,237.5,176.5, fill = 'gold4')
	canvas.create_rectangle(0,124,250,129, fill = 'grey')

def yel2():
	canvas.create_rectangle(12.5,176.5,237.5,226.5, fill = 'gold4')

def yel3():
	canvas.create_rectangle(12.5,276.5,237.5,326.5, fill = 'gold4')

def yel4():
	canvas.create_rectangle(12.5,326.5,237.5,376.5, fill = 'gold4')
	canvas.create_rectangle(0,374,250,379, fill = 'grey')

def yellow4():
	canvas.create_rectangle(12.5,326.5,237.5,376.5, fill = 'yellow1', tags = 'allt')
	canvas.create_rectangle(0,374,250,379, fill = 'grey', tags = 'allt')
	
def yellow3():
	canvas.create_rectangle(12.5,276.5,237.5,326.5, fill = 'yellow1',tags = 'allt')

def restart_p():
	python = sys.executable
	os.execl(python, python, * sys.argv)

count = 0
	
def readSerial():
		arduino = Serial("/dev/ttyACM0", 9600)
		global p
		global a
		global t
		global f
		global A
		global B
		global T1
		global T2
		global canvas	
    		p = arduino.readline()
		t = arduino.readline()
		a = arduino.readline()
		f = arduino.readline()
		if f > 0.0:
			f = float(f)
			f = int(f)

		A.destroy()
		B.destroy()
		Altitude()
		T1.destroy()
		T2.destroy()
		Temperature()
		canvas.delete(det)
		global LorC
		if LorC == False:
			f = f - 62.5
		canvas.delete('allt')
		if f < 126.5:
			red1()
		elif f > 376.5:
			redy()
		elif f > 126.5 and f < 176.5:
			yellow1()
		elif f > 176.5 and f < 226.5:
			yellow2()
		elif f > 226.5 and f < 276.5:
			green()
		elif f > 276.5 and f < 326.5:
			yellow3()
		elif f > 326.5 and f < 376.5:
			yellow4()
		AoA()
		root.after(10, readSerial)

root.after(10,readSerial)
red0()
redx()
yel1()
yel2()
yel3()
yel4()
grn1()
root.mainloop()
