import streamlit as st
from transformers import pipeline
import pandas as pd


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="MoodLens AI",
    page_icon="🎵",
    layout="wide"
)


# ============================================================
# AI EMOTION MODEL
# ============================================================

@st.cache_resource
def load_emotion_model():

    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base"
    )


# ============================================================
# EMOTION DETECTION
# ============================================================

def detect_emotion(text):

    classifier = load_emotion_model()

    result = classifier(text)[0]

    model_emotion = result["label"]
    confidence = result["score"] * 100

    emotion_map = {

        "anger": "Angry",

        "disgust": "Angry",

        "fear": "Stressed",

        "joy": "Happy",

        "sadness": "Sad",

        "surprise": "Excited",

        "neutral": "Neutral"
    }

    emotion = emotion_map.get(
        model_emotion,
        "Neutral"
    )

    return emotion, confidence, model_emotion


# ============================================================
# EMOTION EMOJIS
# ============================================================

emotion_emojis = {

    "Happy": "😊",

    "Sad": "😢",

    "Stressed": "😰",

    "Angry": "😡",

    "Excited": "🤩",

    "Neutral": "😐",

    "Calm": "😌",

    "Energetic": "⚡",

    "Focus": "🎯",

    "Motivation": "💪",

    "Sleep": "😴",

    "Romantic": "❤️",

    "Party": "🎉"
}


# ============================================================
# CUSTOM TAMIL + ENGLISH MUSIC DATABASE
# ============================================================

songs = {


    # ========================================================
    # CALM
    # ========================================================

    "Calm": [

        {
            "name": "Swasame Swasame",
            "artist": "S. P. Balasubrahmanyam & Sadhana Sargam",
            "url": "https://www.youtube.com/results?search_query=Swasame+Swasame+Thenali"
        },

        {
            "name": "Amsham",
            "artist": "Aksomaniac, M.H.R, Bhumi & Circle Tone",
            "url": "https://www.youtube.com/results?search_query=Amsham+Aksomaniac"
        },

        {
            "name": "The Life of Ram",
            "artist": "Pradeep Kumar",
            "url": "https://www.youtube.com/results?search_query=The+Life+of+Ram+Pradeep+Kumar"
        },

        {
            "name": "Golden Hour",
            "artist": "JVKE",
            "url": "https://www.youtube.com/results?search_query=Golden+Hour+JVKE"
        },

        {
            "name": "Until I Found You",
            "artist": "Stephen Sanchez",
            "url": "https://www.youtube.com/results?search_query=Until+I+Found+You+Stephen+Sanchez"
        }

    ],


    # ========================================================
    # HAPPY
    # ========================================================

    "Happy": [

        {
            "name": "Megham Karukatha",
            "artist": "Dhanush",
            "url": "https://www.youtube.com/results?search_query=Megham+Karukatha+Dhanush"
        },

        {
            "name": "Vaathi Coming",
            "artist": "Anirudh Ravichander",
            "url": "https://www.youtube.com/results?search_query=Vaathi+Coming+Anirudh"
        },

        {
            "name": "Pavazha Malli",
            "artist": "Sai Abhyankkar, Shruti Haasan & Vivek",
            "url": "https://www.youtube.com/results?search_query=Pavazha+Malli+Sai+Abhyankkar"
        },

        {
            "name": "On Top of the World",
            "artist": "Imagine Dragons",
            "url": "https://www.youtube.com/results?search_query=On+Top+of+the+World+Imagine+Dragons"
        },

        {
            "name": "Best Day of My Life",
            "artist": "American Authors",
            "url": "https://www.youtube.com/results?search_query=Best+Day+of+My+Life+American+Authors"
        }

    ],


    # ========================================================
    # ENERGETIC
    # ========================================================

    "Energetic": [

        {
            "name": "Thalapathy Kacheri",
            "artist": "Anirudh Ravichander, Vijay & Arivu",
            "url": "https://www.youtube.com/results?search_query=Thalapathy+Kacheri+Anirudh+Vijay"
        },

        {
            "name": "Ranjithame",
            "artist": "Vijay & M. M. Manasi",
            "url": "https://www.youtube.com/results?search_query=Ranjithame+Vijay"
        },

        {
            "name": "Vaathi Coming",
            "artist": "Anirudh Ravichander",
            "url": "https://www.youtube.com/results?search_query=Vaathi+Coming+Anirudh"
        },

        {
            "name": "Levitating",
            "artist": "Dua Lipa",
            "url": "https://www.youtube.com/results?search_query=Levitating+Dua+Lipa"
        },

        {
            "name": "Uptown Funk",
            "artist": "Mark Ronson ft. Bruno Mars",
            "url": "https://www.youtube.com/results?search_query=Uptown+Funk+Mark+Ronson+Bruno+Mars"
        }

    ],


    # ========================================================
    # FOCUS / STUDY
    # ========================================================

    "Focus": [

        {
            "name": "The Life of Ram",
            "artist": "Pradeep Kumar",
            "url": "https://www.youtube.com/results?search_query=The+Life+of+Ram+Pradeep+Kumar"
        },

        {
            "name": "New York Nagaram",
            "artist": "A. R. Rahman",
            "url": "https://www.youtube.com/results?search_query=New+York+Nagaram+AR+Rahman"
        },

        {
            "name": "Experience",
            "artist": "Ludovico Einaudi",
            "url": "https://www.youtube.com/results?search_query=Experience+Ludovico+Einaudi"
        },

        {
            "name": "Time",
            "artist": "Hans Zimmer",
            "url": "https://www.youtube.com/results?search_query=Time+Hans+Zimmer"
        },

        {
            "name": "All the Stars",
            "artist": "Kendrick Lamar & SZA",
            "url": "https://www.youtube.com/results?search_query=All+the+Stars+Kendrick+Lamar+SZA"
        }

    ],


    # ========================================================
    # MOTIVATION
    # ========================================================

    "Motivation": [

        {
            "name": "Mazhaithuli",
            "artist": "Hariharan & M. S. Viswanathan",
            "url": "https://www.youtube.com/results?search_query=Mazhaithuli+Sangamam+Hariharan"
        },

        {
            "name": "Aalaporan Thamizhan",
            "artist": "A. R. Rahman",
            "url": "https://www.youtube.com/results?search_query=Aalaporan+Thamizhan+AR+Rahman"
        },

        {
            "name": "Raga of Revenge",
            "artist": "Anirudh Ravichander",
            "url": "https://www.youtube.com/results?search_query=Raga+of+Revenge+Anirudh"
        },

        {
            "name": "Unstoppable",
            "artist": "Sia",
            "url": "https://www.youtube.com/results?search_query=Unstoppable+Sia"
        },

        {
            "name": "Believer",
            "artist": "Imagine Dragons",
            "url": "https://www.youtube.com/results?search_query=Believer+Imagine+Dragons"
        }

    ],


    # ========================================================
    # SLEEP
    # ========================================================

    "Sleep": [

        {
            "name": "Maya Nadhi",
            "artist": "Ananthu, Pradeep Kumar & Swetha Mohan",
            "url": "https://www.youtube.com/results?search_query=Maya+Nadhi+Kabali"
        },

        {
            "name": "Poongatrile",
            "artist": "Unnikrishnan",
            "url": "https://www.youtube.com/results?search_query=Poongatrile+Unnikrishnan"
        },

        {
            "name": "Nenjukkul Peidhidum",
            "artist": "Hariharan",
            "url": "https://www.youtube.com/results?search_query=Nenjukkul+Peidhidum+Hariharan"
        },

        {
            "name": "Weightless",
            "artist": "Marconi Union",
            "url": "https://www.youtube.com/results?search_query=Weightless+Marconi+Union"
        },

        {
            "name": "Peaceful Piano",
            "artist": "Relaxing Music",
            "url": "https://www.youtube.com/results?search_query=Peaceful+Piano+Sleep+Music"
        }

    ],


    # ========================================================
    # ROMANTIC
    # ========================================================

    "Romantic": [

        {
            "name": "Vaseegara",
            "artist": "Bombay Jayashri",
            "url": "https://www.youtube.com/results?search_query=Vaseegara+Bombay+Jayashri"
        },

        {
            "name": "Anbil Avan",
            "artist": "Devan Ekambaram & Chinmayi",
            "url": "https://www.youtube.com/results?search_query=Anbil+Avan"
        },

        {
            "name": "Kadhal Sadugudu",
            "artist": "S. P. B. Charan",
            "url": "https://www.youtube.com/results?search_query=Kadhal+Sadugudu"
        },

        {
            "name": "Perfect",
            "artist": "Ed Sheeran",
            "url": "https://www.youtube.com/results?search_query=Perfect+Ed+Sheeran"
        },

        {
            "name": "A Thousand Years",
            "artist": "Christina Perri",
            "url": "https://www.youtube.com/results?search_query=A+Thousand+Years+Christina+Perri"
        }

    ],


    # ========================================================
    # PARTY / FUN
    # ========================================================

    "Party": [

        {
            "name": "Aura 10/10",
            "artist": "Hiphop Tamizha & Thamizh Aadhavan",
            "url": "https://www.youtube.com/results?search_query=Aura+10%2F10+Hiphop+Tamizha"
        },

        {
            "name": "Kanimaa",
            "artist": "Santhosh Narayanan & The Indian Choral Ensemble",
            "url": "https://www.youtube.com/results?search_query=Kanimaa+Santhosh+Narayanan+Retro"
        },

        {
            "name": "Oorum Blood",
            "artist": "Sai Abhyankkar, Paal Dabba, bebhumika & Deepthi Suresh",
            "url": "https://www.youtube.com/results?search_query=Oorum+Blood+Sai+Abhyankkar"
        },

        {
            "name": "Cruel Summer",
            "artist": "Taylor Swift",
            "url": "https://www.youtube.com/results?search_query=Cruel+Summer+Taylor+Swift"
        },

        {
            "name": "As It Was",
            "artist": "Harry Styles",
            "url": "https://www.youtube.com/results?search_query=As+It+Was+Harry+Styles"
        }

    ]

}


# ============================================================
# TARGET MOODS
# ============================================================

target_moods = {

    "😌 Calm": "Calm",

    "😊 Happy": "Happy",

    "⚡ Energetic": "Energetic",

    "🎯 Focus / Study": "Focus",

    "💪 Motivation": "Motivation",

    "😴 Sleep": "Sleep",

    "❤️ Romantic": "Romantic",

    "🎉 Party / Fun": "Party"

}


# ============================================================
# SMART MUSIC RECOMMENDATION
# ============================================================

def recommend_category(
    current_emotion,
    desired_mood
):

    if (
        current_emotion == "Stressed"
        and desired_mood == "Calm"
    ):
        return "Calm"

    if (
        current_emotion == "Sad"
        and desired_mood == "Happy"
    ):
        return "Happy"

    if (
        current_emotion == "Angry"
        and desired_mood == "Calm"
    ):
        return "Calm"

    if (
        current_emotion == "Stressed"
        and desired_mood == "Focus"
    ):
        return "Focus"

    if (
        current_emotion == "Sad"
        and desired_mood == "Motivation"
    ):
        return "Motivation"

    return desired_mood


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:

    st.session_state.page = "Home"


if "mood_history" not in st.session_state:

    st.session_state.mood_history = []


if "feedback_history" not in st.session_state:

    st.session_state.feedback_history = []


if "emotion" not in st.session_state:

    st.session_state.emotion = None


if "confidence" not in st.session_state:

    st.session_state.confidence = None


if "model_emotion" not in st.session_state:

    st.session_state.model_emotion = None


if "desired_mood" not in st.session_state:

    st.session_state.desired_mood = None


if "music_category" not in st.session_state:

    st.session_state.music_category = None


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:

    st.title("🎵 MoodLens AI")

    st.caption(
        "Your emotions. "
        "Your destination. "
        "Your music."
    )

    st.markdown("---")

    st.subheader("Navigation")


    if st.button(
        "🏠  Home",
        use_container_width=True
    ):

        st.session_state.page = "Home"


    if st.button(
        "🧠  Analyze Mood",
        use_container_width=True
    ):

        st.session_state.page = "Analyze"


    if st.button(
        "🎯  Mood Goal",
        use_container_width=True
    ):

        st.session_state.page = "Goal"


    if st.button(
        "🎵  My Music",
        use_container_width=True
    ):

        st.session_state.page = "Music"


    if st.button(
        "📊  Mood Journey",
        use_container_width=True
    ):

        st.session_state.page = "Journey"


    if st.button(
        "❤️  Feedback",
        use_container_width=True
    ):

        st.session_state.page = "Feedback"


    st.markdown("---")

    st.caption("🤖 Powered by AI")

    st.caption(
        "🎧 Emotion-aware recommendation"
    )


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    st.title("🎵 Welcome to MoodLens AI")

    st.subheader(
        "🧠 Music that understands how you feel."
    )

    st.write(
        "MoodLens AI uses artificial intelligence "
        "to understand emotions from natural language "
        "and recommend music based on the mood "
        "you want to reach."
    )

    st.markdown("---")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown("## 🧠")

        st.write("### Understand")

        st.write(
            "Describe your day naturally "
            "and let AI identify the emotion."
        )


    with col2:

        st.markdown("## 🎯")

        st.write("### Choose")

        st.write(
            "Choose how you want to feel."
        )


    with col3:

        st.markdown("## 🎵")

        st.write("### Transform")

        st.write(
            "Receive music recommendations "
            "for your emotional goal."
        )


    st.markdown("---")

    st.info(
        "💡 Start by clicking "
        "**🧠 Analyze Mood** from the sidebar."
    )


# ============================================================
# ANALYZE MOOD
# ============================================================

elif st.session_state.page == "Analyze":

    st.title("🧠 Analyze Your Mood")

    st.write(
        "Tell us what happened today. "
        "You don't need to select an emotion."
    )


    user_text = st.text_area(

        "💭 Tell me about your day",

        placeholder=(
            "Example: I have an exam tomorrow "
            "and I'm really nervous. "
            "I keep worrying about whether "
            "I will pass."
        ),

        height=180
    )


    if st.button(
        "🔍 Analyze My Emotion",
        use_container_width=True
    ):

        if not user_text.strip():

            st.warning(
                "⚠️ Please describe how you are feeling."
            )

        else:

            with st.spinner(
                "🤖 AI is analyzing your emotions..."
            ):

                (
                    emotion,
                    confidence,
                    model_emotion
                ) = detect_emotion(user_text)


            st.session_state.emotion = emotion

            st.session_state.confidence = confidence

            st.session_state.model_emotion = model_emotion


            st.success(
                "✅ Emotion analysis completed!"
            )


    if st.session_state.emotion:

        st.markdown("---")

        st.subheader("🤖 AI Result")


        col1, col2 = st.columns(2)


        with col1:

            st.metric(

                "Detected Emotion",

                f"{emotion_emojis.get(
                    st.session_state.emotion,
                    '🧠'
                )} "
                f"{st.session_state.emotion}"
            )


        with col2:

            st.metric(

                "AI Confidence",

                f"{st.session_state.confidence:.1f}%"
            )


        st.progress(

            min(
                st.session_state.confidence / 100,
                1
            )
        )


        st.write(

            "AI classification: "
            f"**{st.session_state.model_emotion}**"
        )


        st.info(

            "🎯 Next step: go to "
            "**Mood Goal** and choose "
            "how you want to feel."
        )


# ============================================================
# MOOD GOAL
# ============================================================

elif st.session_state.page == "Goal":

    st.title("🎯 Choose Your Mood Goal")


    if not st.session_state.emotion:

        st.warning(
            "⚠️ Analyze your mood first."
        )

        st.info(
            "Go to **🧠 Analyze Mood** "
            "from the sidebar."
        )


    else:

        current_emotion = (
            st.session_state.emotion
        )


        st.write(

            "Your current AI-detected mood is "
            f"**{emotion_emojis.get(
                current_emotion,
                '🧠'
            )} "
            f"{current_emotion}**."
        )


        st.markdown("---")


        selected_target = st.selectbox(

            "🌈 How do you want to feel?",

            list(target_moods.keys())
        )


        desired_mood = target_moods[
            selected_target
        ]


        st.session_state.desired_mood = (
            desired_mood
        )


        st.markdown("---")


        st.subheader(
            "🧭 Your Mood Journey"
        )


        st.success(

            f"{emotion_emojis.get(
                current_emotion,
                '🧠'
            )} "
            f"**{current_emotion}**"
            "   →   "
            f"{emotion_emojis.get(
                desired_mood,
                '🎯'
            )} "
            f"**{desired_mood}**"
        )


        if st.button(

            "🎵 Generate My Music",

            use_container_width=True
        ):

            category = recommend_category(

                current_emotion,

                desired_mood
            )


            st.session_state.music_category = (
                category
            )


            history_entry = {

                "Current Emotion":
                    current_emotion,

                "Target Mood":
                    desired_mood,

                "AI Confidence":
                    round(
                        st.session_state.confidence,
                        1
                    ),

                "Music Category":
                    category
            }


            st.session_state.mood_history.append(
                history_entry
            )


            st.success(

                "🎵 Your personalized "
                "music journey is ready!"
            )


            st.info(

                "Go to **🎵 My Music** "
                "from the sidebar."
            )


# ============================================================
# MY MUSIC
# ============================================================

elif st.session_state.page == "Music":

    st.title(
        "🎵 My Personalized Music"
    )


    if not st.session_state.music_category:

        st.warning(
            "⚠️ No playlist has been created yet."
        )

        st.info(

            "Go to **🧠 Analyze Mood → "
            "🎯 Mood Goal** to create "
            "your playlist."
        )


    else:

        category = (
            st.session_state.music_category
        )


        desired = (
            st.session_state.desired_mood
        )


        current = (
            st.session_state.emotion
        )


        st.subheader(

            f"🎧 Music for "
            f"{emotion_emojis.get(
                desired,
                '🎯'
            )} "
            f"{desired}"
        )


        st.write(

            "Your journey: "

            f"{emotion_emojis.get(
                current,
                '🧠'
            )} "

            f"{current}"

            " → "

            f"{emotion_emojis.get(
                desired,
                '🎯'
            )} "

            f"{desired}"
        )


        st.markdown("---")


        for index, song in enumerate(

            songs[category],

            1
        ):

            st.markdown(

                f"### {index}. 🎵 "
                f"{song['name']}"
            )


            st.write(

                f"**Artist:** "
                f"{song['artist']}"
            )


            st.link_button(

                "▶️ Play on YouTube",

                song["url"]
            )


            st.markdown("---")


        st.success(

            "🎧 Enjoy your personalized "
            "music journey!"
        )


# ============================================================
# MOOD JOURNEY
# ============================================================

elif st.session_state.page == "Journey":

    st.title(
        "📊 My Mood Journey"
    )


    if not st.session_state.mood_history:

        st.info(

            "Your mood history will appear "
            "here after you create playlists."
        )


    else:

        df = pd.DataFrame(

            st.session_state.mood_history
        )


        st.metric(

            "🎵 Total Sessions",

            len(df)
        )


        st.markdown("---")


        st.subheader(
            "📝 Session History"
        )


        st.dataframe(

            df,

            use_container_width=True,

            hide_index=True
        )


        st.markdown("---")


        st.subheader(
            "📈 AI Confidence Over Sessions"
        )


        confidence_df = df[
            ["AI Confidence"]
        ]


        confidence_df.index = [

            f"Session {i + 1}"

            for i in range(len(df))
        ]


        st.line_chart(
            confidence_df
        )


        st.markdown("---")


        st.subheader(
            "🧭 Your Emotional Destinations"
        )


        for index, row in df.iterrows():

            st.write(

                f"**Session {index + 1}:** "

                f"{emotion_emojis.get(
                    row['Current Emotion'],
                    '🧠'
                )} "

                f"{row['Current Emotion']}"

                " → "

                f"{emotion_emojis.get(
                    row['Target Mood'],
                    '🎯'
                )} "

                f"{row['Target Mood']}"
            )


# ============================================================
# FEEDBACK
# ============================================================

elif st.session_state.page == "Feedback":

    st.title(
        "❤️ Music Feedback"
    )


    st.write(

        "Your feedback helps us understand "
        "whether the recommendation matched "
        "your emotional goal."
    )


    if not st.session_state.music_category:

        st.info(

            "Create a playlist first "
            "to provide feedback."
        )


    else:

        feedback = st.radio(

            "🎧 How did the music make you feel?",

            [

                "😊 Much better",

                "🙂 Slightly better",

                "😐 No change",

                "😔 Worse"
            ]
        )


        if st.button(

            "💾 Submit Feedback",

            use_container_width=True
        ):


            st.session_state.feedback_history.append(

                feedback
            )


            st.success(

                f"❤️ Feedback recorded: "
                f"{feedback}"
            )


            if feedback == "😊 Much better":

                st.balloons()

                st.success(

                    "🎉 Great! The recommendation "
                    "seems to have worked well for you."
                )


            elif feedback == "🙂 Slightly better":

                st.info(

                    "👍 Thanks! "
                    "That's a positive response."
                )


            elif feedback == "😐 No change":

                st.info(

                    "😐 Thanks. "
                    "This recommendation may need improvement."
                )


            else:

                st.warning(

                    "💭 Thanks for your honest feedback."
                )


        st.markdown("---")


        if st.session_state.feedback_history:

            total = len(

                st.session_state.feedback_history
            )


            positive = sum(

                1

                for item in
                st.session_state.feedback_history

                if item in [

                    "😊 Much better",

                    "🙂 Slightly better"
                ]
            )


            rate = (

                positive / total

            ) * 100


            st.metric(

                "📊 Positive Response Rate",

                f"{rate:.0f}%"
            )


            st.write(

                f"Based on {total} "
                f"feedback response(s)."
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(

    "🎵 MoodLens AI | "
    "AI-powered emotion-aware "
    "music recommendation"
)