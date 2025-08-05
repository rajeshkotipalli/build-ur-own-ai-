import speech_recognition as sr
import pyttsx3
import os
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rich.console import Console
import google.generativeai as genai
import atexit

console = Console()
engine = pyttsx3.init()
atexit.register(engine.stop)

# === CONFIG ===
IDLE_TIMEOUT = 15  # seconds

# Configure Gemini API
genai.configure(api_key="AIzaSyAUtYcGmx9-dg1QGhOc_mHJ7PiTBPbPT60")

def set_male_voice():
    voices = engine.getProperty('voices')
    for voice in voices:
        if "david" in voice.id.lower():
            engine.setProperty('voice', voice.id)
            return
    for voice in voices:
        if "zira" not in voice.id.lower():
            engine.setProperty('voice', voice.id)
            return

def speak(text):
    console.print(f"[bold green]Jarvis:[/] {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech error:", e)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.energy_threshold = 100
        r.pause_threshold = 0.5
        r.dynamic_energy_thresold = True
        try:
            audio = r.listen(source, timeout=IDLE_TIMEOUT)
            command = r.recognize_google(audio)
            console.print(f"[bold cyan]You said:[/] {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            speak("No command received. Going offline.")
            exit()
        except sr.UnknownValueError:
            speak("I didn't catch that.")
            return ""
        except:
            speak("Mic error.")
            return ""

def open_app(command):
    apps = {
        "notepad": "C:\\Windows\\System32\\notepad.exe",
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "whatsapp": "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2412.2.0_x64__cv1g1gvanyjgm\\app\\WhatsApp.exe",
        "powerpoint": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk",
        "excel": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\excel.lnk",
        "edge": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk",
        "sticky notes": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Sticky Notes (new).lnk",
        "word": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
    }
    for app in apps:
        if app in command:
            try:
                os.startfile(apps[app])
                speak(f"Opening {app}")
                return True
            except FileNotFoundError:
                speak(f"Sorry, I couldn't find the file for {app}.")
                return False
    return False

def search_youtube(song):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.youtube.com/")
        wait = WebDriverWait(driver, 15)
        box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
        box.send_keys(song)
        box.send_keys(Keys.RETURN)
        speak(f"Searching YouTube for {song}")
    except Exception as e:
        speak("Failed to search YouTube.")
        print("YouTube error:", e)

def search_in_chrome(query):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.google.com/")
        wait = WebDriverWait(driver, 15)
        box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        box.send_keys(query)
        box.send_keys(Keys.RETURN)
        speak(f"Searching for {query} in Chrome")
    except Exception as e:
        speak("Failed to search in Chrome.")
        print("Chrome search error:", e)

def search_image(query):
    driver = webdriver.Chrome()
    driver.get(f"https://www.google.com/search?tbm=isch&q={query}")
    speak(f"Here are images for {query}")
    try:
        time.sleep(2)
        first_image = driver.find_element(By.XPATH, "(//img[contains(@class,'rg_i')])[1]")
        first_image.click()
        speak("Opened the first image.")
    except Exception as e:
        speak("Couldn't open the image, but the results are loaded.")
        print(e)

def next_image():
    pyautogui.press('right')
    speak("Next image")

def search_google(query):
    speak("Thinking...")
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
        response = model.generate_content(query)
        result = response.text.strip()
        if result:
            print(f"Gemini: {result}")
            speak(result)
        else:
            speak("Sorry, I couldn't get a proper response.")
    except Exception as e:
        print("Gemini error:", e)
        speak("Something went wrong while connecting to Gemini.")

def send_whatsapp_text(name, message):
    speak(f"Opening WhatsApp Web to send message to {name}")
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    speak("Please scan the QR code if not already logged in.")
    time.sleep(15)
    try:
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        time.sleep(1)
        search_box.send_keys(name)
        time.sleep(2)
        pyautogui.press("enter")

        msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        msg_box.send_keys(message)
        pyautogui.press("enter")
        speak("Message sent successfully.")

    except Exception as e:
        speak("Something went wrong while sending the message.")
        print(e)

def main():
    set_male_voice()
    speak("Hello Rajesh sir. Jarvis is now online.")

    while True:
        command = listen()

        if not command:
            continue

        if "exit" in command or "bye" in command:
            speak("Goodbye Rajesh sir.")
            break

        elif "open" in command and open_app(command):
            continue

        elif "youtube" in command or "play" in command:
            song = command.replace("search", "").replace("play", "").replace("on youtube", "").strip()
            search_youtube(song)

        elif "search in chrome" in command:
            query = command.replace("search in chrome", "").strip()
            search_in_chrome(query)

        elif "search for" in command and ("photo" in command or "image" in command or "picture" in command):
            query = command.replace("search for", "").replace("photo", "").replace("image", "").replace("picture", "").strip()
            search_image(query)

        elif "next image" in command or "next photo" in command:
            next_image()

        elif "send" in command and "to" in command and "on whatsapp" in command:
            try:
                message = command.split("send")[1].split("to")[0].strip()
                name = command.split("to")[1].split("on whatsapp")[0].strip()
                send_whatsapp_text(name, message)
            except:
                speak("I couldn't understand the message or contact name.")

        elif "video call" in command or "audio call" in command or "normal call" in command:
            speak("WhatsApp calling is not supported from PC. Please use your phone.")

        else:
            search_google(command)

if __name__ == "__main__":
    main()