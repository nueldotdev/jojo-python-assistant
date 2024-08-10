import speech_recognition as sr
import pyttsx3
import pywhatkit, wikipedia
from googlesearch.googlesearch import GoogleSearch

keywords_for_play = [
    'play', 'play me', 'start playing', 'try playing'
]

keywords_for_wiki = [
    'who is', 'what is', 'when is'
]

keywords_for_search = [
    'search', 'search for', 'find out', 'find'
]


inital = 0
recent_search_object = ''

# Voice Reply
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


# listening
def get_command():
    global inital
    inital += 1

    listener = sr.Recognizer()
    try:
        with sr.Microphone(1) as source:
            if inital <= 1:
                speak("It's Jojo and I'm listening!")
                print('Listening...')
            else:
                speak("Didn't hear you right...")
                speak("Please come again")
                print('Listening...')
            # Set a timeout for listening (adjust as needed)
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source, timeout=15)
            print('Recognizing...')
            command = listener.recognize_google(audio)
            print("You: " + command)
            speak(command)
            return command.lower()
    except sr.UnknownValueError:
        print('Jojo could not understand the audio')
        run_jojo()
    except sr.RequestError as e:
        print(f'Request error: {e}')
    except sr.WaitTimeoutError:
        print('Timeout occurred, no command detected within the specified time')
        run_jojo()
    except Exception as e:
        print(f'Error occurred: {e}')



def process_cmd(act: str, command: str, word: str):

    action = act + 'ing'

    obj = str(command).replace(word, '')
    cmd_updated = str(command).replace(word, action)
    print('Jojo: ' + cmd_updated)
    speak(action.capitalize() + " " + obj)

    return obj


# Jojo gets called
def run_jojo():
    command = get_command()
    command = str(command).lower()

    for word in keywords_for_play:
        if word in command:
            final = process_cmd('play', command, word)
            pywhatkit.playonyt(str(final))
            break
        else:
            pass

    for word in keywords_for_wiki:
        if word in command:
            final = process_cmd('search', command, word)
            result = wikipedia.summary(str(final), sentences=3)
            print(str(result))
            speak(str(result))

            break
        else:
            pass
    
    # elif 'who is' in command:
    #     obj = str(command).replace('who is', '')
    #     cmd_updated = obj + "is"

    #     print("Original: ", obj)
    #     print("Updated: ", cmd_updated)
        # cmd_updated = str(command).replace('who is', '')



if __name__ == '__main__':
    # run_jojo()
    response = GoogleSearch().search("something")
    for result in response.results:
        print("Title: " + result.title)
        print("Content: " + result.getText())
