# Jarvis - AI-Powered Voice Assistant

## Overview

Jarvis is a Python-based AI voice assistant designed to interact with users through natural language voice commands. The assistant can perform desktop automation, open applications, search the internet, answer user queries, and execute various tasks hands-free.

The project integrates Speech Recognition, Natural Language Processing (NLP), Web Automation, and Generative AI technologies to provide an intelligent and interactive user experience.

## Features

### Voice Interaction

* Converts user speech into text using Speech Recognition.
* Responds to user queries through Text-to-Speech (TTS).
* Supports continuous voice-based communication.

### Desktop Automation

Jarvis can open and manage various desktop applications through voice commands, including:

* Microsoft Word
* Microsoft Excel
* Microsoft PowerPoint
* Google Chrome
* Microsoft Edge
* Notepad
* Sticky Notes
* WhatsApp Desktop
* Other installed applications

### Web Search and Automation

* Search videos on YouTube.
* Perform Google searches.
* Search and display images online.
* Open websites using voice commands.
* Send messages through WhatsApp Web.

### AI-Powered Responses

* Integrates Google's Gemini API to answer questions intelligently.
* Provides real-time information and conversational responses.
* Uses Natural Language Processing (NLP) techniques to understand user requests.

### User-Friendly Experience

* Hands-free operation.
* Fast response time.
* Easy-to-use voice interface.

## Technologies Used

### Programming Language

* Python

### Libraries and Frameworks

* SpeechRecognition
* pyttsx3
* Selenium
* PyAutoGUI
* Rich
* Google Generative AI (Gemini API)

### Concepts Implemented

* Natural Language Processing (NLP)
* Speech-to-Text (STT)
* Text-to-Speech (TTS)
* Desktop Automation
* Web Automation
* Artificial Intelligence Integration

## Installation

Install the required dependencies:

```bash
pip install SpeechRecognition pyttsx3 rich pyautogui selenium google-generativeai
```

Configure your Gemini API key:

```python
genai.configure(api_key="YOUR_API_KEY")
```

Run the application:

```bash
python jarvis.py
```

## Sample Voice Commands

* "Open Microsoft Word"
* "Open Excel"
* "Search Python tutorials on YouTube"
* "Search weather updates on Google"
* "Show images of the Moon"
* "Send a WhatsApp message"
* "What is Artificial Intelligence?"

## Future Enhancements

* Offline voice recognition support
* Multi-language communication
* Smart home device integration
* Personalized user profiles
* Voice-based file management system

## Outcome

This project demonstrates the practical implementation of Artificial Intelligence, Natural Language Processing, Speech Recognition, and Automation technologies to create a smart desktop assistant capable of improving productivity through voice-based interaction.
