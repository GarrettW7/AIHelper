from recording import testingNewRecording
from my_whisper import translateAudio
from dataSummarized import dataSummarized
from natalie import getNataliesOpinion
from jarvis import getjarvisesOpinion


def AiHelperHome():
    print()
    print("Welcome to the AI Helper Home!")
    print("Here you will be able to select between a couple different options/personalities of AI so they can help you!")
    print()
    # I need to implement this later
    # print("Would you like to talk directly to the AI or type your thoughts?")
    # print()
    print("0. Exit")
    print("1. AI VoiceMemoSummerizer: AI that will help you summarize your thoughts.")
    print("2. Natalie: A nutrition specialist, but also a great listener. Talk to her about anything!")
    print("3. Jarvis: A personal assistant that works with voice commands and can talk you through anything.")
    print()

    choice = input("Enter the number of the AI you would like to use: ").strip()
    if choice == '0':
        pass
    elif choice == '1':
        voiceMemoHome()
    elif choice == '2':
        Natalie()
    elif choice == '3':
        Jarvis()
    else:
        print("Invalid choice. Please try again.")
        AiHelperHome()


def voiceMemoHome():
    
    # recording()
    testingNewRecording()
    
    print("Translating... Please wait.")
    myText = translateAudio("output.wav")
    print()
    print("--------  AI OVERVIEW --------")
    print()
    data = dataSummarized(myText)
    print(data)
    print()
    print("--------  Hope I helped! --------")
    print()
    
    # choice = input("Would you like to record another voice memo? (yes/no): ").strip().lower()
    # if choice == 'no':
    #     break

    print("Thank you for using our service. Have a great day!")
    print("Goodbye!")

def Natalie():
    print("You are talking to Natalie!")
    print("When you want to end the conversation type 'exit'")
    convoHistory = ""
    while True:
        print()
        yourMessage = input("What do you want to ask her?  ")
        if yourMessage == 'exit':
            break
        print("Natalie is thinking...")
        print()
        print('----------- Natalie\'s Response -----------')
        
        convoHistory = convoHistory + getNataliesOpinion(yourMessage, convoHistory)
 
        print()
        print("(Remeber, you can quit by typing 'exit')")
        print()
    print("Thank you for talking to Natalie!")
    print("Goodbye!")

def Jarvis():
    print("You are going to talk to Jarvis!")
    while True:
        textOrSpeech = input("Would you like to talk to Jarvis through text or speech? (text/speech): ").strip().lower()
        if textOrSpeech == 'text' or textOrSpeech == 'speech':
            break
        else:
            print("Invalid choice. Please try again.")
    print("When you want to end the conversation type 'exit'")
    convoHistory = ""
    while True:
        print()
        if textOrSpeech == 'text':
            yourMessage = input("What do you want to ask him?  ")
        elif textOrSpeech == 'speech':
            testingNewRecording()
            print("Translating... Please wait.")
            yourMessage = translateAudio("output.wav")
        
        if yourMessage == 'exit':
            break

        print("Jarvis is thinking...")
        print()
        print('----------- Jarvis\'s Response -----------')
        
        convoHistory = convoHistory + getjarvisesOpinion(yourMessage, convoHistory)

        print()
        print("(Remeber, you can quit by typing 'exit')")
        print()
    print("Thank you for talking to Jarvis!")
    print("Goodbye!")
    

if __name__ == "__main__":
    AiHelperHome()