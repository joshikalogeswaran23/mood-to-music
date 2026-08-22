import streamlit as st

# Page settings
st.set_page_config(
    page_title="Mood to Music",
    page_icon="🎵",
    layout="centered"
)

# Title
st.title("🎵 Mood to Music")
st.write("Tell us your mood and discover music that matches it!")

# Mood selection
mood = st.selectbox(
    "😊 What is your mood?",
    [
        "Happy",
        "Sad",
        "Relaxed",
        "Romantic",
        "Energetic",
        "Angry"
    ]
)

# Song recommendations
songs = {
    "Happy": [
        {
            "name": "On Top of the World",
            "artist": "Imagine Dragons",
            "url": "https://www.youtube.com/results?search_query=On+Top+of+the+World+Imagine+Dragons"
        },
        {
            "name": "Good Life",
            "artist": "OneRepublic",
            "url": "https://www.youtube.com/results?search_query=Good+Life+OneRepublic"
        },
        {
            "name": "Walking on Sunshine",
            "artist": "Katrina and the Waves",
            "url": "https://www.youtube.com/results?search_query=Walking+on+Sunshine+Katrina+and+the+Waves"
        }
    ],

    "Sad": [
        {
            "name": "The Night We Met",
            "artist": "Lord Huron",
            "url": "https://www.youtube.com/results?search_query=The+Night+We+Met+Lord+Huron"
        },
        {
            "name": "Arcade",
            "artist": "Duncan Laurence",
            "url": "https://www.youtube.com/results?search_query=Arcade+Duncan+Laurence"
        },
        {
            "name": "When I Was Your Man",
            "artist": "Bruno Mars",
            "url": "https://www.youtube.com/results?search_query=When+I+Was+Your+Man+Bruno+Mars"
        }
    ],

    "Relaxed": [
        {
            "name": "Golden Hour",
            "artist": "JVKE",
            "url": "https://www.youtube.com/results?search_query=Golden+Hour+JVKE"
        },
        {
            "name": "Until I Found You",
            "artist": "Stephen Sanchez",
            "url": "https://www.youtube.com/results?search_query=Until+I+Found+You+Stephen+Sanchez"
        },
        {
            "name": "Sunset Lover",
            "artist": "Petit Biscuit",
            "url": "https://www.youtube.com/results?search_query=Sunset+Lover+Petit+Biscuit"
        }
    ],

    "Romantic": [
        {
            "name": "Until I Found You",
            "artist": "Stephen Sanchez",
            "url": "https://www.youtube.com/results?search_query=Until+I+Found+You+Stephen+Sanchez"
        },
        {
            "name": "Lover",
            "artist": "Taylor Swift",
            "url": "https://www.youtube.com/results?search_query=Lover+Taylor+Swift"
        },
        {
            "name": "All of Me",
            "artist": "John Legend",
            "url": "https://www.youtube.com/results?search_query=All+of+Me+John+Legend"
        }
    ],

    "Energetic": [
        {
            "name": "Levitating",
            "artist": "Dua Lipa",
            "url": "https://www.youtube.com/results?search_query=Levitating+Dua+Lipa"
        },
        {
            "name": "Don't Start Now",
            "artist": "Dua Lipa",
            "url": "https://www.youtube.com/results?search_query=Dont+Start+Now+Dua+Lipa"
        },
        {
            "name": "Thunder",
            "artist": "Imagine Dragons",
            "url": "https://www.youtube.com/results?search_query=Thunder+Imagine+Dragons"
        }
    ],

    "Angry": [
        {
            "name": "Believer",
            "artist": "Imagine Dragons",
            "url": "https://www.youtube.com/results?search_query=Believer+Imagine+Dragons"
        },
        {
            "name": "Numb",
            "artist": "Linkin Park",
            "url": "https://www.youtube.com/results?search_query=Numb+Linkin+Park"
        },
        {
            "name": "In the End",
            "artist": "Linkin Park",
            "url": "https://www.youtube.com/results?search_query=In+the+End+Linkin+Park"
        }
    ]
}

# Mood emojis
mood_emojis = {
    "Happy": "😊",
    "Sad": "😢",
    "Relaxed": "😌",
    "Romantic": "❤️",
    "Energetic": "⚡",
    "Angry": "😡"
}

# Display mood
st.subheader(
    f"{mood_emojis[mood]} {mood} Mood"
)

st.write("Here are some songs selected for your mood:")

# Display songs
for song in songs[mood]:

    st.markdown("---")

    st.write(f"### 🎵 {song['name']}")

    st.write(f"**Artist:** {song['artist']}")

    st.link_button(
        "▶️ Play on YouTube",
        song["url"]
    )

st.markdown("---")
st.markdown("---")

st.success(
    "🎧 Enjoy your music! Choose another mood to get different recommendations."
)