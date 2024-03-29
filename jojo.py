import speech_recognition as sr
import pyttsx3
import pywhatkit

# from langchain.llms import o
# from keys import OPENAPI_KEY

# Playing with langchain
# def main():
#     llm = OpenAI(openai_api_key=OPENAPI_KEY)
#     result = llm.predict('5 ideas for videos on python')
#     # ("What's the best thing to do when travelling?")
#     print(result)



# Voice Reply
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


# listening
def get_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone(1) as source:
            print(f"Microphone: {source}")
            speak("It's Jojo and your microphone is ready!")
            print('Listening...')
            # Set a timeout for listening (adjust as needed)
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source, timeout=10)
            print('Recognizing...')
            command = listener.recognize_google(audio)
            print("You: " + command)
            speak(command)
            return command.lower()
    except sr.UnknownValueError:
        print('Jojo could not understand the audio')
    except sr.RequestError as e:
        print(f'Request error: {e}')
    except sr.WaitTimeoutError:
        print('Timeout occurred, no command detected within the specified time')
    except Exception as e:
        print(f'Error occurred: {e}')


# Jojo gets called
def run_jojo():
    command = get_command()
    command = str(command).lower()

    if 'play me' in command:
        obj = str(command).replace('play me', '')
        cmd_updated = str(command).replace('play me', 'playing')
        print('Jojo: ' + cmd_updated)
        speak(f'Play {obj}?:')
        correct = input(f'Play {obj}? (y/n):')
        if correct.lower() == 'y':
            speak('Playing ' + obj)
            pywhatkit.playonyt(obj)
        else:
            obj = input('Please make the correction: ')
            speak('Playing ' + obj)
            pywhatkit.playonyt(obj)



if __name__ == '__main__':
    run_jojo()