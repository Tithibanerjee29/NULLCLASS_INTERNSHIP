import os
import requests
from transformers import pipeline
from PIL import Image
import matplotlib.pyplot as plt

# Set Google Cloud credential path if needed (for advanced vision tasks)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_google_credentials.json"

# Your Gemini API key for image generation
gemini_api_key = "YOUR API KEY"  # Replace with your actual Gemini API key

# Available models for text generation
models = {
    "Llama": "meta-llama/Llama-3.1-8B",
    "BLOOM": "bigscience/bloom-7b1",
    "Falcon": "tiiuae/falcon-7b"
}

# Function to generate text-based articles
def generate_article(prompt, model_name):
    """
    Generates an article based on the prompt and model.
    """
    try:
        generator = pipeline("text-generation", model=model_name)
        response = generator(prompt, max_length=512, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        return f"Error generating text: {str(e)}"

# Function to generate an image from a text description (using Gemini API)
def generate_image_from_text(text_description):
    """
    Generate an image from a description using the Gemini API.
    """
    try:
        api_url = "YOUR API KEY"  # Replace with actual Gemini API endpoint
        headers = {
            "Authorization": f"Bearer {gemini_api_key}",
            "Content-Type": "application/json",
        }
        payload = {"description": text_description}
        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 200:
            image_url = response.json().get("image_url")
            return image_url
        else:
            return f"Image generation failed. Status code: {response.status_code}"
    except Exception as e:
        return f"Error generating image: {str(e)}"

# Function to process an uploaded image and perform analysis (using Pillow and Matplotlib for display)
def process_image(image_path):
    """
    Process an uploaded image and display it.
    """
    try:
        with Image.open(image_path) as img:
            img.show()
            return "Image processed successfully!"
    except Exception as e:
        return f"Error processing image: {str(e)}"

# Main chatbot function to interact with the user
def chatbot():
    """
    Interactive chatbot interface for article generation and image processing.
    """
    print("🤖 Welcome to the Multi-Modal Chatbot!")

    while True:
        print("\n📌 Enter 'text' to input a text query, 'image' to upload an image, or 'exit' to quit:")
        input_type = input("Choose input type: ").lower()
        
        if input_type == "exit":
            print("👋 Exiting the chatbot.")
            break
        
        if input_type == "text":
            prompt = input("📝 Enter a topic for the article: ")
            print("Choose a model: 1) Llama 3.1  2) BLOOM  3) Falcon")
            model_choice = input("Enter model number: ")
            model_key = {"1": "Llama", "2": "BLOOM", "3": "Falcon"}.get(model_choice)
            
            if model_key:
                model_name = models[model_key]
                article = generate_article(prompt, model_name)
                print(f"\n📰 Generated Article:\n{article}")
            else:
                print("⚠️ Invalid model choice. Try again.")
        
        elif input_type == "image":
            image_path = input("📂 Enter the image file path: ")
            image_response = process_image(image_path)
            print(image_response)
            
            text_for_image = input("🎨 Enter a text description to generate an image: ")
            image_url = generate_image_from_text(text_for_image)
            print(f"🖼️ Generated Image URL: {image_url}")
        else:
            print("⚠️ Invalid input type. Please choose 'text' or 'image'.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
