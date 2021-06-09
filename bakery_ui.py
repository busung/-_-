import tkinter
from tkinter import *
import tkinter as tk

class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        self.sand_var = tk.StringVar()
        self.cake_var = tk.StringVar()
        window.title("고객: " + self.name)
        window.geometry('350x200')
        label = Label(window,text="샌드위치 (5000원)")
        sand_entry=tk.Entry(window,width=7,textvariable=self.sand_var)
        label.pack()
        sand_entry.pack()
        label = Label(window, text="케이크 (20000원)")
        cake_entry = Entry(window, width=7,textvariable=self.cake_var)
        label.pack()
        cake_entry.pack()
        button = Button(window,text="주문하기",command=self.send_order)
        button.pack()


    def send_order(self):
        sand_str = self.sand_var.get()
        cake_str = self.cake_var.get()
        sandwich_Text=""
        cake_Text=""
        if not sand_str.isalpha() and int(sand_str) > 0:
            sandwich_Text = "샌드위치 (5000원) "+sand_str+"개"
        if not cake_str.isalpha() and int(cake_str) > 0:
            cake_Text= "케이크 (20000원) "+cake_str+"개"
        if (sand_str.isalpha() or int(sand_str) < 0) and (cake_str.isalpha() or int(cake_str) < 0):
            return

        if sandwich_Text =="":
            order_text = self.name + ": " + cake_Text
            self.bakeryView.add_order(order_text)
            return

        if cake_Text=="":
            order_text = self.name+ ": " + sandwich_Text
            self.bakeryView.add_order(order_text)
            return

        order_text = self.name + ": " + sandwich_Text + ", "+cake_Text
        self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
