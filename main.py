import os
import sys
import contextlib
import time
from dotenv import load_dotenv
from groq import Groq
import speech_recognition as sr
from gtts import gTTS
from events.bus import EventBus


def main():
    bus = EventBus()
    print("Nivi System Initialized...")
    


if __name__ == "__main__":
    main()
