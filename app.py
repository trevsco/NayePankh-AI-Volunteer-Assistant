
import streamlit as st
import time
from gemini_service import generate_response

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="NayePankh AI Assistant",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# CSS
# -------------------------------------------------
st.markdown("""
<style>

/* Main background */
.stApp{
    background-color:#F7FAF8;
}

/* Title */
h1{
    color:#1B5E20 !important;
    font-size:52px !important;
    font-weight:bold !important;
}

/* Text */
p, div, label{
    color:#212121 !important;
    font-size:18px;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background: linear-gradient(to bottom, #E8F5E9, #F4FBF5);
            
}

/* Normal buttons */
.stButton > button{
    background: linear-gradient(135deg,#43A047,#2E7D32);
    color:white !important;
    border:none;
    border-radius:15px;
    height:52px;
    width:100%;
    font-size:16px;
    font-weight:600;
    box-shadow:0px 4px 10px rgba(0,0,0,0.15);
    transition:0.3s;
}

.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0px 6px 15px rgba(0,0,0,0.2);
}

/* Download button */
.stDownloadButton > button{
    background: linear-gradient(135deg,#1976D2,#1565C0);
    color:white !important;
    border:none;
    border-radius:15px;
    height:52px;
    width:100%;
    font-size:16px;
    font-weight:600;
    box-shadow:0px 4px 10px rgba(0,0,0,0.15);
}

.stDownloadButton > button:hover{
    background: linear-gradient(135deg,#1565C0,#0D47A1);
    transform:translateY(-2px);
}

/* Chat cards */
[data-testid="stChatMessage"]{
    background:white;
    border-radius:20px;
    padding:20px;
    margin-bottom:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

/* Hide Streamlit elements */

footer{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Session State
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content":
            "👋 Hello! I am the NayePankh AI Volunteer Assistant.\n\nHow can I help you today?"
        }
    ]

if "query" not in st.session_state:
    st.session_state.query = None

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
with st.sidebar:

    st.markdown("""
    <h2 style='color:#1B5E20'>
    🌿 NayePankh AI
    </h2>
    """, unsafe_allow_html=True)

    st.caption("Volunteer Assistant")

    st.markdown("---")

    st.subheader("Features")

    st.info("📚 FAQ Support")
    st.info("🤝 Volunteer Guidance")
    st.info("🧠 Personalized Responses")
    

    st.markdown("---")

    st.metric("Version", "2.0")
    st.metric("Messages", len(st.session_state.messages))
    st.metric("Conversation Length", len(st.session_state.messages))

    st.markdown("---")

    # Download Chat
    chat_history = ""

    for message in st.session_state.messages:
        chat_history += (
            f"{message['role'].upper()}:\n"
            f"{message['content']}\n\n"
        )

    st.download_button(
        "📥 Download Chat",
        chat_history,
        file_name="chat_history.txt"
    )

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content":
                "👋 Hello! I am the NayePankh AI Volunteer Assistant.\n\nHow can I help you today?"
            }
        ]

        st.session_state.query = None

        st.rerun()

# -------------------------------------------------
# Title
# -------------------------------------------------
st.markdown("""
<h1 style='text-align:center'>
🌿 NayePankh AI
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;
font-size:22px;
color:#616161'>
Helping volunteers and interns with information and guidance.
</p>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Suggested Questions
# -------------------------------------------------
with st.container(border=True):

    st.subheader("💡 Suggested Questions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("What is NayePankh Foundation?"):
            st.session_state.query = "What is NayePankh Foundation?"

        if st.button("How can I volunteer?"):
            st.session_state.query = "How can I volunteer?"

    with col2:

        if st.button("What internships are available?"):
            st.session_state.query = "What internships are available?"

        if st.button("How can I contribute?"):
            st.session_state.query = "How can I contribute?"

# -------------------------------------------------
# Display Messages
# -------------------------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

# -------------------------------------------------
# Input
# -------------------------------------------------
user_input = st.chat_input(
    "Ask about volunteering, internships or NayePankh..."
)

# Button question support
if st.session_state.query:

    user_input = st.session_state.query
    st.session_state.query = None

# -------------------------------------------------
# Generate Response
# -------------------------------------------------
if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.spinner("🤖 Thinking..."):

        time.sleep(1)

        response = generate_response(user_input)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()

