import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import requests
import cv2
import pyautogui
from pprint import pprint

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def take_commend():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("istening..")
        audio = r.listen(source)

        try:
            cm = r.recognize_google(audio, language="en-US")
            print(f"you said: {cm}\n")
        except:
            print('sorry i did-int understand please try again\n')
            speak('sorry i did-int understand please try again')
            return "None"
    return cm


NAME = "none"


def welcom():
    hour = datetime.datetime.now().hour
    if 0 <= hour <= 12:
        print("Hello , Good Morning\n")
        speak("Hello , Good Morning")
    elif 12 < hour <= 16:
        print("Hello , Good After Noon\n")
        speak("Hello , Good After Noon")
    else:
        print("Hello , Good Evening\n")
        speak("Hello , Good Evening")

    print("What is your name? \n")
    speak("What is your name? ")
    global NAME
    while True:
        NAME = take_commend().lower()
        if NAME != "none":
            break
    print(f"Welcom  {NAME} . lets start!\n")
    speak(f"Welcom  {NAME} . lets start!")


# welcom()

while True:
    print("How can i help you?\n")
    speak("How can i help you?")
    commend = take_commend().lower()
    if "bye" in commend or "stop" in commend:
        print(f"Goodby {NAME}\n")
        speak(f"Goodby {NAME}")
        break
    if "wikipedia" in commend:
        print("Searchin Wikipedia\n")
        speak("Searchin Wikipedia")
        commend = commend.replace("wikipedia", "")
        print("how many sentens of the resaults would you like to read to you?\n")
        speak("how many sentens of the resaults would you like to read to you?")
        try:
            sentences = int(take_commend())
        except:
            sentences = 3
        result = wikipedia.summary(commend, sentences=sentences)
        print(f"{sentences} sentences of  your search result in wikipedia\n")
        speak(f"{sentences} sentences of  your search result in wikipedia")
        pprint(result + "\n")
        speak(result)
    elif "youtube" in commend:
        webbrowser.open_new_tab("https://www.youtube.com")
        print("opening youtube.\n")
        speak("opening youtube.")
        time.sleep(5)
    elif "google" in commend:
        webbrowser.open_new_tab("https://www.google.com")
        print("opening google.\n")
        speak("opening google.")
        time.sleep(5)
    elif "news" in commend:
        webbrowser.open_new_tab("https://www.news.google.com")
        print("opening news.\n")
        speak("opening news.")
        time.sleep(20)
    elif "time" in commend:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f" the time is {str_time}\n")
        speak(f" the time is {str_time}")
    elif "camera" in commend or "photo" in commend:
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        if ret:
            cv2.imwrite("your_photo.png", frame)
        camera.release()
        # cv2.destroyWindow()
        print("your photo was taken\n")
        speak("your photo was taken")
    elif "screenshot" in commend:
        my_screenshot = pyautogui.screenshot()
        my_screenshot.save("screenshot.png")
        print("your screenshot was taken\n")
        speak("your screenshot was taken")
    elif "search" in commend:
        commend = commend.replace("search", "")
        print(f"searching{commend}\n")
        speak(f"searching{commend}")
        webbrowser.open_new_tab(commend)
        time.sleep(20)
    elif "ask" in commend:
        print("i can answer the ypur question\n")
        speak("i can answer the ypur question")
        question = take_commend()
        app_id = "84U5L9-95R5RV7TPV"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        print(answer + "\n")
        speak(answer)
    elif 'who' in commend:
        print("hello,i am version of the voice assistant and was programmed by reza\n")
        speak("hello,i am version of the voice assistant and was programmed by reza")
    elif "note" in commend:
        print(f"what should i write {NAME} ? \n")
        speak(f"what should i write {NAME} ?")
        note = take_commend()
        print(f"should i include the time and date ?\n")
        speak(f"should i include the time and date ?")
        ans = take_commend()
        if "y" in ans:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            with open("note.txt", "w") as file:
                file.write(str_time)
                file.write("-" * 40)
                file.write(note)
        else:
            with open("note.txt", "w") as file:
                file.write(note)
    elif "show note" in commend:
        print("showing note..\n")
        speak("showing note..")
        with open("note.txt", "r") as file:
            s = (file.read())
            print(file.read() + "\n")
            speak(file.read())
    elif "photoshop" in commend:
        print("opening photoshop\n")
        speak("opening photoshop")
        os.startfile("C:\Program Files\Adobe\Adobe Photoshop 2023\Photoshop.exe")
        time.sleep(10)
    elif "logout" in commend:
        print("your system will log out after 5 seconds...\n")
        speak("your system will log out after 5 seconds...")
        time.sleep(5)
        subprocess.call(["shutdown","/l"])
    elif "weather" in commend:
        api_key = "1c087837a50f5845f105d3806246a8a0"
        base_url = "https://api.openweathermap.org/date/2.5/weather?"
        print("what is the city name? \n")
        speak("what is the city name? ")
        city_name = take_commend()
        complate_url = base_url + "appid = " + api_key + "&q=" + city_name
        response = requests.get(complate_url)
        res = response.json()
        if res["code"] != "404":
            main = res["main"]
            tempreture = main["temp"]
            humidity = main["humidity"]
            weather = res["weather"]
            weather_describtion = weather[0]["describtion"]
            print(f"tempreture in kelvin unit = {tempreture}\n")
            speak(f"humidity in kelvin unit = {tempreture}")
            print(f"tempreture  = {humidity}\n")
            speak(f"humidity  = {humidity}")
            print(f"weather = {weather}\n")
            speak(f"weather  = {weather}")
            print(f"weather_describtion  = {weather_describtion}\n")
            speak(f"weather_describtion  = {weather_describtion}")
