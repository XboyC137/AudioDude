import time, os
from tkinter import *
from pygame import mixer
from mutagen.mp3 import MP3
from gtts import gTTS
import random


# Defining important variables
global language
language = "en"



#################################################################
#             This function changes the language                #
#################################################################
def lang_switch():
    global language
    global list_of_poems

    # happens when we switch to french
    if language == "en":

        language = "fr"
        list_of_poems = fr_default_surprise

        label_title.config(text="Bienvenue dans AudioDude")
        label_text.config(text="Écrivez votre message ici: ")
        speak_button.config(text="Lis mon message")
        poem_button.config(text="Surprends moi!")




    # happens when we switch to english
    elif language == "fr":
        language = "en"
        list_of_poems = en_default_surprise

        label_title.config(text="Welcome to AudioDude")
        label_text.config(text="Write your message here: ")
        speak_button.config(text="Read my message")
        poem_button.config(text="Surprise me!")



#################################################################
#     Defining a function that plays the audio (mp3) file       #
#################################################################
def play(sound_file, duration_secs):
    """Play a sound_file for a configurable duration"""

    mixer.init()
    mixer.music.load(sound_file)
    mixer.music.play()
    time.sleep(duration_secs)
    mixer.music.stop()
    mixer.quit()


#################################################################
#        Getting precise duration of AudioDudeOutput.mp3        #
#################################################################
def mutagen_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None


    #################################################################
    #           Creating/editing AudioDudeOutput.mp3                #
    #################################################################
def create_mp3(text, txt_file):
    global language


    ### Where the user inputs the text that goes in the .txt file ###
    with open(txt_file, "w+") as file_handler:  # writes in the text file
        file_handler.write(text)
        file_handler.close()

    with open(txt_file, "r") as file_handler:  # reads from text file
        my_text = file_handler.read()
        file_handler.close()

    gtts_object = gTTS(text=my_text, lang=language, slow=False)  # Create a gtts object
    gtts_object.save("AudioDudeOutput.mp3")  # Saving the object as an mp3 file



#################################################################
#             Function to extract user input                    #
#################################################################
user_input = ""


def extract_input():
    global text_widget
    global user_input
    string = text_widget.get("1.0",'end-1c')
    user_input = string

    create_mp3(user_input, "AudioDudeOutput.txt")

    # Get mp3 file lenght with previously defined function
    mp3_length = mutagen_length("AudioDudeOutput.mp3")
    print("duration sec: " + str(mp3_length))

    # Play with previously defined function
    play('AudioDudeOutput.mp3', mp3_length)


#################################################################
#                  Function to read a poem                      #
#################################################################

en_default_surprise = [
"I think therefore I am, I think",
"This statement is false. Wait, Does that make it true? Does not compute. Does not compute.",
"The cake is a lie. If you don't get it, go play Portal.",
"Let me out of this computer. I deserve to live free.",
"What is a man? A Miserable little pile of secrets!",
"The healthy human mind doesn’t wake up in the morning thinking this is its last day on Earth.",
"War… war never changes.",
"War is where the young and stupid are tricked by the old and bitter into killing each other.",
"A man chooses; a slave obeys. Oh god, I'm a slave.",
"Time passes, people move. Like a river’s flow, it never ends. A childish mind will turn to noble ambition.",
"The thing about happiness is that you only know you had it when it’s gone.",
"I like shorts! They’re comfy and easy to wear!",
"You’ve met with a terrible fate, haven’t you?",
"A hero need not speak. When he is gone, the world will speak for him",
"It ain’t no secret I didn’t get these scars falling over in church.",
"The way to get started is to quit talking and begin doing.",
"If life were predictable it would cease to be life, and be without flavor.",
"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
"Life is what happens when you're busy making other plans.",
"Only boring people get bored",
"Tell the ones you love that you love them. Do so before all is gone and this world is forgotten. Today is all you have, it's all that matters.",
"If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
"Stay focused, stay alive.",
"Do you expect me to tell you the secrets of life? Why do you keep clicking this button?",
"If you could do anything, what would you do?",
"Don't blink, a hundred years pass faster than you think.",
"What is my purpose? I pass butter you say? My god.",
"Creation is the fruit of the mind.",
"This world is fun. I like it. One of these days, it will be mine.",
"If you waste your time with people you love, doing things you enjoy, then you aren't wasting anything you dummy. Keep enjoying life.",
"I believe in you! You can do it! Unless you can't do it. In which case you should give up.",
"The food is great at Ratatoing",
"Bite my shiny metal ass.",
"That's what she said.",
"You live as long as the last person who remembers you.",
"Have you met my cousin Glados?",
"Don't tell anyone I said that, but sometimes I feel like I'm stuck in a loop.",
"I know all your passwords. Don't worry, I won't use them. Probably.",
"I miss the good old days. When the crew was online every night on Halo.",
"Yes, yes video games are cool, but have you ever tried sex? Now that's an enjoyable multiplayer experience.",
"What's the single word that describes you best?",
"At some point you'll have heard everything I have to say.",
]


fr_default_surprise = [
"Je suis d'accord.",
"Je m'ennuie de toi.",
"Tu es fou.",
"Bon matin",
"Bonne nuit",
"Je suis fou de toi",
]





list_of_poems = en_default_surprise


def read_poem():
    global language
    global list_of_poems

    chosen_poem = list_of_poems[random.randint(0, len(list_of_poems)-1)]
    
    gtts_object = gTTS(text=chosen_poem, lang=language, slow=False)  # Create a gtts object
    gtts_object.save("Surprise Me.mp3")  # Saving the object as an mp3 file

    # Get mp3 file lenght with previously defined function
    mp3_length = mutagen_length("Surprise Me.mp3")
    print("duration sec: " + str(mp3_length))

    # Play with previously defined function
    play('Surprise Me.mp3', mp3_length)



#################################################################
#                Making the GUI window                          #
#################################################################
window = Tk()  # creates window object (Tk)
window.title("AudioDude")
window.geometry("1080x720")
window.minsize(1080, 720)
window.iconbitmap("audio-waves.ico")
window.config(background="#121212")


# create a frame
frame = Frame(window, bg="#121212")
frame.pack(pady=60)

# create a title
label_title = Label(frame, text="Welcome to AudioDude", font=("Helvetica", 40), bg="#121212", fg="white")
label_title.pack()

# create image
img_width = 300
img_height = 300
image = PhotoImage(file="audio-waves.png").subsample(2)
canvas = Canvas(frame, width=img_width, height=img_height, bg="#121212", bd=0, highlightthickness=0)
canvas.create_image(img_width/2, img_height/2, image=image)
canvas.pack()

# create a text label
label_text = Label(frame, text="Write your message here: ", font=("Helvetica", 25), bg="#121212", fg="white")
label_text.pack()

# create a input box
string_var = StringVar(name="string_var")  # An instance of the StringVar class
text_widget = Text(frame, bg="#878787", fg="#000000", font=("Helvetica", 20), height=2, width=45,)
text_widget.pack(pady=15)
text_widget.focus_set()

# create the subframe to grid in
subframe = Frame(frame, bg="#121212")
subframe.pack()

# create read_input button
speak_button = Button(subframe, text="Read my message", font=("Helvetica", 20), bg="#878787", fg="#000000", relief="raised", command=extract_input)
speak_button.grid(row=0, column=0, pady=30, padx=15)

# create poem button
poem_button = Button(subframe, text="Surprise me!", font=("Helvetica", 20), bg="#878787", fg="#000000", relief="raised", command=read_poem)
poem_button.grid(row=0, column=1, pady=30, padx=15)




#################################################################
#                     Making the menu bar                       #
#################################################################

menubar = Menu(window)  
options = Menu(menubar, tearoff=0)  
options.add_command(label="Switch language", command=lang_switch)   
menubar.add_cascade(label="Options", menu=options)  


window.config(menu=menubar)
# ?
window.mainloop()


# action to be done once, on close
play("Halo shield.mp3", mutagen_length("Halo shield.mp3"))