from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from tkinter import *
from tkinter.ttk import *
import tkinter as tk 

window = Tk()
window.title("Search In Bing")
window.geometry("800x600")

lbl = tk.Label(window, text = "Search", font=("Arial Bold", 40), fg = "blue")
top_label = tk.Label(window, text = "Bing", font=("Arial Bold", 50), fg = "green")

lbl.place(x = 20, y = 220)
top_label.pack(side = TOP)

search_entry = Entry(window, width = 60)

search_entry.place(x = 270, y = 240)

def clicked():
	driver = webdriver.Chrome()

	driver.get("Https://www.bing.com/")

	elem = driver.find_element_by_name("q")

	elem.clear()

	elem.send_keys(search_entry.get())

	elem.send_keys(Keys.RETURN)


btn = Button(window, text = "Search", command = clicked)

btn.place(x = 640, y = 240)

window.mainloop()