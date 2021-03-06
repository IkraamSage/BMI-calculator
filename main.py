# importing tkinter
from tkinter import *
from tkinter import messagebox
# GUI size and headers
root = Tk()
root.title("BMI Calculator")
root.geometry("750x660")
root.config(bg="blue")
header = Label(root, text='IDEAL BODY MASS INDEX CALCULATOR', fg='black')
header.place(x=250, y=20)
# GUI frame placement and size
frame = Frame(root, width=400, height=200, relief='raised', bg='white')
frame.place(x=190, y=80)
# weight label and entry
weight = Label(frame, text="Weight in kilograms:", bg='red', fg='black')
weight.place(x=20, y=20)
weight_entry = Entry(frame)
weight_entry.place(x=180, y=20)
# height label and entry
height = Label(frame, text="Height in centimeters:", bg='red', fg='black')
height.place(x=20, y=60)
height_entry = Entry(frame)
height_entry.place(x=180, y=60)
# gender entry and placement
gender = Label(frame, text="Gender:", bg='red', fg='black')
gender.place(x=100, y=100)
# age entry and placement
age = Label(frame, text="Age:", bg='red', fg='black')
age.place(x=120, y=160)
age_entry = Entry(frame, state='readonly')
age_entry.place(x=180, y=160)
# setting variable option for male and female selection
options = ['Select...', 'Male', "Female"]
variable = StringVar(frame)
variable.set(options[0])

# defining the value
def activate(value):
    variable.set(value)
    if value != "Select...":
        age_entry.config(state='normal')
    else:
        age_entry.config(state='readonly')

# gender menu placement
gender = OptionMenu(frame, variable, *options, command=activate)
gender.place(x=180,  y=100)

# BMI calculation entry and results
def bmi_calc():
    try:
        float(weight_entry.get())
        float(height_entry.get())
        float(age_entry.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + (
                        0.03 * float(age_entry.get())) + 11
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        if result_bmi < 18.5:
            category.config(text='Underweight')
        elif 18.5 <= result_bmi < 25:
            category.config(text='Healthy')
        elif 25 <= result_bmi < 30:
            category.config(text='Overweight')
        elif result_bmi >= 30:
            category.config(text='Obese')

    except ValueError:
        messagebox.showerror(title=None, message='Gender was not specified or invalid entry was given')
        delete()

# button for ideal body mass index
calculate = Button(root, text="Calculate your Ideal Body Mass Index", width=50, command=bmi_calc)
calculate.place(x=180, y=300)
# making the size and placement of button
bmi = Label(root, text="BMI:", bg='#333', fg="white")
bmi.place(rely=0.55, relx=0.1)
bmi_field = Entry(root, state='readonly')
bmi_field.place(rely=0.55, relx=0.2)
ideal_bmi = Label(root, text='Ideal BMI:', bg='#333', fg="white")
ideal_bmi.place(rely=0.55, relx=0.5)
ideal_field = Entry(root, state='readonly')
ideal_field.place(rely=0.55, relx=0.65)

#defining the delete button
def delete():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.config(state='normal')
    bmi_field.config(state='normal')
    ideal_field.config(state='normal')
    age_entry.delete(0, END)
    bmi_field.delete(0, END)
    ideal_field.delete(0, END)
    age_entry.config(state='readonly')
    bmi_field.config(state='readonly')
    ideal_field.config(state='readonly')
    weight_entry.focus()
    variable.set(options[0])
    category.config(text='')


category_head = Label(root, text="Category:", bg='#333', fg='white')
category = Label(root, width=20, bg='#222', fg='white')
category.place(relx=0.38, rely=0.72)
category_head.place(relx=0.45, rely=0.67)
clear = Button(root, text='Clear', command=delete)
clear.place(rely=0.85, relx=0.1)
quit = Button(root, text='Exit', command='exit')
quit.place(rely=0.85, relx=0.83)
root.mainloop()