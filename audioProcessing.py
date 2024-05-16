import time
import random
import RPi.GPIO as GPIO
import speech_recognition as sr

# Setup GPIO
LED_PIN = 18 
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Initialize recognizer
r = sr.Recognizer()

# Function to process audio file
def process_audio(file_name):
    # Load the audio file
    with sr.AudioFile(file_name) as source:
        audio = r.record(source)

    # Recognize speech using Google Web Speech API
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        
        # Check the command and act
        if "on" in text.lower():
            print("Turning the light ON")
            GPIO.output(LED_PIN, GPIO.HIGH)
        elif "off" in text.lower():
            print("Turning the light OFF")
            GPIO.output(LED_PIN, GPIO.LOW)
    except Exception as e:
        print("Error recognizing speech: ", e)

# List of audio files
files = ['on.wav', 'off.wav']

def get_user_input():
    print("Available commands: 'on', 'off', 'random'")
    return input("Enter command (type 'exit' to quit): ")

try:
    # Process files based on user input
    while True:
        user_command = get_user_input()
        if user_command == 'exit':
            break
        elif user_command in ['on', 'off']:
            process_audio(f"{user_command}.wav")
        elif user_command == 'random':
            file = random.choice(files)
            process_audio(file)
        else:
            print("Invalid command.")
        time.sleep(5)  # 5 seconds delay
finally:
    # Cleanup GPIO before exiting
    GPIO.cleanup()
    print("GPIO cleanup done and program terminated successfully.")
