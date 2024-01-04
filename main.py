import os
import json
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory

import requests

#Нажатие на кнопку открытия директории с заданиями и отчетами линии M
def open_file_M():
    global listTasksM
    global listSerReportsM
    global listReportsM
    listTasksM = list()
    listSerReportsM = list()
    listReportsM = list()
    #Очистка поля вывода
    txt_edit_M.delete("1.0", END)
    #Запрос директории
    filepath = askdirectory()
    if filepath == "":
        txt_edit_M.insert(END, "Неверно выбрана директория\n")
        return
    l = os.listdir(filepath)
    #Запись файлов Заданий и Отчета Сериализации
    try:
        for filename in l:
            if "Задание" in filename and ".txt" in filename:
                with open(filepath + '/' + filename, 'r', encoding='utf-8-sig') as file:
                    text = json.load(file)
                    listTasksM.append(text)
            if "Отчёт" in filename and ".txt" in filename:
                with open(filepath + '/' + filename, 'r', encoding='utf-8-sig') as file:
                    text = json.load(file)
                    listSerReportsM.append(text)
    except Exception as e:
        print(e)
    if 'Агрегация' not in l:
        listTasksM = list()
        listSerReportsM = list()
        listReportsM = list()
        txt_edit_M.insert(END, "В данной директории нет папки 'Агрегация'\n")
        return
    # Запись файлов Отчетов Агрегации
    l = os.listdir(filepath + '/Агрегация')
    try:
        for filename in l:
            if "Отчёт" in filename and ".txt" in filename:
                with open(filepath + '/Агрегация/' + filename, 'r', encoding='utf-8-sig') as file:
                    text = json.load(file)
                    listReportsM.append(text)
    except Exception as e:
        print(e)

    if len(listTasksM) == 0:
        txt_edit_M.insert(END, "Текст задания не найден, введите другую директорию\n")
    else:
        txt_edit_M.insert(END, f"Количество заданий: {len(listTasksM)}\n")
        for task in listTasksM:
            txt_edit_M.insert(END, f"{task['id']}\n")
    if len(listSerReportsM) == 0:
        txt_edit_M.insert(END, "Текст задания не найден, введите другую директорию\n")
    else:
        txt_edit_M.insert(END, f"Количество заданий: {len(listSerReportsM)}\n")
        for serReport in listSerReportsM:
            txt_edit_M.insert(END, f"{serReport['id']}\n")
    if len(listReportsM) == 0:
        txt_edit_M.insert(END, "Текст отчётов с агрегаций не найден, введите другую директорию\n")
    else:
        txt_edit_M.insert(END, f"Количество отчётов агрегаций: {len(listReportsM)}\n")
        for report in listReportsM:
            txt_edit_M.insert(END, f"{report['id']}\n")

#Нажатие на кнопку открытия директории с заданиями и отчетами линии S
def open_file_S():
    global listTasksS
    global listReportsS
    listTasksS = list()
    listReportsS = list()
    # Очистка поля вывода
    txt_edit_S.delete("1.0", END)
    #Запрос директории
    filepath = askdirectory()
    if filepath == "":
        txt_edit_S.insert(END, "Неверно выбрана директория\n")
        return
    # Запись файлов Заданий и Отчетов
    l = os.listdir(filepath)
    try:
        for filename in l:
            if "Задание" in filename and ".txt" in filename:
                with open(filepath + '/' + filename, 'r', encoding='utf-8') as file:
                    text = json.load(file)
                    listTasksS.append(text)
            if "Отчёт" in filename and ".txt" in filename:
                with open(filepath + '/' + filename, 'r', encoding='utf-8') as file:
                    text = json.load(file)
                    listReportsS.append(text)
    except Exception as e:
        print(e)
    if len(listTasksS) == 0:
        txt_edit_S.insert(END, "Текст заданий не найден, введите другую директорию\n")
    else:
        txt_edit_S.insert(END, f"Количество заданий: {len(listTasksS)}\n")
        for task in listTasksS:
            txt_edit_S.insert(END, f"{task['id']}\n")
    if len(listReportsS) == 0:
        txt_edit_S.insert(END, "Текст отчётов не найден, введите другую директорию\n")
    else:
        txt_edit_S.insert(END, f"Количество отчётов: {len(listReportsS)}\n")
        for report in listReportsS:
            txt_edit_S.insert(END, f"{report['id']}\n")

def printingM():
    print(listTasksM)
    print(listSerReportsM)
    print(listReportsM)

def printingS():
    print(listTasksS)
    print(listReportsS)


listTasksS = list()
listReportsS = list()
listTasksM = list()
listSerReportsM = list()
listReportsM = list()
window = Tk()
window.title("BrakFounderPy")
window.geometry('400x250')
window.minsize(width=400, height=250)
tab_control = ttk.Notebook(window)
tabM = ttk.Frame(tab_control)
tabS = ttk.Frame(tab_control)
tab_control.add(tabM, text='Линия M')
tab_control.add(tabS, text='Линия S')
tab_control.pack(expand=1, fill='both')
# Вкладка линии M
tabM.rowconfigure(0, minsize=800, weight=1)
tabM.columnconfigure(1, minsize=800, weight=1)
txt_edit_M = Text(tabM)
fr_buttons_M = Frame(tabM)
btn_open_M = Button(fr_buttons_M, text="Открыть", command=open_file_M)
btn_save_M = Button(fr_buttons_M, text="Сохранить как...", command=printingM)
btn_open_M.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save_M.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons_M.grid(row=0, column=0, sticky="ns")
txt_edit_M.grid(row=0, column=1, sticky="nsew")
# Вкладка Линии S
tabS.rowconfigure(0, minsize=800, weight=1)
tabS.columnconfigure(1, minsize=800, weight=1)
txt_edit_S = Text(tabS)
fr_buttons_S = Frame(tabS)
btn_open_S = Button(fr_buttons_S, text="Открыть", command=open_file_S)
btn_save_S = Button(fr_buttons_S, text="Сохранить как...", command=printingS)
btn_open_S.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save_S.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons_S.grid(row=0, column=0, sticky="ns")
txt_edit_S.grid(row=0, column=1, sticky="nsew")

window.mainloop()
