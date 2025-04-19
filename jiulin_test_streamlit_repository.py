# main.py
import streamlit as st
import time


st.set_page_config(
    page_title="Rainbow UI",
    layout="wide",
    initial_sidebar_state="expanded"
)


def inject_css():
    rainbow_css = """
    <style>
        @keyframes rainbow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .stApp {
            background: linear-gradient(
                45deg,
                #ff0000,
                #ff7f00,
                #ffff00,
                #00ff00,
                #0000ff,
                #4b0082,
                #8f00ff,
                #ff0000
            );
            background-size: 600% 600%;
            animation: rainbow 15s ease infinite;
            color: white;
        }

        .main-content {
            background: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0,0,0,0.2);
        }

        .stTextInput>div>div>input,
        .stButton>button {
            background: rgba(255, 255, 255, 0.8) !important;
            border-radius: 25px !important;
            transition: all 0.3s ease !important;
        }

        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
    </style>
    """
    st.markdown(rainbow_css, unsafe_allow_html=True)

inject_css()


st.title("🌈 LIUJIULIN")
st.write("Lucky to lucky 🏀")

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("📝 input", expanded=True):
            name = st.text_input("name")
            mood = st.select_slider("You are ", options=["😭", "😔", "😐", "🙂", "😁"])
            if st.button("Save get"):
                st.session_state.submitted = True

    with col2:
        st.header("JIULIN - Hub")
        clock_placeholder = st.empty()
        while True:
            current_time = time.strftime("%H:%M:%S")
            clock_placeholder.markdown(f"<h2 style='color: #333;'>{current_time}</h2>", 
                                      unsafe_allow_html=True)
            time.sleep(1)

if st.session_state.get('submitted'):
    st.balloons()
    st.success(f"Hi {name}！Good {mood} ~！")
