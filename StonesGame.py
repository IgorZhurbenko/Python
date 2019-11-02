import tkinter as tk

class stones:
    def __init__(self,startingquantity):
        self.startingquantity = startingquantity
        self.currentquantity = startingquantity
        self.memory = list()
    def takeout(self,amount):
        if self.currentquantity>= amount:
            self.currentquantity =  self.currentquantity - amount
            self.memory.append(amount)
        else:
            self.memory.append(self.currentquantity)
            self.currentquantity = 0
    def renew(self):
        self.currentquantity = startingquantity
        self.memory = list()
    def print_in(self,root):
        circles = []
        canvas = tk.Canvas(root, width=1000, height=1000, borderwidth=0, highlightthickness=0, bg="Grey")
        for i in range(self.currentquantity):
            circles.append(canvas.create_oval(10+i*60,10,50+i*60,50,fill = "green"))
        canvas.pack()
        return circles
def move(event):
    event.widget.x = obj.x + 1

    
 
    
#________________________________________

root = tk.Tk()

stones = stones(15)

circles = stones.print_in(root)

for i in circles:
    print(i)

#activate(circles[0],move)

"""canvas = tk.Canvas(root, width=1000, height=1000, borderwidth=0, highlightthickness=0, bg="white")

#canvas.create_oval(100, 100, 150, 150,fill="green", outline="")

canvas.pack()"""

root.mainloop()





    
        
