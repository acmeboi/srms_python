from tkinter import *
from openpyxl import Workbook

class Students:

    def __init__(self, master):
        self.master = master
        self.fram = Frame(self.master)

        btn = Button(self.fram, text="Exit", command=self.exitWindow);
        btn.place(x=100, y=100)

        btnAddStudent = Button(self.fram, text="Save Student Info", command=self.saveStudentInf);
        btnAddStudent.place(x=100, y=50)

        self.fram.pack(fill=BOTH, expand=1)

    def exitWindow(self):
        exit();

    def saveStudentInf(self):
        studentDatabase = Workbook()
        sheet = studentDatabase.active

        sheet['A1'] = "Name"
        sheet['B1'] = "CA"
        sheet['C1'] = "Exam"
        sheet['D1'] = "Total"

        sheet['A2'] = "Isa Muhammed"
        sheet['B2'] = "10"
        sheet['C2'] = "30"
        sheet['D2'] = 30 + 30
        studentDatabase.save(filename="studentDatabase.xlsx")

        msg = Label(self.fram, text="Save Successfull")
        msg.place(x=100, y=150)
        self.fram.pack(fill=BOTH, expand=1)
