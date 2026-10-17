import streamlit as st
from app.cognitive.layers import SynapseBrain
import os

# Page Configuration
st.set_page_config(page_title="Synapse-Code Architect", page_icon="🧠", layout="wide")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 Synapse-Code AI Architect")
st.markdown("""
**Transform your project goals into professional technical blueprints.** 
Choose your preferred AI brain and let the cognitive pipeline handle the rest.
""")

# --- SIDEBAR: Configuration ---
st.sidebar.header("⚙️ AI Configuration")

# 1. Provider Selection
provider = st.sidebar.selectbox(
    "Select AI Provider",
    ["OpenAI", "DeepSeek", "OpenRouter"]
)

# 2. Dynamic Base URL and Model Mapping
provider_config = {
    "OpenAI": {
        "base_url": None, # Uses default OpenAI URL
        "default_model": "gpt-4o",
        "key_env": "OPENAI_API_KEY"
    },
    "DeepSeek": {
        "base_url": "https://api.deepseek.com",
        "default_model": "deepseek-chat",
        "key_env": "DEEPSEEK_API_KEY"
    },
    "OpenRouter": {
        "base_url": "https://openrouter.ai/api/v1",
        "default_model": "deepseek/deepseek-chat",
        "key_env": "OPENROUTER_API_KEY"
    }
}

config = provider_config[provider]

# 3. API Key Handling
# Check if key exists in Hugging Face Secrets first
api_key = os.getenv(config["key_env"])

if not api_key:
    st.sidebar.warning(f"No {provider} API Key found in secrets.")
    user_api_key = st.sidebar.text_input(f"Enter {provider} API Key:", type="password")
    if user_api_key:
        api_key = user_api_key
else:
    st.sidebar.success(f"✅ {provider} Key loaded from secrets.")

# 4. Model Selection
model_choice = st.sidebar.text_input("Model Name", value=config["default_model"])

# --- APPLYING SETTINGS TO ENVIRONMENT ---
# We force the environment variables so the SynapseBrain logic picks them up
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    if config["base_url"]:
        os.environ["OPENAI_API_BASE"] = config["base_url"]
    else:
        # Reset to default if OpenAI is selected
        if "OPENAI_API_BASE" in os.environ:
            del os.environ["OPENAI_API_BASE"]

# --- MAIN INTERFACE ---
col1, col2 = st.columns([2, 1])

with col1:
    goal = st.text_area("Project Goal", 
                        placeholder="Describe your project in detail... (e.g., A SaaS platform for AI-driven legal document analysis with multi-tenant support and PDF parsing)", 
                        height=200)

with col2:
    st.info("💡 **Tip:** Be as specific as possible about your requirements to get a better 'Grid' result.")
    st.markdown("**Workflow:**\n1. Array (Requirements)\n2. Lattice (Dependencies)\n3. Tensor (Tension/Trade-offs)\n4. Grid (Tech Spec)")

if st.button("🚀 Generate Technical Blueprint"):
    if not api_key:
        st.error(f"Please provide a valid {provider} API Key in the sidebar!")
    elif not goal:
        st.warning("Please enter a project goal first.")
    else:
        try:
            with st.spinner(f"Synapse-Code is thinking using {provider} ({model_choice})..."):
                # Initialize the Brain
                brain = SynapseBrain()
                
                # If your SynapseBrain class allows passing a model, do it here.
                # Otherwise, it uses the default inside the class.
                result = brain.process_blueprint(goal)
                
                st.success("Blueprint successfully generated!")
                st.divider()
                
                # Result Display
                if "array" in result:
                    with st.expander("📦 The Array: Atomic Requirements", expanded=True):
                        st.write(result["array"])
                
                if "grid" in result:
                    with st.expander("📐 The Grid: Final Technical Specifications", expanded=True):
                        st.markdown(result["grid"])
                
                # Export
                full_output = f"Project Goal: {goal}\n\n--- THE ARRAY ---\n{result.get('array','')}\n\n--- THE GRID ---\n{result.get('grid','')}"
                st.download_button(
                    label="💾 Download Blueprint (.txt)",
                    data=full_output,
                    file_name="synapse_blueprint.txt",
                    mime="text/plain"
                )

        except Exception as e:
            st.error(f"Critical Error: {e}")
            st.info("Note: If this is an API error, check if your key has enough credits or if the model name is correct.")

# Footer
st.divider()
st.caption("Developed by Synapse-Code | Multi-LLM Support enabled")
