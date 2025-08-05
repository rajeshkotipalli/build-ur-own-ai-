Name : rajesh k 

manavrachna international institue of research and studies 

1/24/set/baiot/013

# build-ur-own-ai-
i have done a small project in which the laptop operates by our voice commands ,which gives responses to questions that u asked , and can open ur applications like ms word ,excel,power point , any applications just by asking in words and search or type required information in it , this was done with python programming language which uses one of the coolest libraies which process natural language processing 


arvis is a Python-based desktop assistant that can perform various tasks using voice commands. It leverages several libraries to interact with the user, control applications, and search the web.

Features

Voice Interaction: Jarvis uses speech recognition to understand commands and a text-to-speech engine to respond.
Application Control: It can open applications like Notepad, Chrome, WhatsApp, PowerPoint, Excel, Edge, Sticky Notes, and Word.
Web Automation: Jarvis can perform the following actions using a web browser:
    Search for videos on YouTube.
    Conduct searches on Google.
    Search for and display images.
    Send messages on WhatsApp Web.
Intelligent Responses: It uses the Gemini API to answer questions and provide information.
Cross-Platform (with dependencies): The core Python code is cross-platform, but some application paths are specific to Windows.
Prerequisites

Before you run Jarvis, you need to have the following installed:

Python 3.x
Google Chrome web browser
A stable internet connection
Installation

Clone the repository:

Bash

git clone <repository_url>
cd jarvis
Install the required Python libraries:

Bash

pip install SpeechRecognition pyttsx3 rich pyautogui selenium google-generativeai
Download the necessary web driver for Selenium:

This project uses the Chrome web driver. Selenium will automatically download and manage the driver for you.

Set up the Gemini API:

Get your Gemini API key from Google AI Studio.
Replace the placeholder in the code with your actual API key:
genai.configure(api_key="YOUR_API_KEY")

Configure application paths (Optional):

If you are not using Windows or your applications are installed in different locations, you may need to update the paths in the open_app function in jarvis.py.

Usage

Run the jarvis.py file from your terminal:

Bash

python jarvis.py
Jarvis will greet you and start listening for commands. Here are some examples of what you can say:

"Open notepad"
"Search for cat videos on YouTube"
"Search in Chrome for the weather"
"Search for pictures of the moon"
"Next image" (after searching for images)
"Send hello world to John on WhatsApp"
"What is the capital of France?"
"Exit" or "Bye" to close the program.

Important Notes

Microphone Access: Ensure you have a working microphone and have granted the necessary permissions for the program to access it.
WhatsApp Web: The first time you use the WhatsApp feature, you will need to manually scan the QR code to log in.
Timeout: Jarvis has a 15-second timeout for listening. If no command is detected within this period, it will go offline.
Error Handling: The program includes basic error handling, but some issues (e.g., network problems, incorrect commands) might require a restart.
File Structure

`jarvis.py`: The main script containing all the logic for the AI assistant.
`README.md`: This file.
License

This project is open-source.
