from googletrans import Translator
from tkinter import *

def translate_text():
    amharic_text = amharic_input.get("1.0", END).strip()
    translator = Translator()
    try:
        translation = translator.translate(amharic_text, src='am', dest='en')
        english_output.delete("1.0", END)
        english_output.insert(END, translation.text)
    except Exception as e:
        english_output.delete("1.0", END)
        english_output.insert(END, f"Error: {str(e)}")

root = Tk()
root.title("Amharic to English Translator")
root.geometry("500x300")

Label(root, text="Enter Amharic Text:", font=("Arial", 14)).pack(pady=10)
amharic_input = Text(root, height=5, width=50)
amharic_input.pack(pady=5)

Button(root, text="Translate", command=translate_text, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

Label(root, text="English Translation:", font=("Arial", 14)).pack(pady=10)
english_output = Text(root, height=5, width=50)
english_output.pack(pady=5)

root.mainloop()
