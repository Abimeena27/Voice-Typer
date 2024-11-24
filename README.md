# Voice Typing Application

## Overview
The Voice Typing Application is a simple desktop application that converts speech into text in real-time. Built using Python's Tkinter library for the GUI and the SpeechRecognition library for converting speech to text, this tool allows users to dictate text via microphone input. It offers a user-friendly interface with start and stop buttons, along with a text box to display the transcribed speech.

## Features
- **Real-time Speech-to-Text**: Convert your speech into text in real time with a simple click of a button.
- **Start and Stop Control**: Easily control the voice recognition with start and stop buttons.
- **Text Display**: The transcribed text is shown in a text box, allowing users to view the results immediately.

## Requirements
- **Python**: Ensure Python is installed on your system.
- **Libraries**: 
  - `speech_recognition`
  - `tkinter`

## Installation
To get started with the application, follow these steps:
1. Clone or download the project repository.
2. Install the necessary dependencies by running:
   ```bash
   pip install SpeechRecognition
   ```
3. For systems lacking Tkinter, install it via the system's package manager (e.g., for Ubuntu: `sudo apt-get install python3-tk`).

## How to Use
1. **Start Recognition**: Click the "Start" button to begin the speech recognition process. Speak into your microphone, and the application will transcribe your speech into text.
2. **Stop Recognition**: When you are done, click the "Stop" button to stop the speech recognition and view the text transcribed.

## Contributions
Feel free to fork the project, submit issues, or propose changes to improve the application.

## License
This project is open-source and licensed under the [MIT License](LICENSE).

## Acknowledgements
- **SpeechRecognition Library**: The core functionality of speech-to-text conversion is powered by the SpeechRecognition library.
- **Tkinter**: Tkinter is used to create the graphical user interface for the application.