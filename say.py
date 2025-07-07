
import cowsay
import pyttsx3

engine = pyttx.init()
this = input("What is this? ")
cowsays.cow(this)
engine.say(this)
engine.runAndWait()
