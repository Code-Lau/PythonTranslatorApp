#Real time translator using Python (https://www.geeksforgeeks.org/real-time-translation-app-using-python/)
from tkinter import ttk,messagebox
from googletrans import LANGUAGES, Translator
import textblob
#How to Build a Language Translator with Text and Audio Using Python and Google APIs (https://medium.com/@nikitasilaparasetty/how-to-build-a-language-translator-with-text-and-audio-using-python-and-google-apis-e2697a97b969)
from gtts import gTTS
import os
import speech_recognition as spr

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.resizable(0, 0)

#How to create translator using Python (https://www.youtube.com/watch?v=3ydfbFFrPWE&list=PLl316cKxhMxtOWHa88kDqm42uWz1aqGfD&index=5)
#Translations
class Translations:
    def label_change():
        c=combo1.get()
        c1=combo2.get()
        label1.configure(text=c)
        label2.configure(text=c1)
        root.after(1000,label_change)

    def translate_now():
        global language
        try:
            text_=text1.get(1.0,END)
            c2=combo1.get()
            c3=combo2.get()
            if(text_):
                words=textblob.TextBlob(text_)
                lan=words.detect_language()
                for i,j in language.items():
                    if(j==c3):
                        lan_=i
                words=words.translate(from_lang=lan,to=str(lan_))
                text2.delete(1.0,END)
                text2.insert(END,words)
        except Exception as e:
            messagebox.showerror("googletrans","Error, please try again")

#Language Translator Using Google API in Python (https://www.geeksforgeeks.org/language-translator-using-google-api-in-python/)
#Speech Recognition
recog1 = spr.Recognizer()
mc = spr.Microphone()

class SpeechRecognition:
    def recognize_speech(recog, source):
        try:
            recog.adjust_for_ambient_noise(source, duration=0.2)
            audio = recog.listen(source)
            recognized_text = recog.recognize_google(audio)
            return recognized_text.lower()
        except spr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
            return None
        except spr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

with mc as source:
    print("Speak 'hello' to initiate the Translation!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    MyText = recognize_speech(recog1, source)

if MyText and 'hello' in MyText:
    translator = Translator()
    from_lang = 'en'
    to_lang = 'hi'

    with mc as source:
        print("Speak a sentence to translate...")
        get_sentence = recognize_speech(recog1, source)

        if get_sentence:
            try:
                print(f"Phrase to be Translated: {get_sentence}")

                text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)
                translated_text = text_to_translate.text

                speak = gTTS(text=translated_text, lang=to_lang, slow=False)

                speak.save("captured_voice.mp3")

                os.system("start captured_voice.mp3")

            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Unable to capture the sentence for translation.")


#Application Icon
image_icon=PhotoImage(file="assets/images/googletranslateicon.png")
root.iconphoto(False,image_icon)

#Arrow Icon
arrow_image=PhotoImage(file="assets/images/arrowexchangeicon.png")
image_label=Label(root,image=arrow_image,width=150)
image_label.place(x=460,y=50)

#Language
language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

#Left Side
combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1=Text(f, font="Robote 20", bg="white", relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#Right Side
combo2=ttk.Combobox(root,values=languageV,font="RobotV 14",state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f1=Frame(root,bg="Black",bd=5)
f1.place(x=620,y=118,width=440,height=210)

text2=Text(f1, font="Robote 20", bg="white", relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#Translate Button
translate=Button(root,text="Translate",font="Roboto 15 bold italic",activebackground="purple",cursor="hand2",bd=5,bg="red",fg="white",command=translate_now)
translate.place(x=480,y=250)

label_change()
root.configure(bg="white")
root.mainloop()
