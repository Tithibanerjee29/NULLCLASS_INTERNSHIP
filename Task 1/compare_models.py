import time
from transformers import pipeline

# Available models (ensure these are downloaded or accessible via API)
models = {
    "GPT-2": "gpt2",
    "BLOOM": "bigscience/bloom-560m",
    "GPT-Neo": "EleutherAI/gpt-neo-1.3B"
}

# Function to generate article
def generate_article(prompt, model_name):
    try:
        generator = pipeline("text-generation", model=model_name, device=-1)
        response = generator(prompt, max_length=512, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        return f"Error generating text with {model_name}: {str(e)}"

# Function to compare models
def compare_models():
    prompt = "The impact of artificial intelligence on modern education"

    # Dictionary to store the performance of each model
    model_performance = {}

    for model_name, model_id in models.items():
        print(f"\nEvaluating model: {model_name}")
        start_time = time.time()  # Start timing the generation
        
        # Generate article with the current model
        generated_text = generate_article(prompt, model_id)
        
        end_time = time.time()  # End timing the generation
        generation_time = end_time - start_time
        
        # Store the result
        model_performance[model_name] = {
            "generated_text": generated_text,
            "generation_time": generation_time
        }
        
        print(f"Model: {model_name}")
        print(f"Time taken: {generation_time:.2f} seconds")
        print(f"Generated Article:\n{generated_text[:300]}...")  # Show first 300 characters of the article

    # Save the performance report to a text file
    with open("comparison_report.txt", "w") as file:
        for model_name, performance in model_performance.items():
            file.write(f"Model: {model_name}\n")
            file.write(f"Generation Time: {performance['generation_time']:.2f} seconds\n")
            file.write(f"Generated Article (First 300 chars):\n{performance['generated_text'][:300]}...\n\n")
    
    print("\nComparison report saved to comparison_report.txt")

if __name__ == "__main__":
    compare_models()
