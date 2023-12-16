import auto_py_to_exe
import tkinter as tk

def on_click(event):
    curent_text = entry_var.get()
    clicked_button_text = event.widget.cget("text")
    if clicked_button_text == "=":
        try:
            results = eval(curent_text)
            entry_var.set(results)
        except Exception as e:
            entry_var.set("ERROR")
    elif clicked_button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(curent_text+clicked_button_text)







root = tk.Tk()
root.title("Какулятор")

entry_var = tk.StringVar()


entry = tk.Entry(root,textvariable=entry_var, width=16, font=("Arial", 20), justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
"7", "8", "9", "/",
"4", "5", "6", "*",
"1", "2", "3", "-",
"0", ".", "=", "+",
"C"
]
row_val = 1
col_val = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text,font=("Helvetica",14),width=4,height=2)
    button.grid(row= row_val, column=col_val,padx=4,pady=4)
    button.bind("<Button-1>", on_click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1



root.mainloop()