from tkinter import scrolledtext
from tkinter import *


def go_kick_some_dirt():
    root.destroy()


click_counter = 0  # global variable to count the number of clicks on the 'NEXT LINE' button


def copy_text_from_input():

    global click_counter
    click_counter += 1  # increment by 1 everytime the button is clicked

    text = text_area.get("1.0",
                         "end")  # retrieve the text from text_area starting from line 1 and column 0 up to the end of the text.

    lines = text.split("\n")  # split the retrieved text into lines based on the newline character \n.

    if click_counter == 1:  # first click on button
        text_area_2.insert("1.0", lines[0] + "\n")  # insert the first line into text_area_2 at line 1 and column 0, followed by a newline character.
        text_area_2.update()
        text_area_3.delete("1.0", "end")  # delete current value of current processing line
        text_area_3.insert("1.0", click_counter)  # print out current processing line #1
    elif click_counter < len(lines):  # from second click
        text_area_2.insert("end", lines[click_counter-1] + "\n")  # continue insert text into text_area_2
        text_area_2.update()
        text_area_3.delete("1.0", "end")  # delete current value of current processing line
        text_area_3.insert("1.0", click_counter)  # print out new value of current processing line


root = Tk()
root.title("Lexical Analzyer for TinyPie")

label1 = Label(root, text="Source Code Input: ")  
label2 = Label(root, text="Lexical Analyzed Result: ")
label3 = Label(root, text="Current Processing Line: ")

text_area = scrolledtext.ScrolledText(root, width=40, height=18, font=("Bold", 10))
text_area_2 = scrolledtext.ScrolledText(root, width=40, height=18, font=("Bold", 10))
text_area_3 = Text(root, width=8, height=1, font=("Bold", 10))

exit_button = Button(root, text="QUIT", padx=40, pady=20, command=go_kick_some_dirt)
Next_Line_button = Button(root, text="NEXT LINE", padx=40, pady=20, command=copy_text_from_input)

label1.grid(row=0, column=0)
label2.grid(row=0, column=10)
label3.grid(row=10, column=0)

exit_button.grid(row=3, column=10)
Next_Line_button.grid(row=3, column=0)

text_area.grid(column=0, row=2, pady=10, padx=10)
text_area_2.grid(column=10, row=2, pady=10, padx=10)
text_area_3.grid(column=1, row=10, pady=10, padx=10)

text_area_3.insert("1.0", 0)  # print out current processing line #0

text_area.focus()
text_area_2.focus()
root.mainloop()
