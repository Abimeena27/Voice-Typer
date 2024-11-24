import tkinter as tk
import threading
import speech_recognition as sr


def start_recognition():
    recognizer = sr.Recognizer()

    def listen():
        with sr.Microphone() as source:
            print("Adjusting noise")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening ... Speak Now.")
            try:
                audio = recognizer.listen(source)
                print("Recognizing....")
                txt = recognizer.recognize_google(audio, show_all=False)
                output_box.delete("1.0", tk.END)  # Clear the Text box
                output_box.insert(tk.END, txt)  # Insert the new text
                print(txt)
            except sr.UnknownValueError:
                print("Sorry, Can't Understand You")
                output_box.delete("1.0", tk.END)
                output_box.insert(tk.END, "Sorry, Can't Understand You")
            except sr.RequestError:
                print("Couldn't place your request")
                output_box.delete("1.0", tk.END)
                output_box.insert(tk.END, "Couldn't place your request")
            except Exception as e:
                print(f"Error: {e}")
                output_box.delete("1.0", tk.END)
                output_box.insert(tk.END, f"Error: {e}")

    while is_listening:
        listen()


def start():
    global is_listening
    is_listening = True
    start_btn.config(state=tk.DISABLED)  # Disable the start button
    stop_btn.config(state=tk.NORMAL)    # Enable the stop button
    threading.Thread(target=start_recognition, daemon=True).start()


def stop():
    global is_listening
    is_listening = False
    start_btn.config(state=tk.NORMAL)   # Enable the start button
    stop_btn.config(state=tk.DISABLED)  # Disable the stop button
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Voice typing stopped.")
    print("Typing Stopped")


# Initialize the application
root = tk.Tk()
root.title("Voice Typer")

root.geometry("750x750")
root.configure(bg='beige')

h1 = tk.Label(root, text="Voice Typer", font=("Times New Roman", 26, "bold italic"), bg='beige', fg='black')
h1.pack(pady=20)

btn_frame = tk.Frame(root, bg='beige')
btn_frame.pack(pady=20)

start_btn = tk.Button(btn_frame, text="Start", font=("Times New Roman", 15), command=start, bg='lightblue', fg='black')
start_btn.pack(side=tk.LEFT, padx=15)

stop_btn = tk.Button(btn_frame, text="Stop", font=("Times New Roman", 15), command=stop, bg='lightblue', fg='black', state=tk.DISABLED)
stop_btn.pack(side=tk.RIGHT, padx=15)


output_frame = tk.Frame(root)
output_frame.pack(pady=15)

output_box = tk.Text(output_frame, wrap=tk.WORD, font=("Times New Roman", 14, "italic"),bg='#e0f7fa', fg='#003366', height=25, width=50)
output_box.pack(padx=10, pady=10)


is_listening = False

root.mainloop()
