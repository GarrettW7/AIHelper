from recording import recording
from my_whisper import translateAudio
from dataSummarized import dataSummarized
import keyboard as key
from natalie import getNataliesOpinion

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
    print()

    choice = input("Enter the number of the AI you would like to use: ").strip()
    if choice == '0':
        pass
    elif choice == '1':
        voiceMemoHome()
    elif choice == '2':
        Natalie()
    else:
        print("Invalid choice. Please try again.")
        AiHelperHome()


def voiceMemoHome():
    
    recording()
    
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
    while True:
        print()
        yourMessage = input("What do you want to ask her?  ")
        if yourMessage == 'exit':
            break
        print("Natalie is thinking...")
        print()
        print('----------- Natalie\'s Response -----------')
        print(getNataliesOpinion(yourMessage))
        print()
        print("(Remeber, you can quit by typing 'exit')")
        print()
    print("Thank you for talking to Natalie!")
    print("Goodbye!")
    

if __name__ == "__main__":
    AiHelperHome()