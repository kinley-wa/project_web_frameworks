import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Daily Focus Tracker", layout="centered")

# Title
st.title("🧠 Daily Focus & Mood Tracker")
st.write("Reflect on your day and improve productivity.")

# Initialize session state
if "logs" not in st.session_state:
    st.session_state.logs = []

# Sidebar inputs
with st.sidebar:
    st.header("Today's Check-in")
    mood = st.selectbox(
        "How do you feel today?",
        ["😊 Happy", "😐 Neutral", "😟 Stressed", "😴 Tired"]
    )

    focus = st.text_input("What is your main focus today?")
    productivity = st.slider("Productivity Level", 1, 10, 5)

    save = st.button("Save Entry")

# Save entry
if save:
    st.session_state.logs.append({
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Mood": mood,
        "Focus": focus,
        "Productivity": productivity
    })
    st.success("Entry saved!")

# Display logs
if st.session_state.logs:
    st.subheader("📓 Your Daily Logs")
    st.table(st.session_state.logs)

    # Insights
    avg_productivity = sum(
        entry["Productivity"] for entry in st.session_state.logs
    ) / len(st.session_state.logs)

    st.subheader("📊 Insights")
    st.metric("Average Productivity", round(avg_productivity, 2))
else:
    st.info("No entries yet. Start by adding one from the sidebar.")
