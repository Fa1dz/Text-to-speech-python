import pyttsx3

def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        text = input("Enter text to speak (or type 'exit' to quit): ").strip()
        if text.lower() == 'exit':
            break
        elif text:
            speak_text(text)
        else:
            print("Please enter some text.")

if __name__ == "__main__":
    main()