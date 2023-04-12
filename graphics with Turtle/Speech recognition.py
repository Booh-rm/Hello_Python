import speech_recognition as sr
import turtle

r = sr.Recognizer()
t = turtle. Turtle()
with sr.Microphone() as source:
    print("Di 'dibujo' para comenzar a dibujar.")
    audio = r.listen(source)
    try:
        command = r.recognize_google(audio,language='es-ES')
        if command == "dibujo":
            t.forward(100)
            t.left(120)
            t.forward(100)
            t.left(120)
            t.forward(100)
    except:
        print("No se pudo entender lo que dijiste.")

