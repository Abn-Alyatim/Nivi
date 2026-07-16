import os
import sys
import contextlib
import time
from dotenv import load_dotenv
from groq import Groq
import speech_recognition as sr
from gtts import gTTS

# 1. تهيئة
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@contextlib.contextmanager
def suppress_stderr():
    try:
        stderr_fileno = sys.stderr.fileno()
        saved_stderr_fd = os.dup(stderr_fileno)
        with open(os.devnull, 'w') as devnull:
            os.dup2(devnull.fileno(), stderr_fileno)
            yield
            os.dup2(saved_stderr_fd, stderr_fileno)
            os.close(saved_stderr_fd)
    except: yield

def listen_and_recognize():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.0
    
    print("\n🎤 NEVE: Listening... (Speak clearly) / استمع إليك...")
    
    try:
        with suppress_stderr():
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.8)
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
        
        print("⏳ Recognizing...")
        # استخدام لغة فارغة سيجعل Google يتعرف تلقائياً (يفضل أن تضبط إعدادات جهازك للصوت)
        # إذا استمرت المشكلة، سنستخدم لغة خليطة
        user_text = recognizer.recognize_google(audio, language="en-US,ar-SA")
        
        print(f"🗣️ You said: {user_text}")
        return user_text
    except Exception as e:
        print(f"❌ Recognition Error: {e}")
        return None

def speak_text(text_to_speak):
    try:
        if not text_to_speak.strip(): return
        output_file = "response.mp3"
        
        # كشف اللغة
        has_arabic = any(u'\u0600' <= char <= u'\u06FF' for char in text_to_speak)
        
        # اختيار اللغة الصحيحة للنطق
        tts = gTTS(text=text_to_speak, lang='ar' if has_arabic else 'en', slow=False)
        tts.save(output_file)
        
        time.sleep(0.2) # انتظار بسيط للتأكد من الكتابة
        os.system(f"mpv --no-video {output_file} > /dev/null 2>&1")
        
        if os.path.exists(output_file): os.remove(output_file)
    except Exception as e:
        print(f"\n❌ Voice Error: {e}")

# ... (باقي كود الـ Loop الرئيسي كما هو)
while True:
    try:
        input("\n⌨️ Press [ Enter ] to speak...")
        user_input = listen_and_recognize()
        if not user_input: continue
            
        # إضافة إرشاد للنموذج ليفهم أنك تطلب منه اللغة
        prompt = f"The user said: {user_input}. Please answer in the SAME language the user used (if English, answer in English; if Arabic, answer in Arabic)."
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=250
        )
        
        response_text = completion.choices[0].message.content
        print(f"\n🤖 NEVE: {response_text}")
        speak_text(response_text)
            
    except KeyboardInterrupt:
        break
