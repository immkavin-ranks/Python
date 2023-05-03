import pyttsx3
Wow = pyttsx3.init()
name = input("Name: ")
Wow.say(f'hello, {name}')
Wow.runAndWait()