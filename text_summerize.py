import subprocess
import sys
import nltk
import tkinter as tk
from tkinter import scrolledtext, messagebox
from transformers import pipeline
import threading

# Install required packages
packages = ["transformers", "torch", "nltk"]
for pkg in packages:
    try:
        __import__(pkg)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

# Ensure punkt tokenizer is downloaded
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

# Load summarization model with explicit model name
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# --- GUI Setup ---
app = tk.Tk()
app.title("📝 Elegant Summarizer")
app.geometry("1200x700+100+50")
app.resizable(True, True)

# Color Theme
BACKGROUND_COLOR = "#2c2c2e"  # elegant dark grey
TEXT_COLOR = "#ffffff"         # white text
INPUT_OUTPUT_BG = "#3a3a3c"    # slightly lighter for contrast

FONT_TITLE = ("Segoe UI", 26, "bold")
FONT_LABEL = ("Segoe UI", 14)
FONT_TEXT = ("Consolas", 12)

# --- Layout Containers ---
left_frame = tk.Frame(app, bg=BACKGROUND_COLOR)
left_frame.place(relx=0.02, rely=0.1, relwidth=0.46, relheight=0.65)

right_frame = tk.Frame(app, bg=BACKGROUND_COLOR)
right_frame.place(relx=0.52, rely=0.1, relwidth=0.46, relheight=0.65)

# Header
header = tk.Label(app, text="📝 Elegant Summarizer", font=FONT_TITLE, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
header.place(relx=0.5, rely=0.02, anchor="n")

# Word Count
token_var = tk.StringVar(value="Words: 0")
token_label = tk.Label(left_frame, textvariable=token_var, fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=FONT_LABEL)
token_label.pack(anchor="ne", padx=10, pady=10)

# Input
tk.Label(left_frame, text="📋 Input Text", font=FONT_LABEL, fg=TEXT_COLOR, bg=BACKGROUND_COLOR).pack(anchor="w", padx=10)
input_area = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, font=FONT_TEXT,
                                       bg=INPUT_OUTPUT_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                                       highlightbackground=TEXT_COLOR, highlightcolor=TEXT_COLOR)
input_area.pack(padx=10, pady=5, fill="both", expand=True)

# Output
tk.Label(right_frame, text="📑 Summary", font=FONT_LABEL, fg=TEXT_COLOR, bg=BACKGROUND_COLOR).pack(anchor="w", padx=10)
output_area = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, font=FONT_TEXT,
                                        bg=INPUT_OUTPUT_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                                        highlightbackground=TEXT_COLOR, highlightcolor=TEXT_COLOR)
output_area.pack(padx=10, pady=5, fill="both", expand=True)

# Summary Length
slider_label = tk.Label(app, text="📏 Summary Length", font=FONT_LABEL, fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
slider_label.place(relx=0.5, rely=0.77, anchor="center")
length_slider = tk.Scale(app, from_=50, to=300, orient=tk.HORIZONTAL, length=300, font=("Segoe UI", 10),
                         bg=BACKGROUND_COLOR, fg=TEXT_COLOR, troughcolor="#5a5a5e", highlightbackground=BACKGROUND_COLOR)
length_slider.set(120)
length_slider.place(relx=0.5, rely=0.82, anchor="center")

# Functionalities
def update_word_count(event=None):
    text = input_area.get("1.0", tk.END)
    word_count = len(text.strip().split())
    token_var.set(f"Words: {word_count}")

input_area.bind("<KeyRelease>", update_word_count)

def summarize_text():
    text = input_area.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Missing Input", "Please enter some text.")
        return

    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, "⏳ Summarizing...")
    summarize_btn.config(state="disabled")

    def run_summary():
        try:
            max_len = length_slider.get()
            min_len = max(30, max_len // 2)
            summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
            output_area.delete("1.0", tk.END)
            output_area.insert(tk.END, summary[0]['summary_text'])
        except Exception as e:
            output_area.delete("1.0", tk.END)
            output_area.insert(tk.END, f"Error: {str(e)}")
        finally:
            summarize_btn.config(state="normal")

    threading.Thread(target=run_summary).start()

def clear_text():
    input_area.delete("1.0", tk.END)
    output_area.delete("1.0", tk.END)
    token_var.set("Words: 0")

# Buttons
btn_frame = tk.Frame(app, bg=BACKGROUND_COLOR)
btn_frame.place(relx=0.5, rely=0.93, anchor="center")

summarize_btn = tk.Button(btn_frame, text="⚡ Summarize", command=summarize_text,
                          font=FONT_LABEL, bg="#4a90e2", fg=TEXT_COLOR, padx=20, pady=10)
summarize_btn.pack(side="left", padx=20)

clear_btn = tk.Button(btn_frame, text="🧹 Clear", command=clear_text,
                      font=FONT_LABEL, bg="#e94e77", fg=TEXT_COLOR, padx=20, pady=10)
clear_btn.pack(side="left", padx=20)

# Start GUI
app.mainloop()