from cbz import cbz
from progress import progress
import time
from PIL import Image
from PIL import ImageTk
import tkinter as tk
from enum import Enum


file = "C:\\Temp\\Temp.cbz"

progress_file = "C:\\Temp\\progress.json"
progress_dict = None


ORIGINAL   = 1
FIT_WIDTH  = 2
FIT_HEIGHT = 3




def next(event):
    print("Next")
    img_path = c.next_page()
    update_image(img_path)
    

def previous(event):
    print("Previous")
    img_path = c.previous_page()
    update_image(img_path)


def quit(event):
    print("Quit")
    prog.save(c.get_md5(), c.get_current_index())
    root.destroy()


def set_size_original(event):
    print("Size: Original")
    global img_size
    img_size = ORIGINAL
    img_path = c.current_page()
    update_image(img_path)



def set_size_fit_width(event):
    print("Size: Fit width")
    global img_size
    img_size = FIT_WIDTH
    img_path = c.current_page()
    update_image(img_path)



def set_size_fit_height(event):
    print("Size: Fit height")
    global img_size 
    img_size = FIT_HEIGHT
    img_path = c.current_page()
    update_image(img_path)



def update_image(img_path):
    img = Image.open(img_path)
    size = get_size(img)
    img = img.resize(size, Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    panel.configure(image=img_tk)
    panel.image = img_tk
    panel.pack(side="bottom", fill="both", expand="yes")



def get_size_fit_width(img):
    width, height = img.size
    ratio = (width / height)

    new_width = screen_width
    new_height = int(new_width / ratio)

    return (new_width, new_height)


def get_size_fit_height(img):
    width, height = img.size
    ratio = (width / height)

    new_height = screen_height
    new_width = int(new_height * ratio)

    return (new_width, new_height)


def get_size_original(img):
    return img.size  


def get_size(img):
    if img_size == ORIGINAL:
        return get_size_original(img)
    elif img_size == FIT_WIDTH:
        return get_size_fit_width(img)
    elif img_size == FIT_HEIGHT:
        return get_size_fit_height(img)



         









img_size = ORIGINAL


root = tk.Tk()
panel = tk.Label(root)
root.bind("<Right>", next)
root.bind("<Left>", previous)
root.bind("<Escape>", quit)
root.bind("1", set_size_original)
root.bind("2", set_size_fit_width)
root.bind("3", set_size_fit_height)


screen_width  = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

c = cbz(file)
c.load_file()

prog = progress()


 
page = prog.load(c.get_md5())
if page:
    img_path = c.page(page)
else:
    img_path = c.first_page()


update_image(img_path)








root.mainloop()







