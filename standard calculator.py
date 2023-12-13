"""
       Thankyou for using this calculator
       It was created by MARDORANGE  \  https://github.com/MardOrange
       Have a good day...
"""

from tkinter import *

# Creating window
window = Tk()
window.configure(bg="Black")

# Creating input bar
entry = Entry(width=15, font=('Arial', 40), borderwidth=15, bg="Black", fg="White")
entry.grid(row=0, column=0, columnspan=100)


# Function to insert a number into the entry field
def insert(num):
	first = entry.get()
	entry.delete(0, END)
	entry.insert(0, str(first) + str(num))


# Function to set the operator to addition
def add():
	global oper
	oper = "add"
	global sn
	sn = entry.get()
	entry.delete(0, END)


# Function to set the operator to subtraction
def sub():
	global oper
	oper = "sub"
	global sn
	sn = entry.get()
	entry.delete(0, END)


# Function to set the operator to multiplication
def mul():
	global oper
	oper = "mul"
	global sn
	sn = entry.get()
	entry.delete(0, END)


# Function to set the operator to division
def div():
	global oper
	oper = "div"
	global sn
	sn = entry.get()
	entry.delete(0, END)


# Function to perform the calculation based on the selected operator
def equals():
	d = entry.get()
	k = entry.delete(0, END)
	if oper == "add":
		entry.insert(0, float(sn) + float(d))
	elif oper == "sub":
		entry.insert(0, float(sn) - float(d))
	elif oper == "mul":
		entry.insert(0, float(sn) * float(d))
	elif oper == "div":
		# Check for division by zero
		if float(d) != 0:
			entry.insert(0, float(sn) / float(d))
		else:
			entry.insert(0, "Error")


# Function to clear the entry field
def clear():
	entry.delete(0, END)


# Function to delete the last character in the entry field (backspace)
def back():
	current_text = entry.get()
	entry.delete(len(current_text) - 1)


# Creating buttons
button_1 = Button(text="1", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=lambda: insert(1))
button_2 = Button(text="2", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=lambda: insert(2))
button_3 = Button(text="3", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=lambda: insert(3))
button_4 = Button(text="4", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=lambda: insert(4))
button_5 = Button(text="5", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=lambda: insert(5))
button_6 = Button(text="6", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=lambda: insert(6))

button_7 = Button(text="7", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=lambda: insert(7))
button_8 = Button(text="8", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=lambda: insert(8))
button_9 = Button(text="9", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=lambda: insert(9))

button_0 = Button(text="0", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=lambda: insert(0))
button_00 = Button(text="00", padx=24, pady=15, font=("Arial", 18), fg='White', bg='Black',command=lambda: insert("00"))
button_po = Button(text=".", padx=34, pady=15, font=("Arial", 18), fg='White', bg='Black', command=lambda: insert("."))

button_p = Button(text="+", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=add)
button_s = Button(text="-", padx=33, pady=15, font=("Arial", 18), fg='White', bg='Black', command=sub)
button_m = Button(text="x", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=mul)
button_d = Button(text="/", padx=33, pady=15, font=("Arial", 18), fg='White', bg='Black', command=div)
button_e = Button(text="=", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=equals)
button_c = Button(text="C", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=clear)
button_back = Button(text="<x", padx=30, pady=15, font=("Arial", 18), fg='White', bg='Black', command=back)

# Putting buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_00.grid(row=4, column=0)
button_po.grid(row=4, column=2)

button_p.grid(row=1, column=3)
button_s.grid(row=2, column=3)
button_m.grid(row=1, column=4)
button_d.grid(row=2, column=4)

button_e.grid(row=3, column=3)
button_c.grid(row=3, column=4)
button_back.grid(row=4, column=3)

# Show the GUI
window.mainloop()

'''

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+=--::::--=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-:::::::::::::-=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:::::.-:::::::::::+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:-:-.:..::::::::::::*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*=-:.:::::::::::::::#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+*=-..:-::::::::::::=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-.::.....-:---:::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.........-:=:-::::::::-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%........:--=-:::-:-::+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:..::---=-=+=::---#*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%##+===-+#*:=%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**=*+@%*##%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+##%%####*:.:-=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*+##*#%#%+:.....-*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@+++%%#*%#%:........-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+===+++=%%%##%%..........-%@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+========+=%%###%#=.......::.##%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+=========++*%####%#-......-..###%@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*=====+=====+###%####.......--####%@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#--====+====*########=......-#%####%@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:...:-=+===####%#####:......#%#####@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-......:==+####%#####*......-######%@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+........=+####%######+......#######%@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%........-=*###%%######-.....=#######@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-.......:==+***##%%%%%#.....:###%%%#%@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*:......:========+%%@%@-.....##%#=-=#%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=....:::::::-===+=====*%%@%.....+%+:...:#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:.................::--==#@%*-....:+......=@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=...:::...................:--=-::-=---:....%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=...:..........................:-+*+++##*=:#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.................................--.:-:-+#%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:........-:........................:.::..:%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:.......:+-.......................:...:.-@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:........-@#=......................:...:*@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:.........#@%*-:...................-...:%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*-.........=#++*%%+-...............:=...+@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@%#*=+=.........-++*@@@@@%+-:...........-=..+@@@@@@@@@@@@@@@@@@@@
-------------------------=*++===.........--------------::::::::::--:----------------------


'''
