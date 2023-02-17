#let's gooooooo!

import random
import time
from pyfiglet import Figlet


def intro_text_font():
    
    dope_font = Figlet(font='slant')
    #dope_font = Figlet(font='5lineoblique')

    print(dope_font.renderText('the'))
    print(dope_font.renderText('oracle'))



# 8 BALL RESPONSES / INTERACTIONS
intro_phrase = [
    "hiii there :)",
    "howdy",
    "hello :D",
    "yoooo",
    "Hey!",
    "Ahoy!",
    "Heyyyy!",
]


offering_advice = [
    "how can I help you?",
    "Whatcha need help with?",
    "what can the oracle provide?",
    "I'm here. What's up?"
]


thinking_out_loud = [
    "wow that's a tough one",
    "give me a sec",
    "give me a sec...",
    "...",
    "hmmmm",
    "hmm...."
]


final_answer = [
    "hmmmmm....no <3",
    ";)",
    "YES",
    "NO",
    "not sure",
    "¯\_ (ツ)_/¯",
    "¯\_ (ツ)_/¯",
    "Teeheehe, what do you think?",
    "yep :)",
    "I don't know...",
    "Yep, you nailed it.",
    "of course!!"
]


wanna_play_again = [
    "Do you have another question to ask?",
    "have another question to ask?",
    "wanna go deeper?",
    "Is there anything else?",
    "anything else?",
    "Do you need more clarity?",
    "need more clarity?"
]


bye = [
    "byeeeee!",
    "bye <3",
    "until next time <3",
    "farewell!",
    "see ya!"
 ]


def awakening():
    
    intro_text_font()
    time.sleep(1)
    
    intro_phrase_prompt = random.choice(intro_phrase)
    print("\n",intro_phrase_prompt, "\n")
    time.sleep(2)

    offering_advice_response = random.choice(offering_advice)
    print("\n",offering_advice_response, "\n")
    print("    [press enter] \n")
    time.sleep(4)

awakening()



def asking_the_question():
    
    while True:

        enter_is_pressed = input("")

        thinking_out_loud_reponse = random.choice(thinking_out_loud)
        print()
        print(thinking_out_loud_reponse)
        print()
              
        
        final_answer_reponse = random.choice(final_answer)
        
        print()
        time.sleep(1)
        print(final_answer_reponse)
        time.sleep(1)
        print()
        
        wanna_play_again_response = random.choice(wanna_play_again)
        
        print()
        time.sleep(1)
        print(wanna_play_again_response)
        print("    [press enter]")
        print()

        time.sleep(7)

        bye_response = random.choice(bye)
        print("\n",bye_response, "\n")


asking_the_question()
