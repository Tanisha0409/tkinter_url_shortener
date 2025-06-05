from tkinter import *
import pyshorteners


def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))
    
root = Tk()
root.title ("url shortner")
root.geometry("300x270")


#creating label
label = Label(root, text="URL Shortner!",bg='black', fg='white', font=("arial", 15) )
longurl_label = Label(root, text="Enter Long URL")
longurl_entry = Entry(root)
shorturl_label = Label(root, text="Created Short URL")
shorturl_entry = Entry(root)
shortenurl_button = Button(root, text="Shorten URL",command=shorten)


#placing widget on screen
label.pack()
longurl_label.pack() 
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shortenurl_button.pack() 



root.mainloop()