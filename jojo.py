import speech_recognition as sr
import pyttsx3
import pywhatkit, wikipedia

# Keywords for different actions
keywords_for_play = ['play', 'play me', 'start playing', 'try playing']
keywords_for_wiki = ['who is', 'what is', 'when is']
keywords_for_search = ['search', 'search for', 'find out', 'find']


wake_word = "hey jojo"

# Initialize variables
initial = 0

# Voice Reply
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    """Function to make Jojo speak."""
    engine.say(text)
    engine.runAndWait()


def listen_for_wake_word():
    """Listen for the wake word to activate Jojo."""
    listener = sr.Recognizer()
    with sr.Microphone(1) as source:
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source, timeout=15)
        try:
            command = listener.recognize_google(audio).lower()
            if wake_word in command:
                return True
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            pass
        except sr.WaitTimeoutError:
            pass
    return False

def get_command():
    """Listen for a command after the wake word is detected."""
    listener = sr.Recognizer()
    with sr.Microphone(1) as source:
        listener.pause_threshold = 5  # Seconds of silence before considering the input complete
        listener.energy_threshold = 300

        speak("What can I do for you?")
        print("Listening for command...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio).lower()
            print("You:", command)
            return command
        except sr.UnknownValueError:
            print("Jojo could not understand the audio.")
        except sr.RequestError as e:
            print(f'Request error: {e}')
        except sr.WaitTimeoutError:
            print('Timeout occurred, no command detected within the specified time.')
    return None

def process_cmd(act: str, command: str, word: str):
    """Process and print the command."""
    action = act + 'ing'
    obj = str(command).replace(word, '')
    cmd_updated = str(command).replace(word, action)
    print('Jojo: ' + cmd_updated)
    speak(action.capitalize() + " " + obj)
    return obj

def run_jojo():
    """Main function to manage Jojo's operation."""

    print("Waiting for wake word...")
    while True:
        if listen_for_wake_word():
            command = get_command()
            if not command:
                continue

            for word in keywords_for_play:
                if word in command:
                    final = process_cmd('play', command, word)
                    pywhatkit.playonyt(str(final))
                    break

            for word in keywords_for_wiki:
                if word in command:
                    final = process_cmd('search', command, word)
                    result = wikipedia.summary(str(final), sentences=3)
                    print(str(result))
                    speak(str(result))
                    break

            # After executing the command, Jojo goes back to listening for the wake word
            speak("Let me know if you need anything else.")
        

if __name__ == '__main__':
    run_jojo()
