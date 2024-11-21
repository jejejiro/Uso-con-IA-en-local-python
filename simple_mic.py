#importamos suprocesos 
import requests
import subprocess as cmdLine
import speech_recognition as sr
import ollama

#iniciamos Inteigencia artificial


# Clase que traduce texto a voz
class eSpeak:

    #__init__ definimos voces
    def __init__(self, voz='mb-vz1'):
        self.voz = voz

    # dice el texto
    def decir(self):
        # define la linea de comando
        command = 'espeak -v ' + self.voz + " " + chr(34) + ctext + chr(34)
        # ejecuta comando en la terminal
        print(command)
        result = cmdLine.run(command, shell=True, capture_output=True, text=True)

#clase que traduce voz a texto
class reconocevoz:
    def __init__(self):
        self.r = sr.Recognizer()

    def recognize(self):
        with sr.Microphone() as source:
            self.r.pause_threshold = 0.9 # debe detener automaticamente la grabacion
            self.r.energy_threshold = 6000
            print ("hable ahora : ")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language="es")
                return text
                
                #print(text)              
            except:
                print("error")


eS = eSpeak()
recognition = reconocevoz()


while True:
    text = recognition.recognize()
    if text:        
        stream = ollama.chat(
            model='llama3', 
            messages=[{"role": "user", "content": text},
                      {"role": "assistant", "content": "asistente"}
                      ],
                     format=text, 
                     options={"temperature": 0.1}
            )
        for chunk in stream:
           #print(chunk['message']['content'], flush=True)
            ctext = stream['message']['content']
            #print(bot)
        eS.decir()
    
