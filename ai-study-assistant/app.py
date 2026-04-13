import streamlit as st
import os

from rag_pipeline import add_notes, retrieve, generate_answer, summarize_notes

st.set_page_config(page_title="AI Study Assistant", layout="wide")

# ==============================
# SESSION STATE
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
# SIDEBAR
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

# Store
if store_btn:
    st.session_state.notes = notes
    add_notes(notes)
    st.sidebar.success("Stored!")

# Summarize
if summary_btn:
    with st.spinner("Summarizing..."):
        st.session_state.summary = summarize_notes(notes)

# Show summary
if st.session_state.summary:
    st.sidebar.markdown("### 📝 Summary")
    st.sidebar.write(st.session_state.summary)

# ==============================
# CHAT
# ==============================
st.title("🧠 AI Study Assistant")

question = st.text_input("Ask a question")

if st.button("Ask") and question:
    st.session_state.messages.append(("user", question))

    with st.spinner("Thinking..."):
        results = retrieve(question)
        context = "\n".join(results)
        answer = generate_answer(question, context)

    st.session_state.messages.append(("bot", answer))
    st.session_state.last_results = results

# Show chat
for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**AI:** {msg}")

# ==============================
# RELEVANT NOTES
# ==============================
if st.session_state.last_results:
    st.markdown("### 📄 Relevant Notes")
    for r in st.session_state.last_results:
        st.write(f"- {r}")