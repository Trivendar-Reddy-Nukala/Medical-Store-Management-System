import pandas as pd
import os
from datetime import datetime 
import matplotlib.pyplot as plt
import tkinter as tk

root = tk.Tk()
root.title("Medical Store Management & Data Management System")
f1=tk.Frame(master=root , background="lightgrey",width=300, height=300)
f2=tk.Frame(master=root , background="lightgrey",width=300, height=300)
f3=tk.Frame(master=root , background="lightgrey",width=300, height=300)
f4=tk.Frame(master=root , background="lightgrey",width=300, height=300)
f1.grid_propagate(False)
f2.grid_propagate(False)
f3.grid_propagate(False)
f4.grid_propagate(False)

def show_frame(frame):
    for f in (f2, f3, f4):
        try:
            f.destroy()
        except:
            pass
    frame = tk.Frame(master=root , background="lightgrey",width=300, height=300)
    frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


selected_operation = tk.IntVar()

def Addmedicine() :
    # show_frame(f2)
    global f2
    f2 = tk.Frame(master=root , background="lightgrey",width=300, height=300)
    f2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    f3.destroy()
    f4.destroy()
    def Save_to_File():
        nonlocal Medname, Medprice, Medrow, Medcol
        name = Medname.get()
        price = Medprice.get()
        row = Medrow.get()
        col = Medcol.get()
        with open("File1.txt", "a") as file:
            file.write(f"{name}\t{price}\t{row}\t{col}\n")
    m1=tk.Label(f2, text="Medicine Name")
    Medname=tk.Entry(f2)
    m2=tk.Label(f2, text="Medicine Price")
    Medprice=tk.Entry(f2) 
    m3=tk.Label(f2, text="Medicine Row")
    Medrow=tk.Entry(f2)
    m4=tk.Label(f2, text="Medicine Column")
    Medcol=tk.Entry(f2)

    m1.pack()
    Medname.pack(padx=5, pady=10)
    m2.pack()
    Medprice.pack(padx=5, pady=10)
    m3.pack()
    Medrow.pack(padx=5, pady=10)
    m4.pack()
    Medcol.pack(padx=5, pady=10)
    submit_button = tk.Button(f2, text="Submit", command=Save_to_File)
    submit_button.pack()
    

def Searchmedicine() :
    # show_frame(f3)
    global f3
    f3 = tk.Frame(master=root , background="lightgrey",width=300, height=300)
    f3.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    f2.destroy()
    f4.destroy()
    def Search_From_File():
        nonlocal Medname
        name = Medname.get()
        with open("File1.txt","r") as file:
            for line in file:
                info = line.strip().split("\t")
                if info[0]==name:
                    m5=tk.Label(f3, text=f"Name: {info[0]}, Price: {info[1]}, Row: {info[2]}, Column: {info[3]}").pack()
    
    m1=tk.Label(f3, text="Medicine Name")
    Medname=tk.Entry(f3)
    submit_button = tk.Button(f3, text="Submit", command=Search_From_File)


    m1.pack()
    Medname.pack(padx=5, pady=10)
    submit_button.pack()
                
daily_amount = 0 

def Billing():
    global daily_amount, f4
    f4 = tk.Frame(master=root , background="lightgrey",width=300, height=300)
    f4.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    f3.destroy()
    f2.destroy()
    amount = 0  

    Medname = tk.StringVar()
    Sheet = tk.StringVar()

    def Bill():
        global daily_amount 
        nonlocal amount
        name = Medname.get()
        sheet = Sheet.get()
        with open("File1.txt", "r") as file:
            for line in file:
                info = line.strip().split("\t")
                if info[0] == name:
                    amount += int(sheet) * int(info[1])
        daily_amount += amount

    def PrintBill():
        Bill()
        m6 = tk.Label(f4, text=f"Total Bill : {amount}")
        m6.pack()

    def callmed():
        nonlocal Medname, Sheet
        Medname_entry = tk.Entry(f4, textvariable=Medname)
        Sheet_entry = tk.Entry(f4, textvariable=Sheet)
        m1=tk.Label(f4, text="Medicine Name").pack()
        Medname_entry.pack(padx=5, pady=10)
        m1=tk.Label(f4, text="Number of sheets").pack()
        Sheet_entry.pack(padx=5, pady=10)
        plus_btn = tk.Button(f4, text='+', command=callmed).pack(padx=5, pady=10)
        submit_button = tk.Button(f4, text="Submit", command=PrintBill).pack()

    callmed()

   
def DataAnalysis() :
    data = pd.read_csv('DailyCollection.csv')
    # print(data)
    x = data['Date']
    y = data['Amount']
    # print(x,y)
    plt.plot(x, y, marker='.', color='red')
    plt.title('DATE VS COLLECTIONS')
    plt.xlabel('DATES')
    plt.ylabel('AMOUNT IN RUPEES')
    plt.show() 

def Save_Data():
    column_name = datetime.now().strftime("%Y-%m-%d")
    file_path = 'DailyCollection.csv'
    write_header = not os.path.exists(file_path) or os.stat(file_path).st_size == 0
    data_to_append = pd.Series([daily_amount], index=[column_name], name=datetime.now().date())
    with open(file_path, mode='a', newline='') as f:
        data_to_append.to_csv(f, header=write_header)
        exit

def1 = tk.Radiobutton(f1, text="Add New medicine", variable=selected_operation, value=1, command=Addmedicine)
def2 = tk.Radiobutton(f1, text="Search medicine", variable=selected_operation, value=2, command=Searchmedicine)
def3 = tk.Radiobutton(f1, text="Billing medicine", variable=selected_operation, value=3, command=Billing)
def4 = tk.Radiobutton(f1, text="Analysis", variable=selected_operation, value=4, command=DataAnalysis)
def5 = tk.Radiobutton(f1, text="Save Data", variable=selected_operation, value=5, command=Save_Data)

def1.pack(anchor=tk.W, padx=10, pady=5)
def2.pack(anchor=tk.W, padx=10, pady=5)
def3.pack(anchor=tk.W, padx=10, pady=5)
def4.pack(anchor=tk.W, padx=10, pady=5)
def5.pack(anchor=tk.W, padx=10, pady=5)

f1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
f2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
f3.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
f4.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
root.mainloop()