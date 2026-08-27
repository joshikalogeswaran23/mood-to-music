# 🎵 MoodLens AI

An AI-powered web application that understands the user's emotions and recommends music based on how they feel and how they want to feel.

## 📌 About the Project

**MoodLens AI** is an emotion-aware music recommendation application designed to make music discovery more personalized and meaningful.

Instead of simply asking users to select a mood, MoodLens AI uses Artificial Intelligence to analyze the user's natural-language input, detect their current emotion, and help them choose the mood they want to reach.

The application creates an interactive **Mood Journey**:

```text
🧠 Current Emotion
        ↓
🎯 Desired Mood
        ↓
🎵 Personalized Music
        ↓
❤️ User Feedback
        ↓
📊 Mood Journey

For example, if a user says:

"I have an exam tomorrow and I am really nervous."

The AI analyzes the sentence and identifies the user's emotional state. The user can then choose a desired mood such as 😌 Calm or 🎯 Focus / Study, and the application recommends suitable music.

✨ Features
🧠 AI-based emotion detection from natural-language text
🎭 Detects emotions such as Happy, Sad, Angry, Stressed, Excited and Neutral
🎯 Allows users to choose their desired mood
🎵 Personalized music recommendations
🇮🇳 Tamil and 🌎 international song recommendations
🧭 Automatically moves to the next step after completing a stage
🖱️ Allows users to manually navigate to any section
📊 Mood Journey and AI confidence tracking
❤️ User feedback system
🎧 Direct access to recommended songs through YouTube
💻 Simple and interactive web interface
🌐 Publicly deployed web application
🎯 Mood Categories

The application provides music recommendations for different emotional goals:

😌 Calm
😊 Happy
⚡ Energetic
🎯 Focus / Study
💪 Motivation
😴 Sleep
❤️ Romantic
🎉 Party / Fun
🤖 AI Emotion Detection

MoodLens AI uses a Transformer-based emotion classification model from Hugging Face:

j-hartmann/emotion-english-distilroberta-base

The model analyzes the user's natural-language input and identifies the underlying emotion.

Example:

User Input:
"I am extremely angry about what happened."

        ↓

🤖 AI Emotion Analysis

        ↓

😡 Detected Emotion: Angry

        ↓

🎯 Choose Desired Mood

😌 Calm
😊 Happy
⚡ Energetic
💪 Motivation
...
🧭 Mood Journey

The application follows an interactive step-by-step journey:

🧠 Analyze Mood
       ↓
🤖 AI Emotion Detection
       ↓
🎯 Choose Mood Goal
       ↓
🎵 Personalized Music
       ↓
❤️ User Feedback
       ↓
📊 Mood Journey

After completing a step, the application automatically moves to the next stage.

Users can also manually select any section from the navigation menu.

🎵 Music Recommendations

The application contains curated songs for different moods.

😌 Calm
🎵 Swasame Swasame
🎵 Amsham
🎵 The Life of Ram
🎵 Golden Hour
🎵 Until I Found You
😊 Happy
🎵 Megham Karukatha
🎵 Vaathi Coming
🎵 Pavazha Malli
🎵 On Top of the World
🎵 Best Day of My Life
⚡ Energetic
🎵 Thalapathy Kacheri
🎵 Ranjithame
🎵 Vaathi Coming
🎵 Levitating
🎵 Uptown Funk
🎯 Focus / Study
🎵 The Life of Ram
🎵 New York Nagaram
🎵 Experience
🎵 Time
🎵 All the Stars
💪 Motivation
🎵 Mazhaithuli Sangamam
🎵 Aalaporan Thamizhan
🎵 Raga of Revenge
🎵 Unstoppable
🎵 Believer
😴 Sleep
🎵 Maya Nadhi
🎵 Poongatrile
🎵 Nenjukkul Peidhidum
🎵 Weightless
🎵 Peaceful Piano
❤️ Romantic
🎵 Vaseegara
🎵 Anbil Avan
🎵 Kadhal Sadugudu
🎵 Perfect
🎵 A Thousand Years
🎉 Party / Fun
🎵 Aura 10/10
🎵 Kanimaa
🎵 Oorum Blood
🎵 Cruel Summer
🎵 As It Was
🛠️ Technologies Used
Python
Streamlit
Hugging Face Transformers
PyTorch
Pandas
YouTube
Git & GitHub
Streamlit Cloud
📂 Project Structure
mood-to-music/
│
├── app.py
├── emotion_test.py
├── real_emotion_test.py
├── requirements.txt
├── README.md
└── .gitignore

The venv/ folder is used only for local development and should not be uploaded to GitHub.

🚀 How to Run the Project
1. Clone the repository
git clone https://github.com/joshikalogeswaran23/mood-to-music.git
2. Open the project folder
cd mood-to-music
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows PowerShell:

venv\Scripts\Activate.ps1
5. Install the required dependencies
pip install -r requirements.txt
6. Run the application
streamlit run app.py
7. Open the application

Streamlit will provide a local URL, usually:

http://localhost:8501
🌐 Live Application

The project is deployed using Streamlit Cloud.

Live App:

https://mood-to-music.streamlit.app/

💻 GitHub Repository

The complete source code is available on GitHub:

https://github.com/joshikalogeswaran23/mood-to-music

🎯 How It Works
User
  ↓
Describes Current Feelings
  ↓
AI Emotion Detection
  ↓
Current Emotion Identified
  ↓
User Selects Desired Mood
  ↓
Personalized Songs Recommended
  ↓
User Listens
  ↓
Provides Feedback
  ↓
Mood Journey Updated
💡 What Makes MoodLens AI Different?

Traditional music recommendation systems generally work like this:

Current Mood
     ↓
Music

MoodLens AI follows a more personalized approach:

Current Emotion
       ↓
Desired Emotion
       ↓
Personalized Music
       ↓
User Feedback
       ↓
Mood Journey
⭐ Core Innovation

Don't just detect how the user feels — help them choose how they want to feel.

The main focus of MoodLens AI is emotional transformation, not just emotional detection.

📊 Mood Journey Example

A user's journey can look like:

Session 01

😰 Stressed
     ↓
😌 Calm
     ↓
🎵 Personalized Playlist
     ↓
😊 Much Better

The application can track:

🧠 Current emotion
🎯 Target mood
🤖 AI confidence
🎵 Music category
❤️ User feedback
📊 Previous mood sessions
❤️ User Feedback

After listening to the recommended music, users can provide feedback.

Available options:

😊 Much better
🙂 Slightly better
😐 No change
😔 Worse

The application uses the feedback to calculate a positive response rate during the current session.

🎯 Project Objectives
🧠 Detect emotions using AI
📝 Understand natural-language input
🎯 Allow users to select a desired emotional state
🎵 Recommend suitable music
🧭 Create an automatic mood journey
🖱️ Provide manual navigation
❤️ Collect user feedback
📊 Track mood journeys
🌐 Provide an accessible web application
🔮 Future Improvements
🎤 Add voice-based emotion detection
📷 Add facial emotion recognition
🧠 Combine text, voice and facial emotions
🎧 Integrate Spotify API
🎶 Automatically create personalized playlists
📊 Add long-term mood analytics
❤️ Improve recommendations using user feedback
🤖 Add AI explanations for why a song was recommended
📱 Improve mobile responsiveness
☁️ Expand the application for large-scale deployment
🏆 Project Highlights
🧠 AI-Powered
       +
🎯 Goal-Oriented
       +
🎵 Personalized
       +
🧭 Interactive
       +
❤️ Feedback-Driven
       +
📊 Data-Aware
       =
🎵 MoodLens AI
👩‍💻 Author

Joshika Logeswaran

GitHub: https://github.com/joshikalogeswaran23

⭐ Support the Project

If you find MoodLens AI interesting, consider giving the repository a ⭐ on GitHub.
