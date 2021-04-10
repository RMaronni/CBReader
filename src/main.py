from cbz import cbz
from progress import progress
import time
from PIL import Image
from PIL import ImageTk
import tkinter as Tk
from enum import Enum


#file = "C:\\Users\\renan\\Desktop\\HQ\\Supergirl v01 - Last Daughter of Krypton (2011) (Digital) (AnHeroGold-Empire).cbz"
file = "C:\\Users\\renan\\Desktop\\HQ\\teste.cbz"

FIT        = 1
FIT_WIDTH  = 2
FIT_HEIGHT = 3
ORIGINAL   = 4



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
    c.close()
    root.destroy()


def set_size_original(event):
    print("Size: Original.")
    global img_size
    img_size = ORIGINAL
    img_path = c.current_page()
    update_image(img_path)



def set_size_fit_width(event):
    print("Size: Fit width.")
    global img_size
    img_size = FIT_WIDTH
    img_path = c.current_page()
    update_image(img_path)



def set_size_fit_height(event):
    print("Size: Fit height.")
    global img_size 
    img_size = FIT_HEIGHT
    img_path = c.current_page()
    update_image(img_path)


def set_size_fit(event):
    print("Size: Fit.")
    global img_size
    img_size = FIT
    img_path = c.current_page()
    update_image(img_path)


def move_up(event):
    canvas.move(canvas_img, 0, 30)

def move_down(event):
    canvas.move(canvas_img, 0, -30)

def move_right(event):
    canvas.move(canvas_img, -30, 0)

def move_left(event):
    print(canvas.coords(canvas_img))
    canvas.move(canvas_img, 30, 0)


def update_image(img_path):
    print(img_path)
    img = Image.open(img_path)
    size = get_size(img)
    img = img.resize(size, Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    canvas.image = img_tk

    canvas.itemconfig(canvas_img, image=canvas.image)

    # Set padding
    if screen_width > size[0]: 
        padding_x = (screen_width-size[0])/2
    else:
        padding_x = 0

    if screen_height > size[1]: 
        padding_y = (screen_height-size[1])/2
    else:
        padding_y = 0

    canvas.pack(side="top", fill="both", expand="yes", anchor='n', padx=padding_x, pady=padding_y)


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


def get_size_fit(img):
    width, height = img.size

    if width > height:
        return get_size_fit_width(img)
    else:
        return get_size_fit_height(img)



def get_size_original(img):
    return img.size  


def get_size(img):
    if img_size == FIT:
        return get_size_fit(img)
    elif img_size == FIT_WIDTH:
        return get_size_fit_width(img)
    elif img_size == FIT_HEIGHT:
        return get_size_fit_height(img)
    elif img_size == ORIGINAL:
        return get_size_original(img)



         









img_size = FIT


root = Tk.Tk()


screen_width  = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas = Tk.Canvas(root, width=screen_width, height=screen_height)

root.bind("<Next>", next)
root.bind("<Prior>", previous)
root.bind("<Escape>", quit)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Right>", move_right)
root.bind("<Left>", move_left)
root.bind("1", set_size_fit)
root.bind("2", set_size_fit_width)
root.bind("3", set_size_fit_height)
root.bind("4", set_size_original)



c = cbz(file)
c.load_file()

prog = progress()


 
page = prog.load(c.get_md5())
if page:
    img_path = c.page(page)
else:
    img_path = c.first_page()

canvas_img = canvas.create_image(0, 0, anchor='nw')
update_image(img_path)







root.attributes("-fullscreen", True)
root.mainloop()







