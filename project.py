from tkinter import*
root = Tk()
root.geometry("500x300")


def getvals():
    print("Accepted...")
    

#Heading
Label(root, text = "REGISTRATION FORM",font="ar 15 bold").grid(row=0,column=3)

#Fields
name = Label(root,text = "NAME")
surname = Label(root,text = "SURNAME")
gender = Label(root,text = "GENDER")
phone = Label(root,text = "PHONE")

#Packing Fields
name.grid(row=1,column = 0)
surname.grid(row=2,column = 0)
gender.grid(row=3,column = 0)
phone.grid(row=4,column = 0)

#Variable Storage of Data
nameValue = StringVar
surnameValue = StringVar
genderValue = StringVar
phoneValue = StringVar
checkvalue = IntVar

#Creating Entry Field and Packing
nameentry = Entry(root, textvariable= nameValue).grid(row=1,column=3)
surnameentry = Entry(root, textvariable=surnameValue).grid(row=2,column=3)
genderentry = Entry(root, textvariable=genderValue).grid(row=3,column=3)
phoneentry = Entry(root, textvariable=phoneValue).grid(row=4,column=3)

#Creating checkbox 
checkbtn = Checkbutton(text="REMEMBER ME?", variable=checkvalue).grid(row=5,column=3)

#Submit button
Button(text="SUBMIT", command=getvals).grid(row=6,column=3)

root.mainloop()

