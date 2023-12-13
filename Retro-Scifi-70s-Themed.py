"""
       Thankyou for using this calculator
       It was created by MARDORANGE  \  https://github.com/MardOrange
       Have a good day...
"""

print("History")

from tkinter import *

# Set color constants
background = '#252522'
buttonbg = '#081B0B'
entrybg = '#143F1A'
entryfg = '#60FF6E'

# Set button sizes
x = 35
y = 20
x1 = 40
y1 = 20

# Window creation
window = Tk()
window.configure(bg=background, )
window.title("Maddorange")
window.iconbitmap('Icon.ico')

# Label at the bottom of the window
lab = Label(text="A QUALITY PRODUCT FROM MARDORANGE")
lab.grid(row=5, column=0, columnspan=30)
lab.configure(font=('Arial', 10), bg=background, fg=entryfg)


# Functions

# Function to insert a number into the entry widget
def insert(num):
	cur = entry.get()
	entry.delete(0, END)
	entry.insert(0, str(cur) + str(num))


# Function to switch to light mode
def light():
	# Change window and button colors
	window.configure(background="White")
	buttonbg = "White"
	entrybg = "White"
	entryfg = "Black"
	button_1.configure(bg='White', fg='Black')
	button_2.configure(bg='White', fg='Black')
	button_3.configure(bg='White', fg='Black')
	button_4.configure(bg='White', fg='Black')
	button_5.configure(bg='White', fg='Black')
	button_6.configure(bg='White', fg='Black')
	button_7.configure(bg='White', fg='Black')
	button_8.configure(bg='White', fg='Black')
	button_9.configure(bg='White', fg='Black')
	button_0.configure(bg='White', fg='Black')
	button_00.configure(bg='White', fg='Black')
	button_p.configure(bg='White', fg='Black')
	button_po.configure(bg='White', fg='Black')
	button_d.configure(bg='White', fg='Black')
	button_m.configure(bg='White', fg='Black')
	button_s.configure(bg='White', fg='Black')
	button_C.configure(bg='White', fg='Black')
	button_e.configure(bg='White', fg='Black')
	button_light.configure(bg='White', fg='Black')
	button_dark.configure(bg='White', fg='Black')

	# Update entry colors
	entry.configure(bg='White')
	entry.configure(fg='Black')
	lab.configure(font=('Arial', 10), bg='White', fg='Black')


def dark():
	window.configure(background='#252522')
	button_1.configure(bg='#081B0B', fg=entryfg)
	button_2.configure(bg='#081B0B', fg=entryfg)
	button_3.configure(bg='#081B0B', fg=entryfg)
	button_4.configure(bg='#081B0B', fg=entryfg)
	button_5.configure(bg='#081B0B', fg=entryfg)
	button_6.configure(bg='#081B0B', fg=entryfg)
	button_7.configure(bg='#081B0B', fg=entryfg)
	button_8.configure(bg='#081B0B', fg=entryfg)
	button_9.configure(bg='#081B0B', fg=entryfg)
	button_0.configure(bg='#081B0B', fg=entryfg)
	button_00.configure(bg='#081B0B', fg=entryfg)
	button_p.configure(bg='#081B0B', fg=entryfg)
	button_po.configure(bg='#081B0B', fg=entryfg)
	button_d.configure(bg='#081B0B', fg=entryfg)
	button_m.configure(bg='#081B0B', fg=entryfg)
	button_s.configure(bg='#081B0B', fg=entryfg)
	button_C.configure(bg='#081B0B', fg=entryfg)
	button_e.configure(bg='#081B0B', fg=entryfg)
	button_light.configure(bg='#081B0B', fg=entryfg)
	button_dark.configure(bg='#081B0B', fg=entryfg)

	# Update entry colors
	entry.configure(bg='#143F1A')
	entry.configure(fg='#60FF6E')
	lab.configure(font=('Arial', 10), bg=background, fg=entryfg)


# Function to clear the entry widget
def clear():
	entry.delete(0, END)


# Functions for basic arithmetic operations
def add():
	global math  # Adding a global math variable to pass into if statement of equalto function to understand which math operator
	math = "add"  # Assing add to math in this function
	global fn  # Assingning these variables as globals to use it in equalto function
	fn = entry.get()  # Saving inserted dat on entry
	entry.delete(0, END)  # Deleting that data from entry


def subtract():
	global math
	math = "sub"
	global fn
	fn = entry.get()
	entry.delete(0, END)


def multiply():
	global math
	math = "mul"
	global fn
	fn = entry.get()
	entry.delete(0, END)


def divide():
	global math
	math = "div"
	global fn
	fn = entry.get()
	entry.delete(0, END)


def equals():
	operator = 0
	sn = entry.get()  # Saving what's in there(entry) now before deleting it
	entry.delete(0, END)  # Deleting it to insert result
	if math == "add":
		entry.insert(0, float(fn) + float(sn))  # Adding the deleted data from add function to deleted data from equalto function
		# (Deleted data means the number which is present in the entry before clicking this button)

		operator = fn + " + " + sn  # Colleting data for printing history on console
	elif math == "sub":
		entry.insert(0, float(fn) - float(sn))
		operator = fn + " - " + sn  # Colleting data for printing history on console
	elif math == "mul":
		entry.insert(0, float(fn) * float(sn))
		operator = fn + " x " + sn  # Colleting data for printing history on console
	elif math == "div":
		entry.insert(0, float(fn) / float(sn))
		operator = fn + " / " + sn  # Colleting data for printing history on console

	# History
	ff = float(entry.get())  # Getting data from entry bar
	lm = (f"{ff:,}")  # Formatting the result by adding comas for easy reading
	print(operator, "=", lm)  # Printing History

	# Inserting formatted result into enry
	entry.delete(0, END)  # Deleting the data before ff to avoid two results get inserted in entry
	entry.insert(0, lm)  # Inserting formatted result into entry bar


# History needs to be improved, Have to add float values, formatting on left side of equals, putting it on screen, animating it etc:


# Creating input bar

entry = Entry(width=18, borderwidth=15, font=('Arial', 45), bg=entrybg, fg=entryfg)

entry.grid(row=0, column=0, columnspan=60)

# Creating buttons
button_1 = Button(window, text="1", padx=x, pady=y, font=('Arial', 30), command=lambda: insert(1), bg=buttonbg,
				  fg=entryfg)
button_2 = Button(window, text="2", padx=x, pady=y, font=('Arial', 30), command=lambda: insert(2), bg=buttonbg,
				  fg=entryfg)
button_3 = Button(window, text="3", padx=x, pady=y, font=('Arial', 30), command=lambda: insert(3), bg=buttonbg,
				  fg=entryfg)
button_4 = Button(window, text="4", padx=x, pady=y, font=('Arial', 30), command=lambda: insert(4), bg=buttonbg,
				  fg=entryfg)
button_5 = Button(window, text="5", padx=x, pady=y, font=('Arial', 30), command=lambda: insert(5), bg=buttonbg,
				  fg=entryfg)
button_6 = Button(window, text="6", padx=x, pady=y, font=('Arial', 30), command=lambda: insert(6), bg=buttonbg,
				  fg=entryfg)
button_7 = Button(window, text="7", padx=x, pady=y, font=('Arial', 30), command=lambda: insert(7), bg=buttonbg,
				  fg=entryfg)
button_8 = Button(window, text="8", padx=x, pady=y, font=('Arial', 30), command=lambda: insert(8), bg=buttonbg,
				  fg=entryfg)
button_9 = Button(window, text="9", padx=x, pady=y, font=('Arial', 30), command=lambda: insert(9), bg=buttonbg,
				  fg=entryfg)

button_00 = Button(window, text="00", padx=x - 11, pady=y, font=('Arial', 30), command=lambda: insert("00"),
				   bg=buttonbg, fg=entryfg)
button_0 = Button(window, text="0", padx=x1 - 2, pady=y + 3, font=('Arial', 27), command=lambda: insert(0), bg=buttonbg,
				  fg=entryfg)
button_po = Button(window, text=".", padx=x + 5, pady=y - 1, font=('Arial', 30), command=lambda: insert("."),
				   bg=buttonbg, fg=entryfg)

button_e = Button(window, text="=", padx=x, pady=y, command=equals, bg=buttonbg, fg=entryfg, font=('Arial', 30))
button_C = Button(window, text="C", padx=x, pady=y, command=clear, bg=buttonbg, fg=entryfg, font=('Arial', 30))
button_p = Button(window, text="+", padx=x, pady=y, command=add, bg=buttonbg, fg=entryfg, font=('Arial', 30))
button_s = Button(window, text="-", padx=x + 5, pady=y, command=subtract, bg=buttonbg, fg=entryfg, font=('Arial', 30))
button_m = Button(window, text="x", padx=x + 4, pady=y, command=multiply, bg=buttonbg, fg=entryfg, font=('Arial', 30))
button_d = Button(window, text="/", padx=x + 8, pady=y, command=divide, bg=buttonbg, fg=entryfg, font=('Arial', 30))

button_dark = Button(window, text="Dark", padx=x + 2, pady=y + 18, command=dark, bg=buttonbg, fg=entryfg,
					 font=('Arial', 15))
button_light = Button(window, text="Light", padx=x, pady=y + 18, command=light, bg=buttonbg, fg=entryfg,
					  font=('Arial', 15))

# Showing buttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_00.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_po.grid(row=4, column=2)

clmsp = 1

# Buttons for changing color modes
button_p.grid(row=1, column=4, columnspan=clmsp)
button_s.grid(row=2, column=4, columnspan=clmsp)
button_e.grid(row=3, column=4, columnspan=clmsp)
button_m.grid(row=1, column=5, columnspan=clmsp)
button_d.grid(row=2, column=5, columnspan=clmsp)
button_C.grid(row=3, column=5, columnspan=clmsp)

button_dark.grid(row=4, column=5)
button_light.grid(row=4, column=4)

# Show the GUI
window.mainloop()

"""

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


"""