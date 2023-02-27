from tkinter import *

def calculate():
    temp = int(entry.get())
    new_temp = 9/5*temp+32
    output_label.configure(text = 'Converted: {:.1f}'.format(new_temp))
    #entry.delete(0,END)

root = Tk()
message_label = Label(text='Enter a temperature', font=('Courier New', 13, 'bold'), fg='black')
answer_label = Label(text='Answer :',font=('Courier New', 13, 'bold')) 
output_label = Label(font=('Courier New', 13, 'bold'))
entry = Entry(font=('Courier New', 13, 'bold'), width=15)
calc_button = Button(text='OK', font=('Courier New', 13, 'bold'), command=calculate, width=6, height=0, bg='black', fg='white')

message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
answer_label.grid(row=2, column=0)
output_label.grid(row=2, column=1)

mainloop()
