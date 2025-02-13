import tkinter

window=tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=700, height=300)
labelText= "I am a Label"
label1=tkinter.Label(text=labelText)
input=tkinter.Entry()

def on_btn_click():
    labelText2= "Button Clinked"
    #label1.config(text=labelText2)
    #OR
    label1["text"] = input.get()

btn= tkinter.Button(text="Click Me",command=on_btn_click)


#Pack Layout Manager
#pack : stack one after another, in the order of pack
#label1.pack()
#input.pack()
#btn.pack()

#pack : stack one after another, in the order of pack. Left to Right
#label1.pack(side=tkinter.LEFT)
#input.pack(side=tkinter.LEFT)
#btn.pack(side=tkinter.LEFT)

#Place Layout Manager at specific position
#label1.place(relx=0.5, rely=0.1)

#Grid Layout Manger. Can not be used with Pack manager
btn2=tkinter.Button(text="Click Me")
label1.grid(row=0, column=0)
input.grid(row=3, column=3)
btn.grid(row=1, column=1)
btn2.grid(row=0, column=2)


window.mainloop()