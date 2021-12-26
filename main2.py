# another version compare whole strings
from tkinter import *
from tkinter import messagebox
import keyboard

text = "blade wake metal young sour snow seat menu anger huge area rebel risk draft fish ant pupil text flag snake year month mail words post book sleep vote joke game list mint mass hell stone hat goose hand lower guess jade "
window = Tk()
window.title("Type Speedily")
window.config(width=2000, height=2000, padx=50, pady=50)

wrong_list=[]
#TODO: countdown timer 60s after user press start button
def countdown(count):
    global entered_text
    if count > 0:
        checkText()
        print(count)
        timer = window.after(500,countdown, count-0.5)
    else:
        CPM = len(entered_text)-len(wrong_list)
        # print("It's end!")
        print(entered_text)
        print(wrong_list)
        typing_text["state"]="disable"
        messagebox.showinfo(title='Your result',message=f'Your CPM is {CPM},your WPM is {int(CPM / 5)}')
def start_timer():
    typing_text["state"]="normal"
    if len(typing_text.get("1.0",END))!=0:
        typing_text.delete('1.0', END)
    countdown(60)


# TODO: Exclude wrong typing word in cpm and wpm

#TODO: Create start button
start_button = Button(text="Start",command=start_timer)
start_button.pack()
#TODO: Display text to be typed
text_label = Label(text=text, font=("Arial",16),wraplengt=1200)
text_label.pack()

#TODO: Column to type the word
typing_text = Text(window,width=149,height=50,bg='light cyan',font=("Arial",16), state='disable')
# entered_text = typing_text.get("1.0",END)
# print(entered_text)
typing_text.pack()

def checkText():
    global entered_text
    # typing_text.bind("<KeyRelease>", fun)
    # split \n to solve red issue even the words correct, after red colour
    entered_text = typing_text.get("1.0", END).split('\n')[0]
    # entered_text = typing_text.get("1.0", END)
    # print(f"{entered_text}.")
    # TODO: Need detect and highlight wrong typed char
    # TODO: Turn back to black if correct
    length = min(len(entered_text), len(text))
    for count in range(length):
        # typing_text.config(foreground='black')
        if text[count] != entered_text[count]:
            typing_text.tag_add("wrong", f"1.{count}")
            typing_text.tag_config("wrong", foreground='red')
            if count not in wrong_list:
                wrong_list.append(count)
        else:
            typing_text.tag_add("correct", f"1.{count}")
            typing_text.tag_config("correct", foreground='black')
            if count in wrong_list:
                wrong_list.remove(count)


# def fun(event):
#     print(event.keysym, event.keysym=='Space')
#     print(event)
#     print("hi")
#TODO: Allow to retype wrong word


#TODO: get length of typed text at the end of 60s(exclude wrong char), as cpm, wpm = int(cpm/5)

## additional if got time
#TODO: keep various text sample
#TODO: random text sample,can press refresh to refresh the text
#TODO: keep high score, allow user type in name
#TODO: display highest score with name

window.mainloop()