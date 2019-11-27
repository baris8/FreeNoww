from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from Filter import Filter

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x350")
        self.window.title("FreeNow Filter - by Baris Üctas")

        self.file = None
        self.v = StringVar(self.window, "jan")

        self.initialize()


    def open_csv(self):
        global file
        global data_area
        file_name = askopenfilename(title = "Open File", filetypes = (("CSV Files","*.csv"),))
        with open(file_name, "r") as f:
            self.data_area.insert(1.0, f.read())
        file = open(file_name, "r")
        if file is None:
            messagebox.showerror("Could not open file", "Please try again!")

    def print_file(self):
        if file is not None:
            print(file.read())
        else:
            messagebox.showerror("Open a File", "Please open a File first!")

    def save_files(self):
        if file is not None:
            fil = Filter(file)
            fil.filter_rides()
            fil.export_to_file(self.v.get())

            #self.window.destroy()
        else:
            messagebox.showerror("Open a File", "Please open a File first!")


    def initialize(self):
        # Menu Bar
        self.menu_bar = Menu(self.window)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Datei öffnen", command=self.open_csv)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.window.config(menu=self.menu_bar)

        # Text Area
        self.data_frame = Frame(self.window).pack()
        self.data_area = Text(self.data_frame, state = DISABLED).pack()


        # Radio Buttons
        values = {"Januar": "jan",
                  "Februar": "feb",
                  "März": "mar",
                  "April": "apr",
                  "Mai": "mai",
                  "Juni": "jun",
                  "Juli": "jul",
                  "August": "aug",
                  "September": "sep",
                  "Oktober": "okt",
                  "November": "nov",
                  "Dezember": "dez"}
        i = 0
        for (text, value) in values.items():
            Radiobutton(self.window, text=text, variable=self.v, value=value).place(x=210, y=((i * 20) + 10))
            i = i + 1

        # Save Button
        save_btn = Button(self.window, text="Save Files", command=self.save_files).place(x=210, y=280)

        # Print Button
        print_btn = Button(self.window, text="Print File", command=self.print_file).place(x=210, y=320)

        self.window.mainloop()


if __name__ == '__main__':
    gui = GUI()
