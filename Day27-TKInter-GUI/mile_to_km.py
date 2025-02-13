from tkinter import Label,Button,Entry,Tk

window=Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)
miles_input= Entry()
miles_label=Label(text="Miles")
equal_label=Label(text="is equal to")
km_label=Label(text="Km")
km_result=Label(text="0")
km=0
calc_button= Button(text="Calculate")

def convert_miles_to_km():
    global km
    km = float(miles_input.get()) * 2.1
    km_result["text"]=str(km)

calc_button.config(command=convert_miles_to_km)

equal_label.grid(column=0,row=1)
miles_label.grid(column=2,row=0)
miles_input.grid(column=1,row=0)
km_result.grid(column=1,row=1)
km_label.grid(column=2,row=1)
calc_button.grid(column=1,row=3)







window.mainloop()