import customtkinter as ctk
import langid
import pycountry
import pyttsx3
import pyperclip
import wikipedia
from googletrans import Translator
import tkinter as tk
from tkinter import messagebox, filedialog
import os

# Theme
current_theme = "dark"

def detect_language():
    text = text_input.get("1.0", "end-1c").strip()
    if text:
        lang_code, confidence = langid.classify(text)
        language_info = pycountry.languages.get(alpha_2=lang_code)

        if language_info:
            language_name = language_info.name
            country_list = [country.name for country in pycountry.countries if lang_code in country.alpha_2.lower()]
            countries_spoken = ", ".join(country_list) if country_list else "Multiple Countries"

            result_label.configure(text=f"🌍 Language: {language_name}\n📍 Spoken In: {countries_spoken}")
        else:
            result_label.configure(text="❌ Language not found!")
    else:
        result_label.configure(text="⚠️ Please enter some text!")

# Function to auto-detect while typing
def auto_detect(event=None):
    detect_language()

# Function to translate text
def translate_text():
    text = text_input.get("1.0", "end-1c").strip()
    if text:
        translator = Translator()
        translation = translator.translate(text, dest="en").text
        result_label.configure(text=f"🗣️ Translation: {translation}")

# Function to pronounce detected text
def speak_language():
    text = text_input.get("1.0", "end-1c").strip()
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def copy_to_clipboard():
    pyperclip.copy(result_label.cget("text"))

#To get AI-powered language facts
def get_language_facts():
    lang_code = langid.classify(text_input.get("1.0", "end-1c"))[0]
    try:
        fact = wikipedia.summary(lang_code, sentences=1)
        result_label.configure(text=f"📚 Fact: {fact}")
    except:
        result_label.configure(text="No facts found.")

# "Languages A-Z"
def open_language_file():
    file_path = "lang.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            messagebox.showinfo("Languages A-Z", content)
    except FileNotFoundError:
        messagebox.showerror("Error", "lang.txt file not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# dark/light mode
def toggle_theme():
    global current_theme
    if current_theme == "dark":
        ctk.set_appearance_mode("light")
        current_theme = "light"
    else:
        ctk.set_appearance_mode("dark")
        current_theme = "dark"

def show_about():
    messagebox.showinfo("About", 
                        "🌍 Language Detection App\n📌 Created with Python & CustomTkinter\n🚀 Features: Auto-detect, Translation, TTS, AI Facts"

                        "\n🔍 Detect: Detects language & country"

                        "\n👨‍💻 Developed by: Mohammed Razin CR\n")

# Function to exit app
def exit_app():
    app.destroy()

app = ctk.CTk()
app.title("Language Detector")
app.geometry("550x600")

# Heading Label
title_label = ctk.CTkLabel(app, text="🌍 Language Detection", font=("Arial", 22, "bold"))
title_label.pack(pady=20)

# Textbox for input
text_input = ctk.CTkTextbox(app, width=400, height=100, font=("Arial", 14))
text_input.pack(pady=10)
text_input.bind("<KeyRelease>", auto_detect)  # Auto-detect on typing

# Detect Button
detect_button = ctk.CTkButton(app, text="🔍 Detect", command=detect_language, font=("Arial", 16))
detect_button.pack(pady=10)

# Result Label
result_label = ctk.CTkLabel(app, text="", font=("Arial", 16), wraplength=400)
result_label.pack(pady=20)
buttons_frame = ctk.CTkFrame(app)
buttons_frame.pack(pady=10)

translate_button = ctk.CTkButton(buttons_frame, text="🔄 Translate", command=translate_text, font=("Arial", 14), width=130)
translate_button.grid(row=0, column=0, padx=5, pady=5)

speak_button = ctk.CTkButton(buttons_frame, text="🔊 Pronounce", command=speak_language, font=("Arial", 14), width=130)
speak_button.grid(row=0, column=1, padx=5, pady=5)

copy_button = ctk.CTkButton(buttons_frame, text="📋 Copy", command=copy_to_clipboard, font=("Arial", 14), width=130)
copy_button.grid(row=1, column=0, padx=5, pady=5)

facts_button = ctk.CTkButton(buttons_frame, text="📚 Language Facts", command=get_language_facts, font=("Arial", 14), width=130)
facts_button.grid(row=1, column=1, padx=5, pady=5)

# Theme Toggle & Show All Languages
extra_buttons_frame = ctk.CTkFrame(app)
extra_buttons_frame.pack(pady=10)

theme_button = ctk.CTkButton(extra_buttons_frame, text="🌙/☀️ Toggle Theme", command=toggle_theme, font=("Arial", 14), width=200)
theme_button.grid(row=0, column=0, padx=5, pady=5)

languages_button = ctk.CTkButton(extra_buttons_frame, text="🌎 Languages A-Z", command=open_language_file, font=("Arial", 14), width=200)
languages_button.grid(row=0, column=1, padx=5, pady=5)

# About and Exit Buttons
footer_frame = ctk.CTkFrame(app)
footer_frame.pack(pady=10)

about_button = ctk.CTkButton(footer_frame, text="ℹ️ About", command=show_about, font=("Arial", 14), width=130)
about_button.grid(row=0, column=0, padx=5, pady=5)

exit_button = ctk.CTkButton(footer_frame, text="❌ Exit", command=exit_app, font=("Arial", 14), width=130)
exit_button.grid(row=0, column=1, padx=5, pady=5)
app.mainloop()
