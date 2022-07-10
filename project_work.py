from sklearn.model_selection import train_test_split
import pandas as pd
from tkinter import *
from tkinter import ttk
import tkinter
from sklearn.preprocessing import StandardScaler
import pickle
shivam = Tk()

shivam.geometry("1200x500")
shivam.minsize(900,800)
shivam.maxsize(1000,900)

Canvas_width = 1000
canvas_height = 900
shivam.geometry(f"{Canvas_width}x{canvas_height}")
can_widget = Canvas(shivam,width=Canvas_width,height=canvas_height)
can_widget.pack

# to creat a rectangle specify parameter in this order-co-ordinates 
# of top left and co-ordinates of bottom right  
can_widget.create_rectangle(0,0,500,700,fill="sky blue")
can_widget.pack()
text = f'''Heart Failure Prediction is the machine learning based
application which is takes some patient details
and predict whether patient have chances of heart
failure or not on the basis of patient details  '''

para = Label(shivam,text = text,fg="white",bg="sky blue",font=("Comicsansms",13,"bold") ).place(x=30,y=250)
Heart = Label(shivam,text = "Welcome to Heart Failure pridiction",fg="white",bg="sky blue",font=("Comicsansms",20,"bold")).place(x=20,y=200)
Enter = Label(shivam,text = "Enter The Details",font=("Comicsansms",15,"bold")).place(x=650,y=110)
# A = Label(shivam,text = "1",font=("Comicsansms",12,"bold")).place(x=520,y=170)
# B = Label(shivam,text = "2",font=("Comicsansms",12,"bold")).place(x=675,y=170)
# C = Label(shivam,text = "3",font=("Comicsansms",12,"bold")).place(x=825,y=170)
# D = Label(shivam,text = "4",font=("Comicsansms",12,"bold")).place(x=520,y=270)
# E = Label(shivam,text = "5",font=("Comicsansms",12,"bold")).place(x=675,y=270)
# F = Label(shivam,text = "6",font=("Comicsansms",12,"bold")).place(x=825,y=270)
# G = Label(shivam,text = "7",font=("Comicsansms",12,"bold")).place(x=520,y=370)
# H = Label(shivam,text = "8",font=("Comicsansms",12,"bold")).place(x=675,y=370)
# I = Label(shivam,text = "9",font=("Comicsansms",12,"bold")).place(x=825,y=370)
# J = Label(shivam,text = "10",font=("Comicsansms",12,"bold")).place(x=520,y=470)
# K = Label(shivam,text = "11",font=("Comicsansms",12,"bold")).place(x=675,y=470)
def getInput():
    result = []
    # age Variable
    age1 = int(age.get())
    result.append(age1)

    # sex Variabel
    sex_var1 = sex_var.get()
    if sex_var1 == 'M':
        result.append(1)
    elif sex_var1 == 'F':
        result.append(0)
    
    #chest pain Variabel
    chestPain1 = chestPain_var.get()
    if chestPain1 == 'ATA':
        result.append(1)
    elif chestPain1 == 'NAP':
        result.append(2)
    elif chestPain1 == 'ASY':
        result.append(0)
    elif chestPain1 == 'TA':
        result.append(3)

    # restingBp variable
    restingBP1 = int(restingBP.get())
    result.append(restingBP1)

    # cholestrol variable
    cholestrol1 = int(cholestrol.get())
    result.append(cholestrol1)

    # Fasting Blood sugar Variable
    fastingBs_var1 = fastingBs_var.get()
    if fastingBs_var1 == "<120":
        result.append(1)
    else:
        result.append(0)
    
    # Resting ECG Variable
    restingECG_var1 = restingECG_var.get()
    if restingECG_var1 == 'Normal':
        result.append(1)
    elif restingECG_var1 == 'ST':
        result.append(2)
    elif restingECG_var1 == 'LVH':
        result.append(0)

    # maxHr Variable
    maxHr1 = int(maxHr.get())
    if 60< maxHr1 < 202:
        result.append(maxHr1)
    else:
        return 'Maximum Heart Rate Must Have Value in between 60 to 202 '
    
    # exerciseAngina variable
    exerciseAngina_var1 = exerciseAngina.get()
    if exerciseAngina_var1 == 'Y':
        result.append(1)
    else:
        result.append(0)
    
    # old Peak Varialbe
    oldPeak1 = float(oldPeak.get())
    result.append(oldPeak1)

    # st slope variabel
    stSlope_var1 = stSlope.get()
    if stSlope_var1 == 'Up':
        result.append(2)
    elif stSlope_var1 == 'Flat':
        result.append(1)
    elif stSlope == 'Down':
        result.append(0)
    print(result)
    # value prediction
    my_model = pickle.load(open(r"E:\my_projects\Hear_Failure_Prediction\rf_model_99", "rb"))
    print("my Results is:", my_model.predict([result]))
    print(result)



B = Button(shivam,text = "Submit",fg="white",bg="sky blue",font=("Comicsansms",12,"bold"), command=getInput).place(x=860,y=470)

age = Entry(shivam,bd=1,width=20)
age.insert(0, 'Age')
age.bind('<FocusIn>')
age.place(x=540,y=170)

sex_var = tkinter.StringVar()
sex = ttk.Combobox(shivam, width=20, textvariable=sex_var)
sex['values'] = ['Sex', 'M', 'F']
sex.place(x=690, y=170)
sex.current(0)

chestPain_var = tkinter.StringVar()
chestPain = ttk.Combobox(shivam, width=20, textvariable=chestPain_var)
chestPain['values'] = ['chestPain', 'TA', 'ATA', 'NAP', 'ASY' ]
chestPain.place(x=850, y=170)
chestPain.current(0)

restingBP = Entry(shivam,width=20)
restingBP.insert(0, 'restingBP')
restingBP.bind('<FocusIn>')
restingBP.place(x=540, y=270)

cholestrol = Entry(shivam,width=20)
cholestrol.insert(0, 'Cholestrol')
cholestrol.bind('<FocusIn>')
cholestrol.place(x=690,y=270)

fastingBs_var = tkinter.StringVar()
fastingBs = ttk.Combobox(shivam, width=20, textvariable=fastingBs_var)
fastingBs['values'] = ['blood sugar', '<120', '>120' ]
fastingBs.place(x=840, y=270)
fastingBs.current(0)


restingECG_var = tkinter.StringVar()
restingECG = ttk.Combobox(shivam, width=20, textvariable=restingECG_var)
restingECG['values'] = ['Resting ECG', 'Normal', 'ST', 'LVH' ]
restingECG.place(x=540, y=370)
restingECG.current(0)

maxHr = Entry(shivam,width=20)
maxHr.insert(0, 'maxHr')
maxHr.bind('<FocusIn>')
maxHr.place(x=690,y=370)

exerciseAngina_var = tkinter.StringVar()
exerciseAngina = ttk.Combobox(shivam, width=20, textvariable=exerciseAngina_var)
exerciseAngina['values'] = ['Exercise Angina', 'Y', 'N' ]
exerciseAngina.place(x=840, y=370)
exerciseAngina.current(0)


oldPeak = Entry(shivam,width=20)
oldPeak.insert(0, 'Old Peak')
oldPeak.bind('<FocusIn>')
oldPeak.place(x=540,y=470)

stSlope_var = tkinter.StringVar()
stSlope = ttk.Combobox(shivam, width=20, textvariable=stSlope_var)
stSlope['values'] = ['ST Slope', 'Up', 'Flat', 'Down' ]
stSlope.place(x=690, y=470)
stSlope.current(0)

shivam.mainloop()