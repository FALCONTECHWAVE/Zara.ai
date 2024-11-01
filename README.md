# Zara.ai
Here's a user manual for the Zara Voice Assistant, including instructions for setting up and running the application in Visual Studio Code (VS Code).

User Manual for Zara Voice Assistant

Table of Contents

1. Introduction


2. Features


3. System Requirements


4. Installation Instructions


5. Setting Up in Visual Studio Code


6. Usage Instructions


7. Troubleshooting Tips


8. Contact Information



1. Introduction

Zara is a voice-activated personal assistant designed to help users manage tasks, retrieve information, and control applications through voice commands.

2. Features

2.1 Voice Interaction

Voice Commands: Interact with Zara using natural language.

Text-to-Speech: Zara responds with spoken feedback.


2.2 Time and Date Functions

Current Time: "What time is it?"

Current Date: "What’s the date today?"


2.3 Web Browsing

Open Website: "Open website [website name]."

Web Search: "Search [query]."


2.4 Information Retrieval

Wikipedia Lookup: "Tell me about [topic/person]."


2.5 Application Control

Launch Applications: "Launch [application name]."


2.6 Music Playback

Play Music: "Play music [song name]."


2.7 Note Taking

Take Note: "Take note." Followed by dictated content.


2.8 Screenshots

Take Screenshot: "Screenshot." Followed by a filename.


3. System Requirements

Operating System: Windows, Linux, or macOS

Python Version: 3.x

Required Libraries:

pyttsx3

speech_recognition

wikipedia

pywhatkit

pyautogui


Hardware: Microphone and speakers/headphones.


4. Installation Instructions

1. Download Python: Install Python from the official website.


2. Install Required Libraries: Open your terminal or command prompt and run the following commands:

pip install pyttsx3 SpeechRecognition wikipedia pywhatkit pyautogui



5. Setting Up in Visual Studio Code

1. Install Visual Studio Code: Download and install from the official website.


2. Open VS Code: Launch Visual Studio Code.


3. Create a New Folder:

Go to File > Open Folder…, and create a new folder for the Zara project.



4. Create a New Python File:

Right-click in the Explorer panel and select New File. Name it zara_assistant.py.



5. Copy the Zara Code: Paste the following code into zara_assistant.py:
<a id="installing"></a>
```
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit as kit
import pyautogui
import datetime
import os

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the service.")
            return None

def take_note():
    speak("What would you like to note?")
    note = listen()
    if note:
        with open("important_notes.txt", "a") as f:
            f.write(f"{note}\n")
        speak("Note taken.")

def take_screenshot(filename):
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{filename}.png")
    speak("Screenshot taken.")

def main():
    speak("Hello, I am Zara. How can I assist you?")
    while True:
        command = listen()
        if command:
            if "time" in command:
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}.")
            elif "date" in command:
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                speak(f"Today's date is {current_date}.")
            elif "open website" in command:
                website = command.replace("open website ", "")
                os.system(f"start {website}")
                speak(f"Opening {website}.")
            elif "search" in command:
                query = command.replace("search ", "")
                kit.search(query)
                speak(f"Searching for {query}.")
            elif "tell me about" in command:
                topic = command.replace("tell me about ", "")
                summary = wikipedia.summary(topic, sentences=1)
                speak(summary)
            elif "launch" in command:
                app = command.replace("launch ", "")
                os.system(f"start {app}")
                speak(f"Launching {app}.")
            elif "play music" in command:
                song = command.replace("play music ", "")
                kit.playonyt(song)
                speak(f"Playing {song}.")
            elif "take note" in command:
                take_note()
            elif "screenshot" in command:
                filename = input("Enter a name for the screenshot file: ")
                take_screenshot(filename)
            elif "exit" in command:
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main()


6. Run the Application:

Open the integrated terminal in VS Code (View > Terminal).

Ensure you are in the directory where your zara_assistant.py file is located.

Run the application by executing:

python zara_assistant.py

```


6. Usage Instructions

Activate Zara: Once the application is running, Zara will greet you and listen for commands.

Give Commands: Speak clearly and naturally; Zara will respond to your commands.

Exit Command: Say "exit" or "quit" to close the assistant.


7. Troubleshooting Tips

Unresponsive Commands: Check microphone settings and ensure it’s not muted.

Installation Issues: Verify that all required libraries are installed correctly.

Voice Recognition Errors: Ensure a quiet environment when giving commands.


8. Contact Information

For support or inquiries, please reach out to the developer at [falcontechwave@gmail.com].


---

This user manual provides a comprehensive guide for setting up and using the Zara Voice Assistant in Visual Studio Code, covering installation, usage, and troubleshooting.

