from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk


def resize(*args):
    try:
        filenames = filedialog.askopenfilenames()
        for filename in filenames:
            image = Image.open(filename)
            w = image.size[0]
            h = image.size[1]
            picsize = w * h * 3 / 1024
            newsize = float(size.get())
            ratio = picsize / newsize
            image.thumbnail((w / ratio, h / ratio))
            image.save('/'.join(i for i in filename.split('/')[:-1]) + '/resized_' + filename.split('/')[-1])
        # meters.set(int(value))
    except ValueError:
        pass

if __name__ == "__main__":
    root = Tk()
    root.title("Resize your images!")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    size = StringVar()
    desired_size = ttk.Entry(mainframe, width=7, textvariable=size)
    desired_size.grid(column=2, row=2, sticky=(W, E))

    ttk.Button(mainframe, text="Resize", command=resize).grid(column=4, row=3, sticky=W)

    ttk.Label(mainframe, text="the size you want").grid(column=1, row=2, sticky=W)

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    desired_size.focus()

    root.mainloop()
