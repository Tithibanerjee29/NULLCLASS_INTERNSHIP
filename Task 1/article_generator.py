import sys

try:
    from transformers import pipeline
except ModuleNotFoundError:
    print("Error: The 'transformers' module is not installed. Please install it using 'pip install transformers'")
    def chatbot():
        print("Exiting due to missing dependencies.")
        return
    
    def generate_article(prompt, model_name):
        return ""
    
    if __name__ == "__main__":
        chatbot()
    
# Available models (ensure these are downloaded or accessible via API)
models = {
    "Llama": "meta-llama/Llama-3.1-8B",
    "BLOOM": "bigscience/bloom-7b1",
    "Falcon": "tiiuae/falcon-7b"
}

def generate_article(prompt, model_name):
    try:
        generator = pipeline("text-generation", model=model_name)
        response = generator(prompt, max_length=512, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        return f"Error generating text: {str(e)}"

def chatbot():
    print("Welcome to the Article Generator Chatbot!")
    
    try:
        while True:
            print("Enter a topic for the article (or type 'exit' to quit):")
            try:
                prompt = sys.stdin.readline().strip()
            except ValueError:
                print("Error: Unable to read input. Exiting chatbot.")
                return
            
            if not prompt or prompt.lower() == "exit":
                return
            
            print("Select a model: 1) Llama 3.1  2) BLOOM  3) Falcon 180B")
            print("Enter model number:")
            
            try:
                choice = sys.stdin.readline().strip()
            except ValueError:
                print("Error: Unable to read input. Exiting chatbot.")
                return
            
            model_key = {"1": "Llama", "2": "BLOOM", "3": "Falcon"}.get(choice)
            if not model_key:
                print("Invalid choice. Try again.")
                continue
            
            model_name = models[model_key]
            article = generate_article(prompt, model_name)
            print("\nGenerated Article:")
            print(article)
    except ValueError:
        print("I/O error encountered. Please ensure input is supported in this environment.")

if __name__ == "__main__":
    chatbot()
