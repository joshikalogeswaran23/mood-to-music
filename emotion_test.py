from textblob import TextBlob


def detect_emotion(text):

    text_lower = text.lower()

    # Emotion keywords
    emotion_keywords = {
        "Stressed": [
            "stress", "stressed", "nervous", "exam",
            "pressure", "worried", "worry", "anxious",
            "anxiety", "tension", "deadline"
        ],

        "Sad": [
            "sad", "cry", "crying", "lonely",
            "depressed", "heartbroken", "upset",
            "unhappy", "terrible"
        ],

        "Angry": [
            "angry", "anger", "furious",
            "hate", "annoyed", "irritated",
            "frustrated", "mad"
        ],

        "Happy": [
            "happy", "wonderful", "great",
            "amazing", "joy", "joyful",
            "good", "fantastic", "love"
        ],

        "Excited": [
            "excited", "thrilled", "awesome",
            "can't wait", "looking forward"
        ],

        "Calm": [
            "calm", "peaceful", "relaxed",
            "relax", "peace", "comfortable"
        ],

        "Tired": [
            "tired", "exhausted", "sleepy",
            "fatigue", "drained"
        ]
    }

    # Find matching emotions
    detected_emotions = []

    for emotion, keywords in emotion_keywords.items():

        for keyword in keywords:

            if keyword in text_lower:
                detected_emotions.append(emotion)
                break

    # If an emotion keyword is found
    if detected_emotions:

        emotion = detected_emotions[0]

        # Calculate intensity
        intensity = 60

        # Strong words increase intensity
        strong_words = [
            "very",
            "extremely",
            "really",
            "so",
            "terribly",
            "completely"
        ]

        for word in strong_words:
            if word in text_lower:
                intensity += 10

        intensity = min(intensity, 100)

        confidence = min(intensity + 20, 99)

        return emotion, intensity, confidence

    # Otherwise use TextBlob
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity >= 0.6:
        emotion = "Happy"

    elif polarity >= 0.2:
        emotion = "Positive"

    elif polarity <= -0.6:
        emotion = "Sad"

    elif polarity <= -0.2:
        emotion = "Negative"

    else:
        emotion = "Neutral"

    intensity = round(abs(polarity) * 100, 2)

    confidence = 60

    return emotion, intensity, confidence


# Get user input
text = input("Tell me about your day: ")

emotion, intensity, confidence = detect_emotion(text)


print("\n🧠 AI Emotion Analysis")
print("-------------------------")

print("Emotion:", emotion)
print("Intensity:", intensity, "%")
print("Confidence:", confidence, "%")