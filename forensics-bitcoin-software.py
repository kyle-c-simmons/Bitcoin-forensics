#!/usr/bin/env python3

# Author: Kyle C. Simmons

# Import all packages 
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import tkinter as tk	

import pandas as pd
import csv

import matplotlib
matplotlib.use("TkAgg")											
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 

# Setup font variables for buttons/labels
titleFont = ("Verdana", 36)			
buttonFont = ("Verdana", 15)	
helpFont = ("Verdana", 15)			

style.use('ggplot') 											# Change style of graph


# Main class and init function
class Main(tk.Tk):

	def __init__(self, *args, **kwargs):						# Always runs when class is called

		tk.Tk.__init__(self, *args, **kwargs) 					# Init tkinter
		container = tk.Frame(self) 								# Setup frame
		container.pack(side="top", fill="both", expand = True)	
		container.grid_rowconfigure(0, weight = 1)				# Setups rows / columns
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {}
		for i  in (mainMenu, graphPage, helpPage): 										
			frame = i(container, self)
			self.frames[i] = frame
			frame.grid(row= 0, column = 0, sticky = "nsew")		# Align the grid
		
		self.display(mainMenu)									# Get display function to display mainMenu


	def display(self, cont):									# Display new frame
		frame = self.frames[cont]
		frame.tkraise() 	
		self.title('Forensics Bitcoin Software')
		self.geometry('1100x800')
		frame.configure(background="#ffffff")					
		

class mainMenu(tk.Frame):										# Setup mainMenu

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)							# Init tkinter and get parent class

		label = tk.Label(self, text="Forensics Bitcoin Software", font=titleFont)
		label.configure(foreground="#000000", background="#ffffff")
		label.pack(pady=10,padx=10)

		# Graph button
		graph_btn = tk.Button(self, text="Display Graph", command=lambda: controller.display(graphPage), font=buttonFont)
		graph_btn.config(height = 2, width = 20, background = "#5F9ED4")
		graph_btn.pack(pady=(80,0)) 	

		# Help button for the helpPage
		help_btn = tk.Button(self, text="Help", command=lambda: controller.display(helpPage), font=buttonFont)
		help_btn.config(height = 2, width = 20, background = "#5F9ED4")
		help_btn.pack(pady=(20,20)) 	

		# Exit applicaton button
		exit_btn = tk.Button(self, text="Exit", command=self.exit, font=buttonFont)
		exit_btn.config(height = 2, width = 20,  background = "#5F9ED4")

		exit_btn.pack() 

	def exit(self):
		exit() # Call the built in exit function

class graphPage(tk.Frame):									# Graph page, this displays the matplotlib graph

	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Bitcoin Graph", font=titleFont)
		label.configure(foreground="#000000", background="#ffffff")
		label.pack(pady=(30,0),padx=0)

		# Ask for .csv file
		f = askopenfilename(title="Choose .csv file")

		# Return to main menu button
		back_btn = tk.Button(self, text="Back", command=lambda: controller.display(mainMenu))
		back_btn.config(height = 2, width = 20,  background = "#5F9ED4")
		back_btn.pack(pady=(0,0), padx=(0,0))

		# Configure graph on page
		pd.options.mode.chained_assignment = None
		new_f = pd.read_csv(f) #Load a csv file
		keep_col = ['value', 'timestamp'] #Get the arguments of the csv file needed
		bitcoins = new_f[keep_col] 
		bitcoins.to_csv("newFile.csv", index=False) #new csv file
		bitcoins.head() 

		# Convert date and time
		bitcoins['timestamp'] = pd.to_datetime(bitcoins.timestamp)
		bitcoins.index = bitcoins['timestamp']
		del bitcoins['timestamp']

		# Plot the data
		bitcoins.head()
		bitcoins.plot()

		# Setup graph settings
		fig = Figure(figsize=(5,5), dpi=100)
		plot = fig.add_subplot(111)
		plot.set_title('Bitcoin Graph')
		plot.set_ylabel('Y axis')
		plot.set_xlabel('Timestamps')
		plot.plot(bitcoins)
		canvas = FigureCanvasTkAgg(fig, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

# HelpPage class, this class displays all text on how to work the software
class helpPage(tk.Frame):

	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Help", font=titleFont)
		label.configure(foreground="#000000", background="#ffffff")
		label.pack(pady=(30,0),padx=10)

		back_btn = tk.Button(self, text="Back", command=lambda: controller.display(mainMenu))
		back_btn.config(height = 2, width = 20,  background = "#5F9ED4")
		back_btn.pack(pady=(0,0), padx=(0,0))

		label = tk.Label(self, text="Welcome to the Forensics Bitcoin software!\n\nThe main menu has three buttons. "
			"The first button will display the graph. The second button will display the help menu (here).\nThe last button exits the application.\n\n"
			"To display new Bitcoin data to analyse, a csv file format is required. Add the .csv file whne the application is launched\n and the data will be displayed on the graph.", font=helpPage)
		label.configure(foreground="#000000", background="#ffffff")
		label.pack(pady=(30,0),padx=10)

# Call main app
app = Main()
app.mainloop()
