from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from Filter import Filter


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x350")
        self.window.title("FreeNow Filter - by Baris Üctas")

        self.open_btn = Button(self.window, text="Öffne Datei", command=self.open_file)
        self.open_btn.pack(side=TOP, expand=YES)

        self.file = None
        self.v = StringVar(self.window, "01")

        self.window.mainloop()

    def open_file(self):
        global file
        file_name = askopenfilename(title="Open File", filetypes=(("CSV Files", "*.csv"),))
        self.file = open(file_name, "r", encoding='utf-8')
        if self.file is None:
            messagebox.showerror("Could not open file", "Please try again!")
        else:
            self.next_page()

    def next_page(self):
        self.open_btn.destroy()
        self.label = Label(self.window, text="Bitte wähle einen Monat aus und drück auf speichern.").pack()

        # Radio Buttons
        values = {"Januar": "01",
                  "Februar": "02",
                  "März": "03",
                  "April": "04",
                  "Mai": "05",
                  "Juni": "06",
                  "Juli": "07",
                  "August": "08",
                  "September": "09",
                  "Oktober": "10",
                  "November": "11",
                  "Dezember": "12"}
        for (text, value) in values.items():
            Radiobutton(self.window, text=text, variable=self.v, value=value).pack()

        self.save_btn = Button(self.window, text="Speichern", command=self.save_files)
        self.save_btn.pack(side=RIGHT, expand=YES)

    def save_files(self):
        filter = Filter(self.file)
        filter.filter_rides(self.v.get())
        filter.export_to_file(self.v.get())
        self.window.destroy()


if __name__ == '__main__':
    gui = GUI()
