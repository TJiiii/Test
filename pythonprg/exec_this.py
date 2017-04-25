from tkinter import *

class App:
    def __init__(self, Parent):
        self.myParent = Parent
        self.F = Frame(Parent)
        self.F.pack()

        self.button1 = Button(self.F)
        self.button1.photo=PhotoImage(file="turtle1.png")
        self.button1.config(image=self.button1.photo,width="200",height="200")
        self.button1.pack(side=LEFT)
        self.button1.bind("<Button-1>", self.button1Click)

        self.button2 = Button(self.F)
        self.button2.photo=PhotoImage(file="brick1.png")
        self.button2.config(image=self.button2.photo,width="200",height="200")
        self.button2.pack(side=LEFT)
        self.button2.bind("<Button-1>", self.button2Click)

        self.button3 = Button(self.F)
        self.button3.photo=PhotoImage(file="pingpong1.png")
        self.button3.config(image=self.button3.photo,width="200",height="200")
        self.button3.pack(side=LEFT)
        self.button3.bind("<Button-1>", self.button3Click)

        self.button4 = Button(self.F)
        self.button4.photo=PhotoImage(file="marioworld1.png")
        self.button4.config(image=self.button4.photo,width="200",height="200")
        self.button4.pack(side=LEFT)
        self.button4.bind("<Button-1>", self.button4Click)


    def button1Click(self, event):
        import turtle_game
    def button2Click(self, event):
        sys.path.append("./brickbreak")
        import brickbreak
    def button3Click(self, event):
        sys.path.append("./pingpong")
        import pingpong
    def button4Click(self, event):
        sys.path.append("./marioworld")
        import marioworld



root=Tk()
App = App(root)
root.mainloop()