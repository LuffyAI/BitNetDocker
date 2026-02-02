import streamlit as st
import asyncio
from pathlib import Path

# ---------- Paths ----------
BITNET_DIR = Path("/app/BitNet")
MODEL_PATH = "/app/BitNet/models/bitnet-b1.58-2B-4T/ggml-model-i2_s.gguf"


# ---------- Backend ----------
class BitNetUI:
    def __init__(self, model_path: str):
        self.model_path = model_path

    async def run_inference(self, prompt: str) -> str:
        proc = await asyncio.create_subprocess_exec(
            "python3",
            "run_inference.py",
            "-m", self.model_path,
            "-p", prompt,
            cwd=BITNET_DIR,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            return stderr.decode()

        return stdout.decode()


# ---------- Page Config ----------
st.set_page_config(
    page_title="BitNet Chat",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- Header ----------
st.markdown(
    """
    <style>
    .header {
        position: sticky;
        top: 0;
        background: white;
        padding: 0.75rem 0;
        border-bottom: 1px solid #e5e5e5;
        z-index: 100;
    }
    </style>
    <div class="header">
        <h2>BitNet Chat</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- State ----------
if "ui" not in st.session_state:
    st.session_state.ui = BitNetUI(MODEL_PATH)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thinking" not in st.session_state:
    st.session_state.thinking = False


# ---------- Render Chat History ----------
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content)


# ---------- Input ----------
prompt = st.chat_input(
    "Send a message",
    disabled=st.session_state.thinking,
)

if prompt and not st.session_state.thinking:
    # lock input
    st.session_state.thinking = True

    # user message (immediate)
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # assistant with animated spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking"):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            response = loop.run_until_complete(
                st.session_state.ui.run_inference(prompt)
            )
            loop.close()

        st.markdown(response)

    # persist assistant message
    st.session_state.messages.append(("assistant", response))

    # unlock + rerun
    st.session_state.thinking = False
    st.rerun()
