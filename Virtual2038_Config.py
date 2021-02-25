import sys
import json
import os
import re
import tkinter
from tkinter import messagebox
from tkinter import colorchooser
import tkinter.filedialog
datas = open("config.json")
data = json.loads(datas.read())
datas.close()
root = tkinter.Tk()
root.title("Virtual2038 Configuration")
root.geometry("360x480")
root.resizable(width=0, height=0)
root.iconbitmap('icons/icon.ico')


def SetValue():
    if(re.match(r"[0123456ABCDEF]{6}", backcolor_box.get())):
        data["backcolor"] = backcolor_box.get()
    else:
        messagebox.showwarning(
            "Error", "Background color's text is Inaccurate")
    if(re.match(r"[0123456ABCDEF]{6}", textcolor_box.get())):
        data["textcolor"] = textcolor_box.get()
    else:
        messagebox.showwarning(
            "Error", "Background color's text is Inaccurate")
    if CheckImage.get() == True:
        if(os.path.isfile(backimage_box.get())):
            data["background_image"] = backimage_box.get()
        else:
            data["background_image"] = None
    else:
        data["background_image"] = None
    data_str = json.dumps(data, indent=4)
    with open("config.json", "w") as datas:
        datas.write(data_str)


def SetAndExit():
    SetValue()
    root.quit()
    sys.exit(0)


def Cancel():
    root.quit()
    sys.exit(0)


def SetBackValue():
    color = colorchooser.askcolor()
    if(color[1] != None):
        color_text = color[1].replace("#", "", 1).upper()
        backcolor_box.delete(0, tkinter.END)
        backcolor_box.insert(tkinter.END, color_text)


def SetForeValue():
    color = colorchooser.askcolor()
    if(color[1] != None):
        color_text = color[1].replace("#", "", 1).upper()
        textcolor_box.delete(0, tkinter.END)
        textcolor_box.insert(tkinter.END, color_text)


def UseSet():
    global CheckImage
    global backimage_box
    global backimage_button
    if CheckImage.get() == True:
        backimage_box = tkinter.Entry(width=50)
        backimage_box.place(x=3, y=106)

        backimage_button = tkinter.Button(
            root, text='参照', width=5, command=SetFileValue)
        backimage_button.place(x=310, y=102)
    else:
        backimage_box.destroy()
        backimage_button.destroy()


def SetFileValue():
    file_path = tkinter.filedialog.askopenfilename(filetypes=[(
        "Image file", "*.png; *.jpg; *.jpeg; *.bmp; *.tcx; *.tga; *.tif; *.lbm; *.pbm; *.ppm; *.pgm; *.xpm;")])
    if(len(file_path) != 0):
        backimage_box.delete(0, tkinter.END)
        backimage_box.insert(tkinter.END, file_path)


CheckImage = tkinter.BooleanVar()

backcolor_text = tkinter.Label(text='Background Color')
backcolor_text.place(x=0, y=0)

backcolor_box = tkinter.Entry(width=50)
backcolor_box.insert(tkinter.END, data["backcolor"])
backcolor_box.place(x=3, y=23)

backcolor_button = tkinter.Button(
    root, text='参照', width=5, command=SetBackValue)
backcolor_button.place(x=310, y=19)

textcolor_text = tkinter.Label(text='Text Color')
textcolor_text.place(x=0, y=40)

textcolor_box = tkinter.Entry(width=50)
textcolor_box.insert(tkinter.END, data["textcolor"])
textcolor_box.place(x=3, y=60)

textcolor_button = tkinter.Button(
    root, text='参照', width=5, command=SetForeValue)
textcolor_button.place(x=310, y=56)

BackImage_Check = tkinter.Checkbutton(
    text="Use background image", command=UseSet, variable=CheckImage)
BackImage_Check.place(x=0, y=80)
if(data["background_image"] != None):
    CheckImage.set(True)
    UseSet()
    backimage_box.delete(0, tkinter.END)
    backimage_box.insert(tkinter.END, data["background_image"])

OK_Button = tkinter.Button(root, text='OK', width=5, command=SetAndExit)
OK_Button.place(x=305, y=445)

OK_Button = tkinter.Button(root, text='Cancel', width=5, command=Cancel)
OK_Button.place(x=255, y=445)

OK_Button = tkinter.Button(root, text='Apply', width=5, command=SetValue)
OK_Button.place(x=205, y=445)

root.mainloop()
