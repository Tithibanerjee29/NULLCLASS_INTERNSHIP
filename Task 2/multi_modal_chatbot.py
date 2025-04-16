import sys
import os
from transformers import pipeline
from PIL import Image
import requests

# Set up Google Cloud authentication (for API use)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_google_credentials.json"

# Available models for text generation
models = {
    "Llama": "meta-llama/Llama-3.1-8B",
    "BLOOM": "bigscience/bloom-7b1",
    "Falcon": "tiiuae/falcon-7b"
}

# Function to generate text-based articles
def generate_article(prompt, model_name):
    try:
        generator = pipeline("text-generation", model=model_name)
        response = generator(prompt, max_length=512, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        return f"Error generating text: {str(e)}"

# Function to generate an image from a text description (using Gemini API)
def generate_image_from_text(text_description):
    try:
        api_url = "https://api.gemini.ai/v1/generate_image"  # Replace with actual Gemini API URL
        headers = {
            "Authorization": "Bearer YOUR_API_KEY",  # Replace with your Gemini API key
            "Content-Type": "application/json",
        }
        payload = {"description": text_description}
        
        # Send request to Gemini API
        response = requests.post(api_url, headers=headers, json=payload)
        
        if response.status_code == 200:
            image_url = response.json().get("image_url")
            return image_url
        else:
            return "Error generating image."
    except Exception as e:
        return f"Error generating image: {str(e)}"

# Function to process an uploaded image and perform analysis (using Pillow)
def process_image(image_path):
    try:
        with Image.open(image_path) as img:
            img.show()  # This will display the image
            # Further processing like using Google Vision API or any other model can be done here
            return "Image processed successfully!"
    except Exception as e:
        return f"Error processing image: {str(e)}"

# Main chatbot function to interact with the user
def chatbot():
    print("Welcome to the Multi-Modal Chatbot!")

    while True:
        print("Enter 'text' to input a text query, 'image' to upload an image, or 'exit' to quit:")
        input_type = input("Choose input type: ").lower()
        
        if input_type == "exit":
            print("Exiting the chatbot.")
            break
        
        if input_type == "text":
            prompt = input("Enter a topic for the article: ")
            print("Select a model: 1) Llama 3.1  2) BLOOM  3) Falcon 180B")
            model_choice = input("Enter model number: ")
            model_key = {"1": "Llama", "2": "BLOOM", "3": "Falcon"}.get(model_choice)
            
            if model_key:
                model_name = models[model_key]
                article = generate_article(prompt, model_name)
                print(f"\nGenerated Article: {article}")
            else:
                print("Invalid model choice. Try again.")
        
        elif input_type == "image":
            image_path = input("Enter the image file path: ")
            image_response = process_image(image_path)
            print(image_response)
            # Optionally generate an image from text
            text_for_image = input("Enter a text description to generate an image: ")
            image_url = generate_image_from_text(text_for_image)
            print(f"Generated Image URL: {image_url}")
        else:
            print("Invalid input type. Please choose 'text' or 'image'.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
