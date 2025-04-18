# 🤖 Multi-Modal Chatbot (Text + Image)

This is a Python-based Multi-Modal Chatbot that can:
- Generate text articles using large language models (LLMs) like LLaMA, BLOOM, and Falcon.
- Generate images from text descriptions using the Gemini AI API.
- Process uploaded images using Pillow (or extendable to Google Vision API).

---

## 📁 Folder Structure
multi-modal-chatbot/
├── article_generator/       # Uses LLaMA, BLOOM, Falcon for text generation
├── image_generator/         # Uses Gemini API for image generation
├── image_analyzer/          # Analyze uploaded images (Pillow-based)
├── chatbot.py               # Main chatbot logic combining text and image
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
└── assets/                  # Sample images / input files



---

## 🚀 Features

- Text generation using popular transformer models.
- Image generation from a text prompt (via Gemini AI API).
- Display or analyze uploaded images.
- Interactive command-line chatbot interface.

---
🧪 Technologies Used
Python 3.8+

Hugging Face Transformers (LLMs)

Google Gemini API (Vision & Image generation)

Pillow (for image handling)

Command-line interface

📌 Notes
Make sure to configure Gemini API keys (if required).

Some models like LLaMA may require additional setup or use via Hugging Face Hub.

This chatbot is extendable with GUI frameworks like Streamlit or Gradio.


## 📦 Installation Steps

1. Clone this repository or download the project folder.
2. Open a terminal inside the project folder.
3. Install dependencies:

```bash
pip install -r requirements.txt

🛠️ How to Run
python chatbot.py
You will be able to:

Enter a text prompt for article generation.

Upload an image and get a description.

Enter a description to generate an image.
