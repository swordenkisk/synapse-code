import streamlit as st
from app.cognitive.layers import SynapseBrain
import os

# Page Configuration
st.set_page_config(page_title="Synapse-Code Architect", page_icon="🧠")

st.title("Synapse-Code AI Architect")
st.markdown("""
Transforming project goals into precise technical specifications through a layered cognitive process: 
**Array ➔ Lattice ➔ Tensor ➔ Grid ➔ Operator**
""")

# --- API Key Management ---
# Attempts to get the key from Hugging Face Secrets. 
# If not found, it prompts the user to enter their own key in the sidebar.
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.sidebar.warning("OpenAI API Key not found in settings.")
    user_api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
    if user_api_key:
        os.environ["OPENAI_API_KEY"] = user_api_key
        api_key = user_api_key

# --- Main Interface ---
goal = st.text_area("Project Goal", 
                    placeholder="Example: Create a high-performance pricing calculator for a SaaS agency that handles dynamic currency conversion and tiered discounts.")

if st.button("Start Cognitive Build Process"):
    if not api_key:
        st.error("Please enter your OpenAI API Key in the sidebar first!")
    elif not goal:
        st.warning("Please describe your project goal first.")
    else:
        try:
            with st.spinner("Processing Cognitive Layers (Array, Lattice, Tensor, Grid)..."):
                # Calling the core logic from your repository
                brain = SynapseBrain()
                result = brain.process_blueprint(goal)
                
                st.success("Architectural Design Complete!")
                
                st.divider()
                
                if "array" in result:
                    with st.expander("Atomic Requirements (The Array)", expanded=True):
                        st.write(result["array"])
                
                if "grid" in result:
                    with st.expander("Technical Specifications (The Grid)", expanded=True):
                        st.markdown(result["grid"])
                
                # Export option
                full_text = f"Goal: {goal}\n\nArray:\n{result.get('array','')}\n\nGrid:\n{result.get('grid','')}"
                st.download_button("Download Blueprint as TXT", full_text, file_name="blueprint.txt")

        except Exception as e:
            st.error(f"An error occurred during processing: {e}")

# Footer
st.divider()
st.caption("Developed by Synapse-Code | Powered by OpenAI")
