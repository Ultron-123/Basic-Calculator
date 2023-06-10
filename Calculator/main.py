import tkinter as tk
import PIL 


root = tk.Tk()
root.geometry("700x550")
root.title("Calculator")
root.iconbitmap("Images/Calc.ico")
root.configure(bg="#cdfaf3")

Entry = tk.Entry(root,relief="sunken",bd=2,font=('Arial',18))
Entry.pack(fill="x",padx=30,pady=50)
Entry.insert(0,0)




global first_num
global second_num
global operation
global check # to delete the existing number on screen after cliking equal and again clicking a number
check = 0
operation="addition"
first_num=0
second_num=0

def Button_click(num):
    global check
    try:
        if check==1 or int(Entry.get())==0:
            Entry.delete(0 , tk.END)
            check = 0
    except:
        pass

    temp = Entry.get()
    Entry.delete(0 , tk.END)
    Entry.insert(0, str(temp) + str(num))


def Clear():
    Entry.delete(0 ,tk.END)
    Entry.insert(0 , 0)


def Back_Button():
    temp=Entry.get()
    Entry.delete(0, tk.END)
    Entry.insert(0 , temp[:-1])


def Decimal_Button():
    temp=Entry.get()
    Entry.delete(0, tk.END)

    index = temp.find('.')

    if index ==-1:
        Entry.insert(0 , temp + '.')
    else:
        Entry.insert(0 , temp + '')


def addition():
    global first_num 
    global operation
    operation = "addition"
    # to convert float to int if decimal part is 0 like 3.0
    if (float(Entry.get())%1==0):
        first_num=int(float(Entry.get()))
    else:
        first_num=float(Entry.get())

    Entry.delete(0, tk.END)


def subtraction():
    global first_num 
    global operation
    operation = "subtraction"
    if (float(Entry.get())%1==0):
        first_num=int(float(Entry.get()))
    else:
        first_num=float(Entry.get())

    Entry.delete(0, tk.END)


def multiplication():
    global first_num 
    global operation
    operation = "multiplication"
    if (float(Entry.get())%1==0):
        first_num=int(float(Entry.get()))
    else:
        first_num=float(Entry.get())

    Entry.delete(0, tk.END)


def division():
    global first_num 
    global operation
    operation = "division"
    if (float(Entry.get())%1==0):
        first_num=int(float(Entry.get()))
    else:
        first_num=float(Entry.get())

    Entry.delete(0, tk.END)


def equal():

    global first_num
    global second_num
    global check

    if (float(Entry.get())%1==0):
        second_num=int(float(Entry.get()))
    else:
        second_num=float(Entry.get())

    Entry.delete(0 , tk.END)
    
    if operation == "addition":
        check=1
        x = first_num + second_num
        if (float(x)%1==0):
            x = int(float(x))
        else:
            x = float(x)

        Entry.insert(0 , x)

    if operation == "subtraction":
        check=1
        x = first_num - second_num
        if (float(x)%1==0):
            x = int(float(x))
        else:
            x = float(x)

        Entry.insert(0 , x)

    if operation == "multiplication":
        check=1
        x = first_num * second_num
        if (float(x)%1==0):
            x = int(float(x))
        else:
            x = float(x)

        Entry.insert(0 , x)

    if operation == "division":
        check=1
        zerodiverror = 1 # for zeredivision error
        try:
            x = first_num % second_num
        except:
            x=0
            Entry.insert(0 , "Error")
            zerodiverror=0
            

        if(x==0 and zerodiverror):
            Entry.insert(0 , int(first_num / second_num) )

        elif(x!=0 and zerodiverror):
            Entry.insert(0 , first_num / second_num)

        








frame = tk.Frame(root,padx=30,pady=5,bg="#cdfaf3")

frame.columnconfigure(0,weight=1)
frame.columnconfigure(1,weight=1)
frame.columnconfigure(2,weight=1)
frame.columnconfigure(3,weight=2)

frame.rowconfigure(0,weight=1)
frame.rowconfigure(1,weight=1)
frame.rowconfigure(2,weight=1)
frame.rowconfigure(3,weight=1)


button_1 = tk.Button(frame, text = "1",font=('Arial',18),padx=10,pady=10 ,bg="white", command = lambda : Button_click(1))
button_2 = tk.Button(frame, text = "2",font=('Arial',18),padx=10,pady=10 ,bg="white", command = lambda : Button_click(2))
button_3 = tk.Button(frame, text = "3",font=('Arial',18),padx=10,pady=10 ,bg="white", command = lambda : Button_click(3))
button_4 = tk.Button(frame, text = "4",font=('Arial',18),padx=10,pady=10 ,bg="white", command = lambda : Button_click(4))
button_5 = tk.Button(frame, text = "5",font=('Arial',18),padx=10,pady=10 ,bg="white", command = lambda : Button_click(5))
button_6 = tk.Button(frame, text = "6",font=('Arial',18),padx=10,pady=10 ,bg="white", command = lambda : Button_click(6))
button_7 = tk.Button(frame, text = "7",font=('Arial',18),padx=10,pady=10 ,bg="white", command = lambda : Button_click(7))
button_8 = tk.Button(frame, text = "8",font=('Arial',18),padx=10,pady=10 ,bg="white", command = lambda : Button_click(8))
button_9 = tk.Button(frame, text = "9",font=('Arial',18),padx=10,pady=10 ,bg="white", command = lambda : Button_click(9))
button_0 = tk.Button(frame, text = "0",font=('Arial',18),padx=10,pady=10 ,bg="white", command = lambda : Button_click(0))
button_add = tk.Button(frame, text = "+",font=('Arial',18),padx=10,pady=10 , command = addition)
button_sub = tk.Button(frame, text = "-",font=('Arial',18),padx=10,pady=10 , command = subtraction)
button_mul = tk.Button(frame, text = "x",font=('Arial',18),padx=10,pady=10 , command = multiplication)
button_div = tk.Button(frame, text = "/",font=('Arial',18),padx=10,pady=10 , command = division)
button_eq = tk.Button(frame, text = "=",font=('Arial',18),padx=10,pady=10 ,bg="yellow", command = equal)
button_clear = tk.Button(frame, text = "C",font=('Arial',18),padx=10,pady=10 , command = Clear)
button_back = tk.Button(frame, text = "Back",font=('Arial',18),padx=10,pady=10 , command = Back_Button)
button_decimal = tk.Button(frame, text = ".",font=('Arial',18),padx=10,pady=10 ,bg="white", command = Decimal_Button)


button_clear.grid(row=0,column=0,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_back.grid(row=0,column=1,columnspan=2,sticky=tk.W + tk.E, padx=0.5,pady=0.5)
button_div.grid(row=0,column=3,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_7.grid(row=1,column=0,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_8.grid(row=1,column=1,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_9.grid(row=1,column=2,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_mul.grid(row=1,column=3,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_4.grid(row=2,column=0,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_5.grid(row=2,column=1,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_6.grid(row=2,column=2,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_sub.grid(row=2,column=3,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_1.grid(row=3,column=0,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_2.grid(row=3,column=1,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_3.grid(row=3,column=2,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_add.grid(row=3,column=3,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_0.grid(row=4,column=0,columnspan=2,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_decimal.grid(row=4,column=2,sticky=tk.W + tk.E , padx=0.5,pady=0.5)
button_eq.grid(row=4,column=3,sticky=tk.W + tk.E , padx=0.5,pady=0.5)







frame.pack(fill="both")



def click():
    label=tk.Label(root,text=Entry.get()).pack()

button = tk.Button(root,text="Click Here!", command = click)
button.pack()


















root.mainloop()