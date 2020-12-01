import tkinter as tk

userName = ""

class nameChanger(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, legalFrame, prefFrame, diplomaFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        name = tk.Entry(self)
        nameLabel = tk.Label(self, text="Please enter your name")
        nameLabel.pack(side="top", pady=10)
        name.pack(side="top")
        label = tk.Label(self, text="Please choose the type of name change")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Legal",
                            command=lambda: controller.show_frame("LegalFrame"))
        button2 = tk.Button(self, text="Preferred",
                            command=lambda: controller.show_frame("PrefFrame"))
        button1.pack()
        button2.pack()


class LegalFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Legal Name Change")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PrefFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Preferred Name Change")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class DiplomaFrame(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Diploma Info")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = nameChanger()
    app.mainloop()