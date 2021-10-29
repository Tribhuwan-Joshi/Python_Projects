import pyttsx3
from PyDictionary import PyDictionary


class Speaking:
    def speak(self,audio):
        engine = pyttsx3.init('sapi5')  # using sapi5 tts engine
        
        # using getter and setter of pyttsx3
        voices = engine.getProperty("voices")
        
        engine.setProperty("rate" , 140)
        #Method for the speaking of the assistant
        engine.setProperty("voice",voices[0].id)

        # using the audio argument for speaking it out
        engine.say(audio)
        engine.runAndWait()


class Meaning:
    def Dictionary(self):
        speak = Speaking()  # instantiation of class Speaking
        dic = PyDictionary()

        
        speak.speak("Enter the word you want to find the meaning sir")

        # Taking the input from the user
        query= str(input())
        word = dic.meaning(query)

        # i am using this variable to make sure the engine don't read out all the meanings
        i=0
        if i<1: 
            for state in word:
            
                print(word[state])
                speak.speak(f"the meaning of {query} is ".format(query)+ str((word[state])[:2]))
                i+=1
        
        speak.speak("If you want to find more meanings please press 1 else press 0 to exit")
        find_more = int(input("Press 1 to find more meanings or Press 0 to exit: "))
        while find_more:
            speak.speak("Enter your another word sir!")
            query= str(input())
            word = dic.meaning(query)

            
            i=0
            if i<1: 
                for state in word:
                
                    print((word[state])[:2])
                    speak.speak(f"the meaning of {query} is ".format(query)+ str((word[state])[:2]))
                    i+=1
            
            speak.speak("If you want to find more meanings please press 1 else press 0 to exit")
            find_more = int(input("Press 1 to find more meanings or Press 0 to exit: "))

        speak.speak("Thank you and Hope I was helpful")


if __name__ == "__main__":
    Meaning()
    Meaning.Dictionary(self=None)



# Scripted by Tribhuwan-Joshi


