# Import Modules
from tkinter import *
from tkinter import messagebox

# Initializing the window
app = Tk()
app.geometry('700x550')
app.config(bg='#8dfeff')
app.title('Python')
app.resizable(0, 0)

# Sample contact list
contact_list = [
    {"Name": "John Smith", "Number": "555-1234", "Email": "john.smith@example.com"},
    {"Name": "Jane Doe", "Number": "20 7946 0958", "Email": "jane.doe@example.co.uk"},
    {"Name": "Akira Tanaka", "Number": "3-1234-5678", "Email": "akira.tanaka@example.jp"},
    {"Name": "Maria Garcia", "Number": "91 123 4567", "Email": "maria.garcia@example.es"},
    {"Name": "Chen Wei", "Number": "10 1234 5678", "Email": "chen.wei@example.cn"},
    {"Name": "Ahmed Khan", "Number": "4 123 4567", "Email": "ahmed.khan@example.ae"},
    {"Name": "Anna Müller", "Number": "30 123456", "Email": "anna.mueller@example.de"},
    {"Name": "Pierre Dubois", "Number": "1 23 45 67 89", "Email": "pierre.dubois@example.fr"},
    {"Name": "Svetlana Ivanova", "Number": "495 123-45-67", "Email": "svetlana.ivanova@example.ru"},
    {"Name": "Carlos Silva", "Number": "11 1234-5678", "Email": "carlos.silva@example.br"}
]

# Variables
Name = StringVar()
Number = StringVar()
Email = StringVar()

# Create frame
frame = Frame(app)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


# Function to get selected value
def selected():
    if len(select.curselection()) == 0:
        messagebox.showerror('Error', 'Please select a name')
    else:
        index = select.curselection()[0]
        contact = contact_list[index]
        Name.set(contact["Name"])
        Number.set(contact["Number"])
        Email.set(contact["Email"])


# Function to add new contact
def add_contact():
    if Name.get() != '' and Number.get() != '' and Email.get() != '':
        contact_list.append({"Name": Name.get(), "Number": Number.get(), "Email": Email.get()})
        update_listbox()
        messagebox.showinfo("Success", "Contact added successfully!")
        reset_form()
    else:
        messagebox.showwarning('Input Error', 'Please fill out the form')


# Function to edit existing contact
def edit_contact():
    if len(select.curselection()) == 0:
        messagebox.showerror('Error', 'Please select a contact to edit')
    else:
        index = select.curselection()[0]
        contact_list[index] = {"Name": Name.get(), "Number": Number.get(), "Email": Email.get()}
        update_listbox()
        messagebox.showinfo("Success", "Contact updated successfully!")
        reset_form()


# Function to delete contact
def delete_contact():
    if len(select.curselection()) == 0:
        messagebox.showerror('Error', 'Please select a contact to delete')
    else:
        index = select.curselection()[0]
        del contact_list[index]
        update_listbox()
        messagebox.showinfo("Success", "Contact deleted successfully!")
        reset_form()


# Function to view contact
def view_contact():
    selected()


# Function to update listbox
def update_listbox():
    select.delete(0, END)
    for contact in contact_list:
        select.insert(END, contact["Name"])


# Function to reset form
def reset_form():
    Name.set("")
    Number.set("")
    Email.set("")


# Function to exit application
def exit_app():
    app.destroy()


# Define labels and entry widgets
Label(app, text='Name', font=('Times new roman', 22, 'bold'), bg='SlateGray3').place(x=40, y=20)
Entry(app, textvariable=Name, width=30).place(x=200, y=30)

Label(app, text='Contact No.', font=('Times new roman', 20, 'bold'), bg='SlateGray3').place(x=40, y=70)
Entry(app, textvariable=Number, width=30).place(x=200, y=80)

Label(app, text='Email', font=('Times new roman', 20, 'bold'), bg='SlateGray3').place(x=40, y=120)
Entry(app, textvariable=Email, width=30).place(x=200, y=130)

# Define buttons
Button(app, text="Add", font='Helvetica 15 bold', bg='#e8c1c7', padx=20, command=add_contact).place(x=70, y=160)
Button(app, text="Edit", font='Helvetica 15 bold', bg='#e8c1c7', padx=20, command=edit_contact).place(x=70, y=220)
Button(app, text="Delete", font='Helvetica 15 bold', bg='#e8c1c7', padx=20, command=delete_contact).place(x=70, y=280)
Button(app, text="View", font='Helvetica 15 bold', bg='#e8c1c7', padx=20, command=view_contact).place(x=70, y=340)
Button(app, text="Reset", font='Helvetica 15 bold', bg='#e8c1c7', padx=20, command=reset_form).place(x=70, y=400)
Button(app, text="Exit", font='Helvetica 15 bold', bg='#e8c1c7', padx=20, command=exit_app).place(x=70, y=460)

# Initialize listbox with contacts
update_listbox()

app.mainloop()
