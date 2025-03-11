from customtkinter import *
from tkinter import Menu

def set_theme(theme):
    if theme == "light":
        set_appearance_mode("light")
    elif theme == "dark":
        set_appearance_mode("dark")

root = CTk()
root.title("Калькулятор")
root.geometry("339x440")

display = CTkEntry(root, font=('Arial', 24), justify='right', width=300, height=50)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def on_button_click(button):
    if button == "=":
        try:
            res = eval(display.get())
            res = int(res) if isinstance(res, float) and res.is_integer() else res
        except ZeroDivisionError:
            display.delete(0, END)
            display.insert(END, "Error, can't divide by zero")
        except Exception:
            pass
        else:
            display.insert(END, "=" + str(res))
    elif button == "C":
        display.delete(0, END)
    else:
        display.insert(END, button)

buttons = []
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    '(', ')'
]
row_val = 1
col_val = 0

for text in button_texts:
    button = CTkButton(root, text=text, font=('Arial', 20), width=75, height=60,
                       corner_radius=10, command=lambda t=text: on_button_click(t))
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    buttons.append(button)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

def set_button_color(color):
    color_map = {
        "Блакитний": "#3498db",
        "Сірий": "#808080",
        "Чорний": "#000000",
        "Помаранчевий": "#FF8C00"
    }

    new_color = color_map.get(color, "#3B3B3B")
    for button in buttons:
        button.configure(fg_color=new_color)

menubar = Menu(root)
theme_menu = Menu(menubar, tearoff=0)
theme_menu.add_command(label="Світла тема", command=lambda: set_theme("light"))
theme_menu.add_command(label="Темна тема", command=lambda: set_theme("dark"))
menubar.add_cascade(label="Тема", menu=theme_menu)

button_menu = Menu(menubar, tearoff=0)
button_menu.add_command(label="Блакитний", command=lambda: set_button_color("Блакитний"))
button_menu.add_command(label="Сірий", command=lambda: set_button_color("Сірий"))
button_menu.add_command(label="Чорний", command=lambda: set_button_color("Чорний"))
button_menu.add_command(label="Ющенко - так!", command=lambda: set_button_color("Помаранчевий"))
menubar.add_cascade(label="Колір кнопок", menu=button_menu)

root.config(menu=menubar)
root.mainloop()