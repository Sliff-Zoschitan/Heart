from tkinter import *
from PIL import Image, ImageTk

def raise_frame(frame):
    frame.tkraise()
def che(check1, check2,check3):
    check1.grid(row=0, column=1)
    check2.grid(row=1, column=1)
    check3.grid(row=2, column=1)

win1 = Tk()
win1.resizable(width = False, height = False)
win1.geometry("1280x720+125+50")
win1.title("Heart")
win1.iconbitmap('icon.ico')

f1 = Frame(win1)
f2 = Frame(win1)
f3 = Frame(win1)
f4 = Frame(win1)
f1['bg'] = '#f6e5eb'
f2['bg'] = '#f6e5eb'
f3['bg'] = '#f6e5eb'
f4['bg'] = '#f6e5eb'
f1.grid(row=0, column=0, sticky='news')
f2.grid(row=0, column=0, sticky='news')
f3.grid(row=0, column=0, sticky='news')
f4.grid(row=0, column=0, sticky='news')
win1.grid_columnconfigure(0, minsize=1280)
win1.grid_rowconfigure(0, minsize=720)


imageBtnInfo_patient = PhotoImage(file = 'Images/Info_patient.png')
imageBtnNew_patient = PhotoImage(file = 'Images/New_patient.png')
imageLogo = PhotoImage(file = 'Images/Logo.png')
imageLogo2 = PhotoImage(file = 'Images/Logo2.png')
imageBtnFill_data = PhotoImage(file = 'Images/Fill_data.png')
imageBtnPerson_data = PhotoImage(file = 'Images/Person_data.png')
imageBtnFamily_data = PhotoImage(file = 'Images/Family_data.png')
imageBtnLocal_data = PhotoImage(file = 'Images/Local_data.png')
imageCheck_mark = PhotoImage(file = 'Images/Check_mark.png')
imageBtnForecast = PhotoImage(file = 'Images/Forecast.png')
imageBtnBack = PhotoImage(file = 'Images/Back.png')
imageBtnInfo = PhotoImage(file = 'Images/Info.png')
imageBtnMenu = PhotoImage(file = 'Images/Menu.png')
imageBtnSave = PhotoImage(file = 'Images/Save.png')
############1
logo_title1 = Frame(f1)
logo_title1['bg'] = '#f6e5eb'
logo_title1.pack(side=TOP, pady=70)
Logo1 = Label (logo_title1,
              height=119,
              width=117,
              bg = '#f6e5eb',
              image = imageLogo).grid(row=0, column=0)
title1 = Label(logo_title1,
              text='HeartCare',
              bg = '#f6e5eb',
              font = 'BankGothic 30',
              fg = '#cf3d3d').grid(row=0, column=1)
BtnInfo_patient = Button(f1,
              text="Информация о пациенте",
              height = 65,
              width = 363,
              image = imageBtnInfo_patient,
              borderwidth = 0,
              bg = '#f6e5eb',
              command=lambda:raise_frame(f2)).pack(side=LEFT, pady=0, padx=90)
BtnNew_patient = Button(f1,
              text="Новый пациент",
              height=65,
              width=363,
              image = imageBtnNew_patient,
              borderwidth = 0,
              bg = '#f6e5eb').pack(side=RIGHT, pady=0, padx=90)

############2
logo_title2 = Frame(f2)
logo_title2['bg'] = '#f6e5eb'
logo_title2.place(x=20, y=10)
Logo2 = Label(logo_title2,
              height=47,
              width=45,
              bg = '#f6e5eb',
              image = imageLogo2).grid(row=0, column=0)
title2 = Label(logo_title2,
              text='Информация о пациенте',
              bg = '#f6e5eb',
              font = 'GothicCentury 19',
              fg = '#cf3d3d').grid(row=0, column=1)
inputFr = Frame(f2)
inputFr['bg'] = '#f6e5eb'
inputFr.place(x=25, y=100)
inputFr.grid_columnconfigure(1, minsize=300)
fiolb = Label(inputFr,
              text='ФИО',
              font='GothicCentury 20',
              bg = '#f6e5eb',
              fg='#cf3d3d').grid(row=0, column=0)
fio = Entry(inputFr,
            font='GothicCentury 18',
            width=30).grid(row=1, column=0)
datelb = Label(inputFr,
              text='Дата рождения',
              font='GothicCentury 20',
              bg = '#f6e5eb',
              fg='#cf3d3d').grid(row=0, column=1)
date = Entry(inputFr,
            font='GothicCentury 18',
            width=10,
            ).grid(row=1, column=1)

BtnFill_data = Button(inputFr,
              text="Заполнить данные",
              height=42,
              width=187,
              image = imageBtnFill_data,
              borderwidth = 0,
              bg = '#f6e5eb',
              command=lambda:che(CheckPerson_data,CheckFamily_data,CheckLocal_data)).grid(row=1, column=2)
blocks = Frame(f2)
blocks['bg'] = '#f6e5eb'
blocks.pack(side=LEFT)
blocks.grid_columnconfigure(0, minsize=350)
blocks.grid_rowconfigure(0, minsize=90)
blocks.grid_rowconfigure(1, minsize=90)
blocks.grid_rowconfigure(2, minsize=90)
BtnPerson_data = Button(blocks,
              text="Персональные данные",
              height=50,
              width=303,
              image = imageBtnPerson_data,
              borderwidth = 0,
              bg = '#f6e5eb').grid(row=0, column=0)
BtnFamily_data = Button(blocks,
              text="Семейное положение",
              height=50,
              width=303,
              image = imageBtnFamily_data,
              borderwidth = 0,
              bg = '#f6e5eb').grid(row=1, column=0)
BtnLocal_data = Button(blocks,
              text="Район проживания",
              height=50,
              width=303,
              image = imageBtnLocal_data,
              borderwidth = 0,
              bg = '#f6e5eb').grid(row=2, column=0)
CheckPerson_data = Label(blocks,
              height=27,
              width=24,
              image = imageCheck_mark,
              borderwidth = 0,
              bg = '#f6e5eb')
CheckFamily_data = Label(blocks,
              height=27,
              width=24,
              image = imageCheck_mark,
              borderwidth = 0,
              bg = '#f6e5eb')
CheckLocal_data = Label(blocks,
              height=27,
              width=24,
              image = imageCheck_mark,
              borderwidth = 0,
              bg = '#f6e5eb')

BtnForecast = Button(f2,
              text="Прогноз",
              height=50,
              width=303,
              image = imageBtnForecast,
              borderwidth = 0,
              bg = '#f6e5eb',
              command=lambda:raise_frame(f3)).place(x=488,y=620)
BtnBack1 = Button(f2,
                 image=imageBtnBack,
                 borderwidth = 0,
                 bg = '#f6e5eb',
                 command=lambda:raise_frame(f1)).place(x=50,y=620)
##################3
logo_title3 = Frame(f3)
logo_title3['bg'] = '#f6e5eb'
logo_title3.place(x=20, y=10)
Logo3 = Label(logo_title3,
              height=47,
              width=45,
              bg = '#f6e5eb',
              image = imageLogo2).grid(row=0, column=0)
title3 = Label(logo_title3,
              text='Данные прогнозирования',
              bg = '#f6e5eb',
              font = 'GothicCentury 19',
              fg = '#cf3d3d').grid(row=0, column=1)
BtnBack2 = Button(f3,
                 image=imageBtnBack,
                 borderwidth = 0,
                 bg = '#f6e5eb',
                 command=lambda:raise_frame(f2)).place(x=50,y=620)
Bolezni = Label(f3,
                text='Вероятность развития болезней\n\n'
                     +'1.Артериальная гипертензия\n'
                     +'2.Ишемическая болезнь сердца\n'
                     +'3.Инфаркт миокарда\n'
                     +'4.ОНМК\n'
                     +'5.Сердечная недостаточность\n',
                justify = LEFT,
                bg='#f6e5eb',
                font='GothicCentury 19',
                fg='#cf3d3d').place(x=50,y=150)
Infos = Frame(f3)
Infos['bg'] = '#f6e5eb'
Infos.place(x=450, y=213)
Infos.grid_rowconfigure(0, minsize=28)
Infos.grid_rowconfigure(1, minsize=28)
Infos.grid_rowconfigure(2, minsize=28)
Infos.grid_rowconfigure(3, minsize=28)
Infos.grid_rowconfigure(4, minsize=28)
Infos.grid_columnconfigure(0, minsize=28)
Infos.grid_columnconfigure(1, minsize=28)
LbInf1 = Label(Infos,
                 text='%75',
                 borderwidth = 0,
                 font='GothicCentury 15',
                 bg = '#f6e5eb',
               fg='#cf3d3d').grid(row=0, column=0)
LbInf2 = Label(Infos,
                 text='%63',
                 borderwidth = 0,
                 font='GothicCentury 15',
                 bg = '#f6e5eb',
               fg='#cf3d3d').grid(row=1, column=0)
LbInf3 = Label(Infos,
                 text='%30',
                 borderwidth = 0,
                 font='GothicCentury 15',
                 bg = '#f6e5eb',
               fg='#cf3d3d').grid(row=2, column=0)
LbInf4 = Label(Infos,
                 text='%25',
                 borderwidth = 0,
                 font='GothicCentury 15',
                 bg = '#f6e5eb',
               fg='#cf3d3d').grid(row=3, column=0)
LbInf5 = Label(Infos,
                 text='%15',
                 borderwidth = 0,
                 font='GothicCentury 15',
                 bg = '#f6e5eb',
               fg='#cf3d3d').grid(row=4, column=0)
BtnInf1 = Button(Infos,
                 image=imageBtnInfo,
                 borderwidth = 0,
                 height=19,
                 width=113,
                 bg = '#f6e5eb').grid(row=0, column=1)
BtnInf2 = Button(Infos,
                 image=imageBtnInfo,
                 borderwidth = 0,
                 height=19,
                 width=113,
                 bg = '#f6e5eb').grid(row=1, column=1)
BtnInf3 = Button(Infos,
                 image=imageBtnInfo,
                 borderwidth = 0,
                 height=19,
                 width=113,
                 bg = '#f6e5eb').grid(row=2, column=1)
BtnInf4 = Button(Infos,
                 image=imageBtnInfo,
                 borderwidth = 0,
                 height=19,
                 width=113,
                 bg = '#f6e5eb').grid(row=3, column=1)
BtnInf5 = Button(Infos,
                 image=imageBtnInfo,
                 borderwidth = 0,
                 height=19,
                 width=113,
                 bg = '#f6e5eb').grid(row=4, column=1)

Factors = Label(f3,
                text='Основные факторы\n\n'
                     +'1.Сахарный диабет\n'
                     +'2.Повышеный уровень холестерина\n'
                     +'3.Курение\n\n'
                     +'Дополнительные факторы\n\n'
                     +'1.Вредные условия труда\n'
                     +'2.Отсутствие высшего образования\n'
                     +'3.Плохая ифроструктура района\n',
                justify = LEFT,
                bg='#f6e5eb',
                font='GothicCentury 19',
                fg='#cf3d3d').place(x=700,y=150)
BtnSave = Button(f3,
              text="В меню",
              height=46,
              width=289,
              image = imageBtnSave,
              borderwidth = 0,
              bg = '#f6e5eb').place(x=450,y=620)
BtnMenu = Button(f3,
              text="Сохранить",
              height=46,
              width=289,
              image = imageBtnMenu,
              borderwidth = 0,
              bg = '#f6e5eb',
              command=lambda:raise_frame(f1)).place(x=950,y=620)

raise_frame(f1)
win1.mainloop()

