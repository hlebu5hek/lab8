'''Объекты – студенты
Функции:	сегментация полного списка студентов по курсам
визуализация предыдущей функции в форме круговой диаграммы
сегментация полного списка студентов по успеваемости
визуализация предыдущей функции в форме круговой диаграммы'''

from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as p

root = Tk()
root.title("Students")
root.geometry('420x480')
root.resizable(False, False)

students = []

class student():
    name, surname, year = '', '', 0
    marks = {'mark': '0'}

    def __init__(self, name, surname, year, marks):
        self.name = name
        self.surname = surname
        self.year = year
        self.marks = marks


def prop(n):
    return 360.0 * n / 1000


def sort_by_year(enter = students):
    out = [[],[],[],[]]

    enter.sort(key=lambda x: x.year)
    j = 1
    for i in enter:
        if int(i.year) > j:
            j = int(i.year)
        out[j-1].append(i)
    for i in range(len(out)):
        out[i].sort(key=lambda x: x.surname)

    stList = []
    for i in enter:
        stList.append(i.name + ' ' + i.surname + ', Курс: ' + i.year)
    PrintList(stList)
    pie = []
    for i in out:
        pie.append(len(i))
    drawPie(pie, ['1 курс', '2 курс', '3 курс', '4 курс'])


# все 5, 5 больше, 4 больше, есть 3. Все зачтено, есть долги
def sort_by_marks():
    out = [[],[],[],[],[]]
    marks_only = list(map(lambda x: list(x.marks.values()), students))
    for i in range(len(students)):
        a = marks_only[i].count(5)
        b = marks_only[i].count(4)
        c = marks_only[i].count(3)
        f = marks_only[i].count(0)
        if c == 0 and b == 0 and f == 0: out[0].append(students[i])
        elif c == 0 and f == 0 and a > b: out[1].append(students[i])
        elif c == 0 and f == 0 and a <= b: out[2].append(students[i])
        elif c != 0 and f == 0: out[3].append(students[i])
        else: out[4].append(students[i])
    for i in range(len(out)):
        out[i].sort(key=lambda x: x.surname)

    stList = []
    for i in out:
        for j in i:
            stList.append(j.name + ' ' + j.surname + ', Курс: ' + j.year)
    PrintList(stList)
    pie = []
    for i in out:
        pie.append(len(i))
    drawPie(pie, ['все 5', '5 больше', '4 больше', 'есть 3', 'есть долги'])


def loadStudents():
    stList = []
    filename = entryf.get()

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            a = line.split(' ')
            m = a[3].split(';')
            marks = {}
            for i in m:
                marks[i.split(',')[0]] = int(i.split(',')[1].replace('\n', ''))

            st = student(a[0], a[1], a[2], marks)
            students.append(st)
            stList.append(a[0] + ' ' + a[1] + ', Курс: ' + a[2] + '\n')

    PrintList(stList)


def PrintList(list):
    studListd = StringVar(value=list)
    listboxd = Listbox(listvariable=studListd)
    listboxd.place(anchor=NW, x=15, y=65, width=385, height=360)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listboxd.yview)
    scrollbar.place(anchor=NW, y=65, x=385, width=20, height=360)
    listboxd["yscrollcommand"] = scrollbar.set

def drawPie(entry, labels):
    p.pie(x=entry, labels=labels)
    p.show()


#tkinter
btn = ttk.Button(text="Загрузить из файла", command=loadStudents)
btn.place(anchor=NW, x = 250, y = 20, height = 25, width = 150)

btnSort1 = ttk.Button(text="Сортировать по курсу", command=sort_by_year)
btnSort1.place(anchor=NW, x = 15, y = 440, height = 25, width = 170)

btnSort2 = ttk.Button(text="Сортировать по оценкам", command=sort_by_marks)
btnSort2.place(anchor=NW, x = 230, y = 440, height = 25, width = 170)

labelFile = ttk.Label(text="Имя файла:")
labelFile.place(anchor=NW, x = 15, y = 20, height = 25)
entryf = ttk.Entry()
entryf.place(anchor=NW, x = 90, y = 20, height = 25, width = 150)

studListd = StringVar(value=[])
listboxd = Listbox(listvariable=studListd)
listboxd.place(anchor=NW, x = 15, y = 65, width = 385, height = 360)

scrollbar = ttk.Scrollbar(orient="vertical", command=listboxd.yview)
scrollbar.place(anchor=NW, y = 65, x = 385, width = 20, height = 360)
listboxd["yscrollcommand"] = scrollbar.set

root.mainloop()