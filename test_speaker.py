import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 170)

engine.say("Hello Partner, Buddy is speaking.")

engine.runAndWait()
