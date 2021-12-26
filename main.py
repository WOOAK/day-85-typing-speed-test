# function refers to https://typing-speed-test.aoeu.eu/?lang=en, exclude feature to backspace to previous word
from tkinter import *
from tkinter import messagebox


text = "blade wake metal young sour snow seat menu anger huge area rebel risk draft fish ant pupil text flag snake year " \
       "month mail words post book sleep vote joke game list mint mass hell stone hat goose hand lower guess jade change " \
       "tree house speed space kind rest pouch single yarn crochet line check numb rust goods left need alone corn frown " \
       "girl account train hunt santa deer wrong label wish learn play"
word_list = text.split()
window = Tk()
window.title("Type Speedily")
window.config(width=2000, height=2000, padx=50, pady=50)


wrong_list=[]
position = 0
total_chars = 0
total_wrong = 0
start_pos = 0
end_pos= 0
one_second = 0

#TODO: countdown timer 60s after user press start button
def countdown(count):

    global entered_word, total_wrong, one_second
    if count > 0:
        if one_second%10 == 0:
            timer_label.config(text=round(count))
        checkText(word_list[position])
        # check every 0.2 seconds
        window.after(100,countdown, count-0.1)
        one_second += 1
    else:
# TODO: get length of typed text at the end of 60s(exclude wrong char), as cpm, wpm = int(cpm/5)
        # include unfinished word without type space
        total_wrong+=len(wrong_list)
        # Total characters tested
        total_chars = len(''.join(word_list[0:position]))+len(entered_word.lstrip())
# TODO: Exclude wrong typing word in cpm and wpm
        CPM = total_chars-total_wrong
        typing_text["state"]="disable"
        start_button["state"] = "normal"
        timer_label.config(text="0")

        print(total_chars)
        print(total_wrong)

        # messagebox.showinfo(title='Your result',message=f'Your CPM is {CPM},your WPM is {int(CPM / 5)}')
        result = Label(text=f'Your CPM is {CPM},your WPM is {int(CPM / 5)}',font=("Arial", 16, "bold"))
        result.pack()

# TODO: Triggered by start button, initialise variable to restart new game
def start_timer():
    global position, start_pos, end_pos, total_wrong, total_chars
    # reset everything
    total_wrong=0
    total_chars=0
    text_label.tag_remove("current_word", f"1.{start_pos}",f"1.{end_pos}")
    position = 0
    start_pos = 0
    end_pos = len(word_list[position])
    # highlight first word
    text_label.tag_add("current_word",f"1.{start_pos}",f"1.{end_pos}")
    text_label.tag_config("current_word",background="yellow")
    typing_text["state"]="normal"
    start_button["state"] = "disable"
    if len(typing_text.get("1.0",END))!=0:
        typing_text.delete('1.0', END)
    countdown(60)

def checkText(word):
    global entered_word
    # check whether spacebar typed.
    typing_text.bind("<Key>", space_typed)
    entered_word = typing_text.get("1.0", END).split('\n')[0]

    length = min(len(word), len(entered_word.lstrip()))

    for count in range(length):
        # typing_text.config(foreground='black')
# TODO: Need detect and highlight wrong typed char
        space_char_length = len(entered_word)-len(entered_word.lstrip())
        if word[count] != entered_word.lstrip()[count]:
            typing_text.tag_add("wrong", f"1.{count+space_char_length}")
            typing_text.tag_config("wrong", foreground='red')
            # text_label.tag_remove("correct", f"1.{count+space_char_length}")
            if count not in wrong_list:
                wrong_list.append(count)

        else:
# TODO: Turn back to black if correct
            typing_text.tag_add("correct", f"1.{count+space_char_length}")
            typing_text.tag_config("correct", foreground='black')
            # text_label.tag_remove("wrong", f"1.{count+space_char_length}")
            if count in wrong_list:
                wrong_list.remove(count)

# TODO: Spacebar/Enter to proceed to next word.
def space_typed(event):
    global position, wrong_list, total_wrong, entered_word, start_pos,end_pos
    # accidetally key in space at the beginning of text will not proceed to next word
    if (event.keysym=='space' or event.keysym=='Return') and len(entered_word.lstrip())!=0:
        # cater for forfeited word
        # example: "blade", user type space bar just after type "b", it consider 4 other chars wrong.
        total_wrong += (len(wrong_list)+len(word_list[position])-len(entered_word.lstrip()))
        wrong_list=[]
        #remove highlight of current when proceed to next word
        text_label.tag_remove("current_word", f"1.{start_pos}", f"1.{end_pos}")
        # proceed to next word after space bar typed
        position +=1
        start_pos = end_pos + 1
        end_pos = start_pos + len(word_list[position])
        text_label["state"]="normal"
        text_label.tag_add("current_word", f"1.{start_pos}", f"1.{end_pos}")
        text_label.tag_config("current_word", background="yellow")
        text_label["state"] = "disable"
        typing_text.delete('1.0', END)


#TODO: Display timer
timer_label= Label(text="00",font=("Arial", 30, "bold"))
timer_label.pack()
#TODO: Display text to be typed
text_label = Text(height=5,font=("Ms Sans Serif",24),spacing2=2.0,wrap="word")
text_label.insert(END,text)
text_label["state"]="disable"
text_label.pack()
#TODO: Create start button. Can use to restart for new game
start_button = Button(text="Start",command=start_timer)
start_button.pack()
#TODO: Column to type the word
typing_text = Text(window,width=10,height=1,bg='light cyan',font=("Arial",24), state='disable')
typing_text.pack()






## additional if got time
#TODO: keep various text sample
#TODO: random text sample,can press refresh to refresh the text
#TODO: keep high score, allow user type in name
#TODO: display highest score with name

window.mainloop()