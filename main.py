from student import Students
from tkinter import *

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

window = Tk()

window.wm_title("Add Student")
window.geometry("300x300")
display = Students(window)

window.mainloop()

