import pyperclip
import pyshorteners
from tkinter import *

root = Tk()

# Set the geometry
root.geometry("400x200")

# Give a title
root.title("URL Shortener")

# Set a background color
root.configure(bg="#49A")

# Take 2 string variables for keeping long and short URL
url = StringVar()
url_address = StringVar()

# Define 2 functions for shortening URL and copying the URL
def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="My URL Shortener", font=("poppins", 16)).pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate Short URL", command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy URL", command=copyurl).pack(pady=5)

root.mainloop()