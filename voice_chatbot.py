import speech_recognition as sr
import pyttsx3

# 음성 인식기 및 TTS 엔진 초기화
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen():
    """사용자의 음성을 듣고 인식합니다."""
    with sr.Microphone() as source:
        print("듣고 있습니다... 말씀해주세요.")
        audio_data = recognizer.listen(source)
        try:
            # 구글 웹 음성 API를 사용하여 인식(다른 API로 변경 가능)
            text = recognizer.recognize_google(audio_data, language='ko-KR')
            return text
        except sr.UnknownValueError:
            return "음성을 인식할 수 없습니다."
        except sr.RequestError:
            return "음성 인식 서비스에 접근할 수 없습니다."

def respond(text):
    """인식된 텍스트에 기반하여 응답합니다."""
    print("인식된 내용:", text)
    if "안녕" in text:
        response = "안녕하세요, 만나서 반가워요."
    else:
        response = "죄송해요, 이해하지 못했어요."
    print("응답:", response)
    tts_engine.say(response)
    tts_engine.runAndWait()

if __name__ == "__main__":
    while True:
        text = listen()
        if text:
            respond(text)
        else:
            break
