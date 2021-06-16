import tkinter as tk
class FileMenu(tk.Menu):
    def __init__ (self, parent):
        tk.Menu.__init__(self, parent, tearoff=False)
        self.add_command(label='Exit', command=self.quit)

class MainMenu(tk.Menu):
    def __init__ (self, parent):
        tk.Menu.__init__(self, parent, tearoff=False)
        self.file_menu = FileMenu(self)
        self.add_cascade(label='File', menu=self.file_menu)

class View:
    def __init__ (self, parent):
        self.frame = tk.Frame(parent)
        self.parent = parent
        self.menu = MainMenu(self.frame)
        self.parent.configure(menu=self.menu)
        self.parent.geometry('200x200')
        self.frame.pack(fill='both', expand=True)

class App:
    def __init__ (self):
        self.root = tk.Tk()
        self.view = View(self.root)

    def run (self):
        self.root.title('Window Title')
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()

while True:
	s = input('please enter:')
	if s == 'ok':
		break
	print ('Length of the string is', len(s))
print ('Done!')