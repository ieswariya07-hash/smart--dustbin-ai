import cv2
import time
from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='ta')
    tts.save("voice.mp3")
    os.system("start voice.mp3")

cap = cv2.VideoCapture(0)

last_wrong = 0
last_full = 0
last_clean = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.putText(frame, "Smart Dustbin System", (50,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    fill_level = int(time.time()) % 100

    # 🗑️ Dustbin Full Alert
    if fill_level > 80 and time.time() - last_full > 10:
        speak("டஸ்ட்பின் நிரம்பியுள்ளது. தயவு செய்து உடனே காலி செய்யுங்கள்.")
        last_full = time.time()

    # ⚠️ Wrong Waste Alert (demo simulation)
    if fill_level % 30 == 0 and time.time() - last_wrong > 10:
        speak("தவறான குப்பை போடப்பட்டுள்ளது. தயவு செய்து சரியான குப்பையை போடுங்கள்.")
        last_wrong = time.time()

    # ⏰ Cleaning Reminder (demo)
    if time.time() - last_clean > 20:
        speak("டஸ்ட்பின் நீண்ட நேரமாக சுத்தம் செய்யப்படவில்லை. தயவு செய்து சுத்தம் செய்யுங்கள்.")
        last_clean = time.time()

    cv2.imshow("Smart Dustbin", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()