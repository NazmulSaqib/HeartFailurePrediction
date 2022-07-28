from lib2to3.pytree import LeafPattern
from sklearn.model_selection import train_test_split
import pandas as pd
from tkinter import *
from tkinter import ttk
import tkinter
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle
from PIL import ImageTk, Image
from tkinter import ttk
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
Heart = Label(shivam,text = "Welcome to Heart Failure prediction",fg="white",bg="sky blue",font=("Comicsansms",20,"bold")).place(x=20,y=200)
Enter = Label(shivam,text = "Enter The Details",font=("Comicsansms",15,"bold")).place(x=650,y=110)
# function for data Validation
def getInput():
    result = []
    # age Variable
    try:
       age1 = int(age.get())
       result.append(age1)
    except:
        return ErrorFunction("Age must be Interger")
    
    

    # sex Variabel
    sex_var1 = sex_var.get()
    if sex_var1 == "Sex":
        return ErrorFunction("Please Enter Sex")
    else:
        result.append(sex_var1)
    
    #chest pain Variabel
    chestPain1 = chestPain_var.get()
    if chestPain1 == "chestPain":
        return ErrorFunction("Please Enter Chest Pain type")
    else:
        result.append(chestPain1)
    
    # restingBp variable
    try:
        restingBP1 = int(restingBP.get())
        result.append(restingBP1)
    except:
        return ErrorFunction("Resting BP must be an Interger")
    

    # cholestrol variable
    try:
        cholestrol1 = int(cholestrol.get())
        result.append(cholestrol1)
    except:
        return ErrorFunction("Cholestrol must be an integer")

    # Fasting Blood sugar Variable
    fastingBs_var1 = fastingBs_var.get()
    if fastingBs_var1 == "blood sugar":
        return ErrorFunction("Please Enter Blood Sugar")
    else:
        if fastingBs_var1 == "<120":
           result.append(1)
        else:
           result.append(0)
    
    # Resting ECG Variable
    restingECG_var1 = restingECG_var.get()
    if restingECG_var1 == "Resting ECG":
        return ErrorFunction("Please Enter Resting ECG")
    else:
        result.append(restingECG_var1)

    # maxHr Variable
    try:
        maxHr1 = int(maxHr.get())
        result.append(maxHr1)
    except:
        return ErrorFunction("Heart Rate (maxHr) must be Integer")
    
    # exerciseAngina variable
    exerciseAngina_var1 = exerciseAngina.get()
    if exerciseAngina_var1 == 'Exercise Angina':
        return ErrorFunction("Please Enter Exercise Angina")
    else:
        result.append(exerciseAngina_var1)
    
    # old Peak Varialbe
    try:
        oldPeak1 = float(oldPeak.get())
        result.append(oldPeak1)
    except:
        return ErrorFunction("Old Peak must be an integer")

    # st slope variabel
    stSlope_var1 = stSlope.get()
    if stSlope_var1 == 'ST Slope':
        return ErrorFunction("Please Enter ST Slope")
    else:
        result.append(stSlope_var1)
    final_function(result)
#function for error handling
def ErrorFunction(str_var):
    new_popup = Toplevel(shivam)
    new_popup.geometry("700x150")
    new_popup.title("Error")
    Label(new_popup, text= str_var, font=('Comicsansms 18 bold'),fg="red").place(x=150,y=50)
# function for data standrization and prediction   
def final_function(my_list):
    dataFrame = pickle.load(open(r'new_data', 'rb'))
    dataFrame.loc[len(dataFrame.index)] = my_list
    # Data Encoding 
    le = LabelEncoder()
    dataFrame['Sex'] = le.fit_transform(dataFrame['Sex'])
    dataFrame['ChestPainType'] = le.fit_transform(dataFrame['ChestPainType'])
    dataFrame['RestingECG'] = le.fit_transform(dataFrame['RestingECG'])
    dataFrame['ExerciseAngina'] = le.fit_transform(dataFrame['ExerciseAngina'])
    dataFrame['ST_Slope'] = le.fit_transform(dataFrame['ST_Slope'])
    # Standarization on data
    sc = StandardScaler()
    dataFrame1 = sc.fit_transform(dataFrame)
    target_value = dataFrame1[-1]
    model = pickle.load(open(r"rf_model_99", 'rb'))
    predicted_value = model.predict([target_value])
    # for getting result on popup window
    global photo
    if predicted_value == 0:
        # pop_up("You Do Not have chances of Heart Failure")
        top = Toplevel(shivam)
        photo = PhotoImage(file="happy2.png")
        label= Label(top,image=photo)
        label.place(x=300, y=0)
        top.geometry("710x400")
        top.title("Heart Failure Prediction Result")
        Label(top, text="You Do Not have chances of Heart Failure" , font=('Comicsansms 18 bold'),fg="green").place(x=150,y= 200)
        Label(top,text="You don't need contact the doctor",font=('Comicsansms 10 bold')).place(x=270,y=250)
    else:
        # pop_up("You have chances of Heart Failure",fg="white",bg="red")
        top = Toplevel(shivam)
        photo = PhotoImage(file="Sad.png")
        label= Label(top,image=photo)
        label.place(x=250, y=0)
        top.geometry("710x400")
        top.title("Heart Failure Prediction Result")
        Label(top, text= "You have chances of Heart Failure" , font=('Comicsansms 18 bold'),fg="red").place(x=150,y= 200)
        Label(top,text="So contact doctor as soon as possible",font=('Comicsansms 10 bold')).place(x=220,y=250)
        
# function for pop up window
# def pop_up(value):
    # top = Toplevel(shivam)
    # top.geometry("750x270")
    # top.title("Heart Failure Prediction Result")
    # Label(top, text= value , font=('Mistral 18 bold')).place(x=150,y= 80)

#Menubutton

def open_popup():
    top=Toplevel(shivam)
    top.geometry("750x400")
    top.title("About information")
    Label(top,text = f'''nazmul saqib
    name nazmul saqib class b.tech fourth year 
    name nazmul saqib class b.tech fourth year
    shivam kumar
    name shivam kumar class b.tech fourth year
    name shivam kumar class b.tech fourth year
    shuja rashid
    name shuja rashid class b.tech fourth year
    name shuja rashid class b.tech fourth year  ''',font=('Comicsansms 12 bold')).place(x=5,y=2)
Label(shivam,font=('Helvetica 14 bold')).pack(pady=20)  

    
# def clear_entry():
#    age.delete(0, END)
#    sex_var.set("Sex")
#    chestPain_var.delete(0, END)
#    restingBP.delete(0, END)
#    cholestrol.delete(0, END)
#    fastingBs_var.delete(0, END)
#    restingECG_var.delete(0, END)
#    maxHr.delete(0, END)
#    exerciseAngina_var.delete(0, END)
#    oldPeak.delete(0, END)
#    stSlope_var.delete(0, END)

mymenu = Menu(shivam)
mymenu.add_command(label = "About",command=open_popup)
mymenu.add_command(label = "Exit",command=quit)
# mymenu.add_command(label = "Clear", command=all_clear)
shivam.config(menu=mymenu)



B = Button(shivam,text = "Submit",fg="white",bg="sky blue",font=("Comicsansms",12,"bold"), command=getInput).place(x=860,y=470)
# all Entry widgets 
age = Entry(shivam,bd=1,width=18, font=("Comicsansms",10,"bold"))
age.insert(0, 'Age')
age.bind('<FocusIn>')
age.place(x=540,y=170)

sex_var = tkinter.StringVar()
sex = ttk.Combobox(shivam, width=18, textvariable=sex_var,font=("Comicsansms",10,"bold"),)
sex['values'] = ['Sex', 'M', 'F']
sex.place(x=688, y=170)
sex.current(0)

chestPain_var = tkinter.StringVar()
chestPain = ttk.Combobox(shivam, width=18, textvariable=chestPain_var,font=("Comicsansms",10,"bold"),)
chestPain['values'] = ['chestPain', 'TA', 'ATA', 'NAP', 'ASY' ]
chestPain.place(x=849, y=170)
chestPain.current(0)

restingBP = Entry(shivam,width=18,font=("Comicsansms",10,"bold"),)
restingBP.insert(0, 'restingBP')
restingBP.bind('<FocusIn>')
restingBP.place(x=540, y=270)

cholestrol = Entry(shivam,width=18,font=("Comicsansms",10,"bold"),)
cholestrol.insert(0, 'Cholestrol')
cholestrol.bind('<FocusIn>')
cholestrol.place(x=690,y=270)

fastingBs_var = tkinter.StringVar()
fastingBs = ttk.Combobox(shivam, width=19, textvariable=fastingBs_var,font=("Comicsansms",10,"bold"),)
fastingBs['values'] = ['blood sugar', '<120', '>120' ]
fastingBs.place(x=840, y=270)
fastingBs.current(0)


restingECG_var = tkinter.StringVar()
restingECG = ttk.Combobox(shivam, width=16, textvariable=restingECG_var,font=("Comicsansms",10,"bold"),)
restingECG['values'] = ['Resting ECG', 'Normal', 'ST', 'LVH' ]
restingECG.place(x=540, y=370)
restingECG.current(0)

maxHr = Entry(shivam,width=18,font=("Comicsansms",10,"bold"),)
maxHr.insert(0, 'maxHr')
maxHr.bind('<FocusIn>')
maxHr.place(x=690,y=370)

exerciseAngina_var = tkinter.StringVar()
exerciseAngina = ttk.Combobox(shivam, width=19, textvariable=exerciseAngina_var,font=("Comicsansms",10,"bold"),)
exerciseAngina['values'] = ['Exercise Angina', 'Y', 'N' ]
exerciseAngina.place(x=840, y=370)
exerciseAngina.current(0)


oldPeak = Entry(shivam,width=18,font=("Comicsansms",10,"bold"),)
oldPeak.insert(0, 'Old Peak')
oldPeak.bind('<FocusIn>')
oldPeak.place(x=540,y=470)

stSlope_var = tkinter.StringVar()
stSlope = ttk.Combobox(shivam, width=18, textvariable=stSlope_var,font=("Comicsansms",10,"bold"),)
stSlope['values'] = ['ST Slope', 'Up', 'Flat', 'Down' ]
stSlope.place(x=690, y=470)
stSlope.current(0)

shivam.mainloop()
