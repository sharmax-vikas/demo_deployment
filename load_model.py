
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
# Load saved model and tokenizer
saved_path = "./models"
tokenizer = AutoTokenizer.from_pretrained(saved_path)
model = AutoModelForSequenceClassification.from_pretrained(saved_path)

def sent(text):
    # Use tokenizer to process text
    t = tokenizer(text, padding="max_length", truncation=True, max_length=512)  # Pad/truncate to max_length

    # Use model to predict sentiment
    input_ids = t["input_ids"]
    attention_mask = t["attention_mask"]

    input_ids = torch.tensor(input_ids)
    attention_mask = torch.tensor(attention_mask)

    # Make prediction
    output = model(input_ids.unsqueeze(0), attention_mask=attention_mask.unsqueeze(0)) # Add batch dimension
    # Get sentiment scores
    sentiment_scores = output.logits
    # Apply softmax to get probabilities
    sentiment_probabilities = F.softmax(sentiment_scores, dim=1)

    # Determine sentiment (0: negative, 1: positive)
    sentiment = torch.argmax(sentiment_probabilities)

    # Calculate sentiment percentages
    negative_percentage = round(sentiment_probabilities[0][0].item() * 100, 2)
    positive_percentage = round(sentiment_probabilities[0][1].item() * 100, 2)

    print(f"Negative Sentiment: {negative_percentage}%")
    print(f"Positive Sentiment: {positive_percentage}%")
    return int(sentiment)

