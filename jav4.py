from tkinter import *
import google.generativeai as genai
import pyttsx3  # For offline English voice output

# ------------------- AI Setup -------------------
API_KEY = "*******************************************"  # Replace with your Gemini API key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# Create chat session ONCE
chat = model.start_chat()

# ------------------- Voice Function -------------------
def speak(text):
    """Create a fresh engine each time to avoid blocking"""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change index for male/female
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ------------------- Upload Function -------------------
def upload(event=None):
    user_msg = txt.get().strip()
    if not user_msg:
        return
    
    # Send to AI
    response = chat.send_message(user_msg)


    # Show response in Listbox
    chat_list.insert(END, f"You: {user_msg}")
    chat_list.insert(END, f"AI: {response.text}")
    chat_list.see(END)  # Auto scroll to latest message

    # Voice output
    speak(response.text)


    # Clear input box
    entry.delete(0, END)

# ------------------- Tkinter Setup -------------------
win = Tk()
win.title("My AI Chatbot")
win.geometry("600x500")

txt = StringVar()

Label(win, text="MY CHATBOT AI", fg="green",
      font=("Times New Roman", 30)).pack(padx=20, pady=10)

# Input field
entry = Entry(win, textvariable=txt, fg="orange",
              font=("Times New Roman", 20), width=40)
entry.pack(padx=10, pady=10)

# Bind Enter key
entry.bind("<Return>", upload)

# Send button
Button(win, text="   🠉   ", fg="green",
       font=("Times New Roman", 18), command=upload).pack(pady=10)


# Chat history list
chat_list = Listbox(win, width=70, height=20,fg="green",font=("Times New Roman", 12))
chat_list.pack(padx=10, pady=10)



win.mainloop()

