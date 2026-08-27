from transformers import pipeline

print("Loading AI emotion model...")

classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

print("Model loaded successfully!")

text = input("\nTell me about your day: ")

result = classifier(text)[0]

emotion = result["label"]
confidence = result["score"] * 100

print("\n🧠 AI Emotion Analysis")
print("-------------------------")
print("Emotion:", emotion)
print("Confidence:", round(confidence, 2), "%")