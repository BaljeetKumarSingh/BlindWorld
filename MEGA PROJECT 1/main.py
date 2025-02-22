import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import musicLibrery
import requests
from openai import OpenAI
reconizer = sr.Recognizer()#hum jo bolenge usko recognize karega
engine = pyttsx3.init()#initialize
def speak(text):
    engine.say(text)
    engine.runAndWait() 

newsapi="431f0b2cf5014f7195a823b2e7c236e5"
def aiprosess(commend) :
            client = OpenAI(api_key="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",
            )

            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a vertual assistant. name subho.my location is jonka west bengal pin 711226s"},
                    
                        {"role": "user","content": commend }
                    
                ]

            )

            return completion.choices[0].message.content
def processCommand(c):
    if "open google" in c.lower():# same as if(c.lower == "open google")
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif"open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif"open Instagram" in c.lower():
        webbrowser.open("http://www.instagram.com")
    elif"open pornhub" in c.lower():
        webbrowser.open("http://pornhub.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrery.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
            response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=431f0b2cf5014f7195a823b2e7c236e5")
                    # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                articles = data.get("articles", [])
                
                # Speak each article title
                if articles:
                    speak("Here are the top news headlines:")
                    for i, article in enumerate(articles, start=1):
                        title = article.get("title", "No title available")
                        speak(f"Headline {i}: {title}")
                else:
                    speak("Sorry, I could not find any news articles.")
            else:
                speak("Sorry, I couldn't fetch the news. Please check your API key or connection.")
    
    else:
        #let open ai handle the request
        output=aiprosess(c)
        speak(output)
        print(output)


if __name__ == "__main__":
    speak("Initializing.. motherchod.......")
    speak("good evening sir i  am  motherchod  your  assistent  how  can  i  help  you  sir")
    while True:
            # Lisent forthe wake word Lilleeee...
            # obtain audio from the microphone
            r = sr.Recognizer()
            # recognize speech using Sphinx
            print("recognizing.....")
            try:
                with sr.Microphone() as source:
                    print("Listining....")
                    audio = r.listen(source,timeout=2,phrase_time_limit=2)
                    word=r.recognize_google(audio)
                    print(word)
                if(word.lower() == "mondal" or "mondol" or"sourav" or"sourabh" or"mandol" or"moondal" or "subho" or "shubho" or "suvo" or "subhoo" or "subbbho"):
                    speak("mondal activate...")
                    #listen for comand
                
                    with sr.Microphone() as source:
                        print("subho active....")
                        audio=r.listen(source,timeout=4,phrase_time_limit=4)
                        commend=r.recognize_google(audio)
                        processCommand(commend)

                
               
            except Exception as e:
                print("error; {0}".format(e))