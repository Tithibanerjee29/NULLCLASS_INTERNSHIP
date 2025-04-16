# Step 1: Import Required Libraries
from transformers import pipeline

# Step 2: Load Sentiment Analysis Pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Step 3: Define Sentiment-Based Response Logic
def generate_response(user_input):
    result = sentiment_pipeline(user_input)[0]
    sentiment = result['label']
    confidence = round(result['score'] * 100, 2)

    if sentiment == "POSITIVE":
        return f"😊 I'm really glad to hear that! (Confidence: {confidence}%) Is there anything else I can help with?"
    elif sentiment == "NEGATIVE":
        return f"🙁 I'm sorry to hear that. (Confidence: {confidence}%) Let’s work on making this better for you."
    else:
        return f"😐 Got it. (Confidence: {confidence}%) Let me know how I can assist further."

# Step 4: CLI Chatbot Loop
if __name__ == "__main__":
    print("🤖 Sentiment-Aware Chatbot is online! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Stay positive! ✨")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)