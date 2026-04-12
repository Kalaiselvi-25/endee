import streamlit as st
import os

# 🔥 Clean logs
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

from rag_pipeline import add_notes, retrieve, generate_answer, summarize_notes

st.set_page_config(page_title="AI Study Assistant", layout="wide")

# ==============================
# ✅ SESSION STATE (IMPORTANT)
# ==============================
if "notes" not in st.session_state:
    st.session_state.notes = ""

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_results" not in st.session_state:
    st.session_state.last_results = []

# ==============================
# 🎨 MODERN CSS
# ==============================
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}

.chat-container {
    max-width: 800px;
    margin: auto;
}

.chat-bubble {
    padding: 12px 16px;
    border-radius: 18px;
    margin-bottom: 10px;
    display: inline-block;
    max-width: 75%;
    font-size: 15px;
}

.user {
    background-color: #4CAF50;
    color: white;
    float: right;
    clear: both;
}

.bot {
    background-color: #e4e6eb;
    color: black;
    float: left;
    clear: both;
}

textarea, input {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# 🧠 TITLE
# ==============================
st.markdown("<h1 style='text-align:center;'>🧠 AI Study Assistant</h1>", unsafe_allow_html=True)

# ==============================
# 📌 SIDEBAR
# ==============================
st.sidebar.title("📚 Notes")

notes = st.sidebar.text_area(
    "Paste notes",
    value=st.session_state.notes,
    height=200
)

with st.sidebar.form("notes_form"):
    store_btn = st.form_submit_button("📥 Store")
    summary_btn = st.form_submit_button("📝 Summarize")

# 🔹 Store Notes
if store_btn:
    st.session_state.notes = notes
    add_notes(notes)
    st.sidebar.success("Stored!")

# 🔹 Summarize Notes
if summary_btn:
    with st.spinner("Summarizing..."):
        st.session_state.summary = summarize_notes(st.session_state.notes)

# 🔹 Always show summary
if st.session_state.summary:
    st.sidebar.markdown("### 📝 Summary")
    st.sidebar.write(st.session_state.summary)

# 🔹 Optional Notes Preview (clean UI)
if st.session_state.notes:
    st.sidebar.markdown("### 📄 Notes Preview")
    for line in st.session_state.notes.split("."):
        line = line.strip()
        if line:
            st.sidebar.write(f"• {line}")

# ==============================
# 💬 CHAT SECTION
# ==============================
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

with st.form("chat_form", clear_on_submit=True):
    question = st.text_input("Type your question...")
    ask_btn = st.form_submit_button("Ask")

# 🔹 Ask question
if ask_btn and question:
    st.session_state.messages.append(("user", question))

    with st.spinner("Thinking..."):
        results = retrieve(question)
        context = "\n".join(results)
        answer = generate_answer(question, context)

    st.session_state.messages.append(("bot", answer))
    st.session_state.last_results = results

# 🔹 Render chat
for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"<div class='chat-bubble user'>{msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble bot'>{msg}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# 📄 RELEVANT NOTES
# ==============================
if st.session_state.last_results:
    st.markdown("### 📄 Relevant Notes")
    for r in st.session_state.last_results:
        st.write(f"- {r}")