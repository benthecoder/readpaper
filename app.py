import streamlit as st
from pathlib import Path
import tempfile
from main import Sumrize
from utils import create_markdown_pdf


st.set_page_config(page_title="readpaper", page_icon="📄")

st.title("readpaper")

# File uploader
uploaded_file = st.file_uploader("Upload your research paper (PDF)", type="pdf")

# Initialize session state for storing the summary
if "summary" not in st.session_state:
    st.session_state.summary = None

# File uploader and field input remain the same ...

if uploaded_file:
    # Only analyze if we don't already have a summary
    if st.session_state.summary is None:
        with st.spinner("Analyzing paper... this takes about a minute"):
            try:
                # Save uploaded file temporarily
                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=".pdf"
                ) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name

                # Initialize summarizer
                summarizer = Sumrize()

                # Generate summary
                st.session_state.summary = summarizer.summarize(tmp_path)

            except Exception as e:
                st.error(f"Error processing paper: {str(e)}")

            finally:
                # Cleanup
                if "tmp_path" in locals():
                    Path(tmp_path).unlink(missing_ok=True)

    if st.session_state.summary:
        st.markdown(st.session_state.summary)

        # Add download button
        st.download_button(
            label="Download Summary as PDF",
            data=create_markdown_pdf(st.session_state.summary),
            file_name=f"{Path(uploaded_file.name).stem}_summary.pdf",
            mime="application/pdf",
        )

else:
    st.info(
        "Please upload a PDF file and specify the research field to begin analysis."
    )

with st.sidebar:
    st.header("ReadPaper 📚")
    st.markdown(
        """
    AI-powered research paper analyzer that generates comprehensive summaries.
    
    ### Summary Structure
    - Problem Statement & Significance
    - Conceptual Innovation
    - Technical Architecture
    - Mathematical Foundation
    - Critical Analysis & Future Work
    
    ---
    Powered by [Claude 3.5 Sonnet](https://www.anthropic.com/claude)
    
    [View on GitHub](https://github.com/benthecoder/readpaper) • [Twitter](https://twitter.com/benxneo)
    
    Built by [Benedict Neo](https://www.linkedin.com/in/benedictneo/)
    """
    )
