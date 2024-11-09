import streamlit as st
from pathlib import Path
import tempfile
from main import Sumrize
from utils import create_markdown_pdf
import json
from pathlib import Path


def load_sample_summary(filename):
    sample_path = Path("sample_summary") / f"{filename}_summary.md"
    try:
        with open(sample_path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error loading sample summary: {str(e)}"


st.set_page_config(page_title="readpaper", page_icon="📄")

st.title("ReadPaper")

# Initialize session state for storing the summary and current file name
if "summary" not in st.session_state:
    st.session_state.summary = None
if "current_file_name" not in st.session_state:
    st.session_state.current_file_name = None

# File uploader
uploaded_file = st.file_uploader("Upload your research paper (PDF)", type="pdf")

if uploaded_file:
    # Check if a new file was uploaded
    if st.session_state.current_file_name != uploaded_file.name:
        st.session_state.summary = None  # Reset summary for new file
        st.session_state.current_file_name = (
            uploaded_file.name
        )  # Update current file name
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
        "Please upload a PDF file to begin analysis. Or explore sample summaries below 👇"
    )

    tab1, tab2 = st.tabs(["BERT", "Attention Is All You Need"])

    with tab1:
        with st.expander(
            "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
            expanded=True,
        ):
            bert_summary = load_sample_summary("bert")
            st.markdown(bert_summary)
            # Add citation
            st.markdown(
                """
            ---
            📄 [Original Paper](https://arxiv.org/abs/1810.04805) by Devlin et al. (2018)
            """
            )

    with tab2:
        with st.expander("Attention Is All You Need", expanded=True):
            attention_summary = load_sample_summary("attention")
            st.markdown(attention_summary)
            # Add citation
            st.markdown(
                """
            ---
            📄 [Original Paper](https://arxiv.org/abs/1706.03762) by Vaswani et al. (2017)
            """
            )

with st.sidebar:
    st.header("📚 ReadPaper")

    st.markdown(
        """
        A better paper summary powered by [Claude 3.5 Sonnet](https://www.anthropic.com/claude)
        
        #### 📋 Summary Structure
        • Problem Statement & Significance  
        • Conceptual Innovation  
        • Technical Architecture  
        • Mathematical Foundation  
        • Critical Analysis & Future Work
        
        ---
                
        [![GitHub](https://img.shields.io/badge/GitHub-View_Project-gray?logo=github)](https://github.com/benthecoder/readpaper)
        
        Built by [Benedict Neo](https://www.linkedin.com/in/benedictneo/)  
        DM me on [Twitter](https://twitter.com/benxneo)

        """
    )
