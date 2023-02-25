#let's gooooooo!
import random
import time
from pyfiglet import Figlet

#lists of responses/interactions
intro_phrase = [
    "Hiii there :)",
    "Howdy",
    "Hello :D",
    "Yoooo",
    "Hey!",
    "Ahoy!",
    "Heyyyy!",
    "Whuddup!"
]

offering_advice = [
    "How can I help you?", 
    "Whatcha need help with?",
    "What can the oracle provide?",
    "I'm here. What's up?"
]

thinking_out_loud = [
    "Wow that's a tough one",
    "Give me a sec",
    "Give me a sec...",
    "...", 
    "Hmmmm",
    "Hmm...."
]

final_answer = [
    "Hmmmmm....no <3",
    ";)",
    "YES",
    "NO",
    "Not sure",
    "¯\_ (ツ)_/¯",
    "¯\_ (ツ)_/¯",
    "¯\_ (ツ)_/¯",
    "Teeheehe, what do you think?",
    "yep :)",
    "I don't know...",
    "Yep, you nailed it.",
    "idk"
    "Heck yeah!!!"
    "Of course!!",
    "Definitely!",
    "Mos def"
]

wanna_play_again = [
    "Do you have another question to ask?",
    "Have another question to ask?",
    "Wanna go deeper?",
    "Is there anything else?",
    "Anything else?",
    "Do you need more clarity?",
    "Need more clarity?"
]

bye = [
    "Byeeeee!",
    "Bye <3",
    "Until next time <3",
    "Farewell!",
    "See ya!"]



#fancy "the oracle" font
def intro_text_font():

    dope_font = Figlet(font='slant')
    
    print(dope_font.renderText('the'))
    print(dope_font.renderText('oracle'))    

    

# should be self-explanatory lol
def crystal_ball_image():
    print("            ⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠾⠛⠋⠉⠉⠉⠉⢙⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⠀⠀⢀⣼⠟⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⣷⡀⠀⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⠀⣾⢇⣤⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠁⢹⣇⠀⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⠀⠀⣠⣤⡙⠻⢿⣿⣿⣿⣿⣿⣋⣠⣤⡶⠟⢁⣤⡄⠀⠀⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣷⣤⣈⣉⠉⠛⠛⠉⣉⣠⣤⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⣾⣦⣀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⢋⣠⣴⣷⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⢿⣿⣿⣿⣷⣶⣤⣬⣭⣉⣉⣉⣩⣭⣥⣤⣶⣾⣿⣿⣿⡿⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀")
    print(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀")




#the start of the oracle's life
def awakening():

    intro_text_font()
    time.sleep(2)
    crystal_ball_image()
    time.sleep(2)
    
    print(
    "\nWelcome to the magical Oracle, where you can ask any question that your heart desires."
  )
    time.sleep(4)
    print("Actually, any yes/no* question your heart desires :)")
    time.sleep(3)
    print("because that's all I'm trained to do at this point...")
    time.sleep(3)
    print("...anyway...")
    time.sleep(1)

    intro_phrase_prompt = random.choice(intro_phrase)
    print("\n",intro_phrase_prompt, "\n")
    time.sleep(1)

    print("\n",random.choice(offering_advice), "\n")
    print("*** Think about your question, then press [enter] to 'ask' *** \n")


awakening()


#pressing enter to repeat the cycle of asking a question
def asking_the_question():

    while True:
    
        user_input = input("> ")
        
        # if user pressed [enter]  
        if user_input == "":
            # the oracle is thinking...
            time.sleep(1)
            print("\n",random.choice(thinking_out_loud))
        
            # the oracle is giving its answer
            time.sleep(2)
            print("\n",random.choice(final_answer),"\n")
        
            # the oracle asks if user has another question
            print()
            time.sleep(2)
            print(random.choice(wanna_play_again))
            print("\n*** Press [enter] to ask again or [q] to end ***\n")
        
        # if user types [Q] or [q]  
        elif user_input == "Q" or user_input == "q":
            #the oracle says bye
            print("\n",random.choice(bye), "\n")
            break
        
        # if user types something besides [enter] or [Q] or [q]
        else:
            print("\nOnly press the [enter] or [q] keys <3\n")
    

asking_the_question()
