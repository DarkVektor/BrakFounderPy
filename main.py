import os
import json
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory

#Нажатие на кнопку открытия директории с заданиями и отчетами линии M
def open_file_M():
    btn_exe_M["state"] = "normal"
    btn_save_M["state"] = "disabled"
    global pathM
    global listTasksM
    global listSerReportsM
    global listReportsM
    pathM = ""
    listTasksM = list()
    listSerReportsM = list()
    listReportsM = list()
    #Очистка поля вывода
    txt_edit_M.delete("1.0", END)
    #Запрос директории
    filepath = askdirectory()
    if filepath == "":
        txt_edit_M.insert(END, "Неверно выбрана директория\n")
        btn_exe_M["state"] = "disabled"
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
        btn_exe_M["state"] = "disabled"
        txt_edit_M.insert(END, f"{e}\n")
        listTasksM.clear()
        listSerReportsM.clear()
        return
    if 'Агрегация' not in l:
        listTasksM.clear()
        listSerReportsM.clear()
        txt_edit_M.insert(END, "В данной директории нет папки 'Агрегация'\n")
        btn_exe_M["state"] = "disabled"
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
        btn_exe_M["state"] = "disabled"
        txt_edit_M.insert(END, f"{e}\n")
        listTasksM.clear()
        listSerReportsM.clear()
        listReportsM.clear()
        return

    if len(listTasksM) == 0:
        txt_edit_M.insert(END, "Текст задания не найден, введите другую директорию\n")
        btn_exe_M["state"] = "disabled"
        listTasksM.clear()
        listSerReportsM.clear()
        listReportsM.clear()
        return
    else:
        txt_edit_M.insert(END, f"Количество заданий: {len(listTasksM)}\n")
        for task in listTasksM:
            txt_edit_M.insert(END, f"{task['id']}\n")
    if len(listSerReportsM) == 0:
        txt_edit_M.insert(END, "Текст задания не найден, введите другую директорию\n")
        btn_exe_M["state"] = "disabled"
        listTasksM.clear()
        listSerReportsM.clear()
        listReportsM.clear()
        return
    else:
        txt_edit_M.insert(END, f"Количество отчётов сериализаций: {len(listSerReportsM)}\n")
        for serReport in listSerReportsM:
            txt_edit_M.insert(END, f"{serReport['id']}\n")
    if len(listReportsM) == 0:
        txt_edit_M.insert(END, "Текст отчётов с агрегаций не найден, введите другую директорию\n")
        btn_exe_M["state"] = "disabled"
        listTasksM.clear()
        listSerReportsM.clear()
        listReportsM.clear()
        return
    else:
        txt_edit_M.insert(END, f"Количество отчётов агрегаций: {len(listReportsM)}\n")
        for report in listReportsM:
            txt_edit_M.insert(END, f"{report['id']}\n")
    pathM = filepath

#Нажатие на кнопку открытия директории с заданиями и отчетами линии S
def open_file_S():
    btn_exe_S["state"] = "normal"
    btn_save_S["state"] = "disabled"
    global pathS
    global listTasksS
    global listReportsS
    pathS = ""
    listTasksS = list()
    listReportsS = list()
    # Очистка поля вывода
    txt_edit_S.delete("1.0", END)
    #Запрос директории
    filepath = askdirectory()
    if filepath == "":
        txt_edit_S.insert(END, "Неверно выбрана директория\n")
        btn_exe_S["state"] = "disabled"
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
        btn_exe_S["state"] = "disabled"
        txt_edit_S.insert(END, f"{e}\n")
        listTasksS.clear()
        listReportsS.clear()
        return
    if len(listTasksS) == 0:
        txt_edit_S.insert(END, "Текст заданий не найден, введите другую директорию\n")
        btn_exe_S["state"] = "disabled"
        listTasksS.clear()
        listReportsS.clear()
        return
    else:
        txt_edit_S.insert(END, f"Количество заданий: {len(listTasksS)}\n")
        for task in listTasksS:
            txt_edit_S.insert(END, f"{task['id']}\n")
    if len(listReportsS) == 0:
        txt_edit_S.insert(END, "Текст отчётов не найден, введите другую директорию\n")
        btn_exe_S["state"] = "disabled"
        listTasksS.clear()
        listReportsS.clear()
        return
    else:
        txt_edit_S.insert(END, f"Количество отчётов: {len(listReportsS)}\n")
        for report in listReportsS:
            txt_edit_S.insert(END, f"{report['id']}\n")
    pathS = filepath

#Выполняет поиск ошибок
def executeM():
    global TextReportM
    TextReportM = ""
    btn_save_M["state"] = "normal"
    btn_exe_M["state"] = "disable"
    if (len(listTasksM) and len(listSerReportsM) and len(listReportsM)) != 0:
        #Создание словаря и проверка пачек на дубли из задания Сериализации
        dictTaskPacksM = dict()
        dublesTasks = ""
        for task in listTasksM:
            for packs in task["productNumbers"]:
                if dictTaskPacksM.get(packs["Number"], None):
                    dublesTasks += f"{packs['Number']} в задании уже есть\n"
                else:
                    dictTaskPacksM[packs["Number"]] = 1
        #Проверка пачек на дубли и принадлежность их заданию
        dictReportsPacks = dict()
        dictBoxs = dict()
        dublesPacks = ""
        dublesBoxs = ""
        otherErrors = ""
        for report in listReportsM:
            for box in report["readyBox"]:
                if dictBoxs.get(box['boxNumber'], None):
                    dublesBoxs += f"{box['boxNumber']} уже есть в {report['id']}/{box['Number']} и в {dictBoxs[box['boxNumber']]}"
                else:
                    dictBoxs[box['boxNumber']] = f"{report['id']}/{box['Number']}"
                    for pack in box["productNumbers"]:
                        if dictTaskPacksM.get(pack, None):
                            if dictReportsPacks.get(pack, None):
                                dublesPacks += f"{pack} в коробах {dictReportsPacks[pack]} и {box['boxNumber']}\n"
                            else:
                                dictReportsPacks[pack] = box["boxNumber"]
                        else:
                            otherErrors += f"{pack} в коробе {box['boxNumber']} отсутствует в тексте задания\n"
        #Вывод текста ошибок
        if dublesTasks == "" and dublesPacks == "" and otherErrors == "" and dublesBoxs == "":
            txt_edit_M.insert(END, f"\nСерия обработана без ошибок.\nВсего в серии: {len(dictReportsPacks)}\nБрака: {len(dictTaskPacksM) - len(dictReportsPacks)}")
            TextReportM = CreateMainReportM(dictTaskPacksM)
        if dublesTasks != "":
            txt_edit_M.insert(END, "Дубли пачек в задании:\n" + dublesTasks)
            btn_save_M["state"] = "disabled"
        if dublesBoxs != "":
            txt_edit_M.insert(END, "Дубли коробов в задании:\n" + dublesBoxs)
            btn_save_M["state"] = "disabled"
        if dublesPacks != "":
            txt_edit_M.insert(END, "Дубли пачек:\n" + dublesPacks)
            btn_save_M["state"] = "disabled"
        if otherErrors != "":
            txt_edit_M.insert(END, "Прочие ошибки:\n" + otherErrors)
            btn_save_M["state"] = "disabled"
    else:
        txt_edit_M.insert(END, "Не хватает текста какого/их-то отчёта/ов...")
        btn_save_M["state"] = "disabled"

#Выполняет поиск ошибок
def executeS():
    global TextReportS
    TextReportS = ""
    btn_save_S["state"] = "normal"
    btn_exe_S["state"] = "disable"
    if (len(listTasksS) and len(listReportsS)) != 0:
        # Создание словаря и проверка пачек на дубли из задания Сериализации
        dictTaskPacksS = dict()
        dublesTasks = ""
        for task in listTasksS:
            for packs in task["productNumbers"]:
                pack = packs[4:17]
                if dictTaskPacksS.get(pack, None):
                    dublesTasks += f"{pack} в задании уже есть\n"
                else:
                    dictTaskPacksS[pack] = 1
        #Проверка пачек на дубли и принадлежность их заданию
        dictReportsPacks = dict()
        dictBoxs = dict()
        dublesPacks = ""
        dublesBoxs = ""
        otherErrors = ""
        countSample = 0
        for report in listReportsS:
            #Агрегация
            for box in report['readyBox']:
                if dictBoxs.get(box['boxNumber'], None):
                    dublesBoxs += f"{box['boxNumber']} - такой короб уже есть в {report['id']} и {dictBoxs[box['boxNumber']]}\n"
                else:
                    dictBoxs[box['boxNumber']] = report['id']
                    for pack in box['contentNumbers']:
                        if dictTaskPacksS.get(pack, None):
                            if dictReportsPacks.get(pack, None):
                                dublesPacks += f"{pack} в коробах {dictReportsPacks[pack]} и {box['boxNumber']}\n"
                            else:
                                dictReportsPacks[pack] = box['boxNumber']
                        else:
                            otherErrors += f"{pack} в коробе {box['boxNumber']} отсутствует в тексте задания\n"
            #Отбор
            for pack in report['sampleNumbers']:
                countSample += 1
                if dictTaskPacksS.get(pack['number'], None):
                    if dictReportsPacks.get(pack['number'], None):
                        dublesPacks += f"{pack['number']} в {dictReportsPacks[pack['number']]} и отборе\n"
                    else:
                        dictReportsPacks[pack['number']] = 'отборе'
        #Вывод текста ошибок
        if dublesTasks == "" and dublesPacks == "" and otherErrors == "" and dublesBoxs == "":
            txt_edit_S.insert(END, f"\nСерия обработана без ошибок.\nВсего в серии: {len(dictReportsPacks) - countSample}\n"
                                   f"Отбор: {countSample}\n"
                                   f"Брака: {len(dictTaskPacksS) - len(dictReportsPacks)}")
            TextReportS = CreateMainReportS(dictTaskPacksS)
        if dublesTasks != "":
            txt_edit_S.insert(END, "Дубли пачек в задании:\n" + dublesTasks)
            btn_save_S["state"] = "disabled"
        if dublesBoxs != "":
            txt_edit_S.insert(END, "Дубли коробов в задании:\n" + dublesBoxs)
            btn_save_S["state"] = "disabled"
        if dublesPacks != "":
            txt_edit_S.insert(END, "Дубли пачек:\n" + dublesPacks)
            btn_save_S["state"] = "disabled"
        if otherErrors != "":
            txt_edit_S.insert(END, "Прочие ошибки:\n" + otherErrors)
            btn_save_S["state"] = "disabled"

    else:
        txt_edit_S.insert(END, "Не хватает текста какого/их-то отчёта/ов...")
        btn_save_S["state"] = "disabled"

#Создание главного отчета Сериализации Линии M
def CreateMainReportM(dtpM):
    answerM = dict()
    answerM['id'] = listSerReportsM[0]['id']
    answerM['startTime'] = listSerReportsM[0]['startTime']
    answerM['endTime'] = listSerReportsM[0]['endTime']
    answerM['sampleNumbers'] = listSerReportsM[0]['sampleNumbers']
    answerM['operators'] = listSerReportsM[0]['operators']
    answerM['readyBox'] = listSerReportsM[0]['readyBox']
    answerM['defectiveCodes'] = list()
    answerM['emptyNumbers'] = list()
    for report in listReportsM:
        for box in report["readyBox"]:
            for pack in box["productNumbers"]:
                if dtpM[pack] == 1:
                    answerM['emptyNumbers'].append(pack)
                    del dtpM[pack]
    for pack in dtpM:
        answerM['defectiveCodes'].append({"number": pack, "defectCode" : "1"})
    return json.dumps(answerM, indent=4, ensure_ascii=False)

#Создание главного отчета Сериализации/Агрегации Линии S
def CreateMainReportS(dtpS):
    answerS = dict()
    answerS['id'] = listReportsS[0]['id']
    answerS['startTime'] = listReportsS[0]['startTime']
    answerS['endTime'] = listReportsS[0]['endTime']
    answerS['serializedOnly'] = list()
    answerS['readyBox'] = list()                #Из-за нескольких отчетов нужно объединить короба
    answerS['defectiveCodes'] = list()
    answerS['sampleNumbers'] = list()           #Из-за нескольких отчетов нужно объединить отборы
    answerS['emptyNumbers'] = list()
    for report in listReportsS:
        for box in report['readyBox']:
            answerS['readyBox'].append(box)
            for pack in box['contentNumbers']:
                if dtpS.get(pack, None):
                    del dtpS[pack]
        for pack in report['sampleNumbers']:
            answerS['sampleNumbers'].append(pack)
            if dtpS.get(pack['number'], None):
                del dtpS[pack['number']]
    for pack in dtpS:
        answerS['defectiveCodes'].append({"number": pack, "defectCode": "1"})
    return json.dumps(answerS, indent=4, ensure_ascii=False)

#Сохранение общего текста отчёта линии M
def saveM():
    answerFile = open(pathM + "/Общий отчет.txt", "w")
    answerFile.write(TextReportM)
    answerFile.close()
    #Отрисовка текстового поля Отчёта
    subWindow = Toplevel(window)
    subWindow.title("Текст общего отчета")
    subWindow.geometry('668x392+600+120')
    subWindow.wm_maxsize(width=668, height=392)
    subWindow.wm_minsize(width=668, height=392)
    TextReportFrame = Text(subWindow)
    TextReportFrame.grid(row=0, column=0, padx=2, pady=2)
    scrollbarReport = Scrollbar(subWindow, command=TextReportFrame.yview)
    scrollbarReport.grid(row=0, column=1, sticky='nsew')
    TextReportFrame['yscrollcommand'] = scrollbarReport.set
    TextReportFrame.insert(END, TextReportM)

#Сохранение общего текста отчёта линии S
def saveS():
    answerFile = open(pathS + "/Общий отчет.txt", "w")
    answerFile.write(TextReportS)
    answerFile.close()
    # Отрисовка текстового поля Отчёта
    subWindow = Toplevel(window)
    subWindow.title("Текст общего отчета")
    subWindow.geometry('668x392+600+120')
    subWindow.wm_maxsize(width=668, height=392)
    subWindow.wm_minsize(width=668, height=392)
    TextReportFrame = Text(subWindow)
    TextReportFrame.grid(row=0, column=0, padx=2, pady=2)
    scrollbarReport = Scrollbar(subWindow, command=TextReportFrame.yview)
    scrollbarReport.grid(row=0, column=1, sticky='nsew')
    TextReportFrame['yscrollcommand'] = scrollbarReport.set
    TextReportFrame.insert(END, TextReportS)

pathS = ""
listTasksS = list()
listReportsS = list()
TextReportS = ""
pathM = ""
listTasksM = list()
listSerReportsM = list()
listReportsM = list()
TextReportM = ""
window = Tk()
window.title("BrakFounderPy")
window.geometry('1100x400+100+100')
window.minsize(width=400, height=250)
tab_control = ttk.Notebook(window)
tabM = ttk.Frame(tab_control)
tabS = ttk.Frame(tab_control)
tab_control.add(tabM, text='Линия M')
tab_control.add(tabS, text='Линия S')
tab_control.pack(expand=1, fill='both')
# Вкладка линии M
tabM.rowconfigure(0, minsize=10, weight=1)
tabM.columnconfigure(1, minsize=10, weight=1)
txt_edit_M = Text(tabM)
fr_buttons_M = Frame(tabM)
btn_open_M = Button(fr_buttons_M, text="Открыть", command=open_file_M)
btn_exe_M = Button(fr_buttons_M, text="Обработать", command=executeM)
btn_save_M = Button(fr_buttons_M, text="Сохранить как...", command=saveM)
btn_open_M.grid(row=0, column=0, sticky="ew", padx=5, pady=2)
btn_exe_M.grid(row=1, column=0, sticky="ew", padx=5)
btn_save_M.grid(row=2, column=0, sticky="ew", padx=5, pady=2)
fr_buttons_M.grid(row=0, column=0, sticky="ns")
txt_edit_M.grid(row=0, column=1, sticky="nsew")
scrollReportM = Scrollbar(tabM, command=txt_edit_M.yview)
scrollReportM.grid(row=0, column=2, sticky='nsew')
txt_edit_M['yscrollcommand'] = scrollReportM.set
btn_exe_M["state"] = "disabled"
btn_save_M["state"] = "disabled"
# Вкладка Линии S
tabS.rowconfigure(0, minsize=10, weight=1)
tabS.columnconfigure(1, minsize=10, weight=1)
txt_edit_S = Text(tabS)
fr_buttons_S = Frame(tabS)
btn_open_S = Button(fr_buttons_S, text="Открыть", command=open_file_S)
btn_exe_S = Button(fr_buttons_S, text="Обработать", command=executeS)
btn_save_S = Button(fr_buttons_S, text="Сохранить как...", command=saveS)
btn_open_S.grid(row=0, column=0, sticky="ew", padx=5, pady=2)
btn_exe_S.grid(row=1, column=0, sticky="ew", padx=5)
btn_save_S.grid(row=2, column=0, sticky="ew", padx=5, pady=2)
fr_buttons_S.grid(row=0, column=0, sticky="ns")
txt_edit_S.grid(row=0, column=1, sticky="nsew")
scrollReportS = Scrollbar(tabS, command=txt_edit_S.yview)
scrollReportS.grid(row=0, column=2, sticky='nsew')
txt_edit_S['yscrollcommand'] = scrollReportS.set
btn_exe_S["state"] = "disabled"
btn_save_S["state"] = "disabled"

window.mainloop()