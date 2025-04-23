# TASK-1 TEXT SUMMARIZATION TOOL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: Kapadia Jay Pareshbhai

*INTERN ID*: C0DF298

*DOMAIN*: Artificial Intelligence Markup Language.

*DURATION*: 4 WEEEKS

*MENTOR*: NEELA SANTOSH

# TEXT SUMMARIZATION TOOL 

In today’s fast-paced digital world, we are constantly surrounded by vast amounts of online content. Reading lengthy articles, blogs, or reports can be time-consuming and overwhelming. To address this challenge, I developed an Article Summarizer using Python, designed to condense long articles into short, meaningful summaries while preserving the core message.

**Text Summarizer** is a Python and Tkinter desktop application that enables users to create brief summaries of lengthy texts or articles with the help of a robust pre-trained transformer model. It has a clean and responsive GUI, adjustable summary lengths, real-time word count monitoring, and seamless performance due to threading.

---

## Features

- **Modern GUI:** Developed with Tkinter and themed with a dark elegant scheme for readability and beauty.
- **Text Summarization:** Employs Hugging Face's `transformers` pipeline utilizing the `distilbart-cnn-12-6` model for quality text summarization.
- **Live Word Count:** Updates in real time when you type or paste content.
- **Customizable Summary Length:** Quickly configure the length of the produced summary using a horizontal slider.
- **Multithreaded Processing:** Maintains the GUI interactive while producing summaries in the background.
- **Clear Button:** Clears both input and output sections instantly with one click.

---

## Powered By

- [Transformers (Hugging Face)](https://huggingface.co/transformers/)
- [Torch (PyTorch)](https://pytorch.org/)
- [NLTK (Natural Language Toolkit)](https://www.nltk.org/)

---

## How It Works

1. Opens a Tkinter-based desktop application.
2. Copy and paste or type the content you wish to summarize into the left pane.
3. Use the slider to specify the maximum number of words for your summary.
4. Click "⚡ Summarize" to create the summary based on the transformer model.
5. The result is displayed on the right, overwriting the loading text.
6. Use "Clear" to clear the application.

---

##  GUI Layout

- **Top container:** Input area for text with a word count meter.
- **bottom container:** Where the generated summary is displayed.
- **Bottom Panel:** Has action buttons to summarize and clear.
- **Slider Control:** Placed at the bottom of the panels to control summary length.

---

## ⚠️ Notes

- This is designed for short to medium-length texts (less than 1024 tokens) because of model limitations.
- Internet connection is needed on first use to download the model.
- It's optimized for English text input.

##  OUTPUT:-

![Image](https://github.com/user-attachments/assets/b71a3ecb-fa51-4b3e-9c2a-8210da968517)

