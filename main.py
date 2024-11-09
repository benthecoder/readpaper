import base64
import logging
import os
import sys
from datetime import datetime
from pathlib import Path

import streamlit as st
from anthropic import Anthropic
from dotenv import load_dotenv
from tqdm import tqdm

from prompts import ResearchPrompts

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


class Sumrize:
    def __init__(self):
        load_dotenv()
        api_key = st.secrets.get("ANTHROPIC_API_KEY", os.getenv("ANTHROPIC_API_KEY"))
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY not found in Streamlit secrets or environment variables"
            )

        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")

        self.client = Anthropic(api_key=api_key)
        self.model = "claude-3-5-sonnet-20241022"
        self.analytics = {"token_counts": {}, "total_tokens": 0}

    def _encode_pdf(self, pdf_path):
        """Convert PDF to base64 encoding."""
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode("utf-8")

    def summarize_section(self, pdf_base64, section):
        """Generate summary for a specific section."""
        # Get prompts
        system_context = ResearchPrompts.get_system_context()
        prompt = ResearchPrompts.get_prompt(section)

        # Ensure prompt is not empty
        if not prompt:
            raise ValueError(f"Empty prompt for section: {section}")

        try:
            # Count tokens first (without caching)
            response = self.client.beta.messages.count_tokens(
                betas=["token-counting-2024-11-01", "pdfs-2024-09-25"],
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "document",
                                "source": {
                                    "type": "base64",
                                    "media_type": "application/pdf",
                                    "data": pdf_base64,
                                },
                            },
                            {"type": "text", "text": prompt},
                        ],
                    }
                ],
            )

            if hasattr(response, "usage"):
                self.analytics["token_counts"][section] = response.input_tokens
                logger.info(
                    f"Section {section}: {response.input_tokens:,} input tokens"
                )

        except Exception as e:
            logger.warning(f"Token counting failed: {str(e)}")

        try:
            # Use beta messages endpoint for PDF support
            response = self.client.beta.messages.create(
                model=self.model,
                max_tokens=4096,
                temperature=0,
                system=system_context,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "document",
                                "source": {
                                    "type": "base64",
                                    "media_type": "application/pdf",
                                    "data": pdf_base64,
                                },
                                "cache_control": {"type": "ephemeral"},
                            },
                            {"type": "text", "text": prompt},
                        ],
                    }
                ],
                betas=[
                    "pdfs-2024-09-25",
                    "prompt-caching-2024-07-31",  # Enable prompt caching
                ],
            )

            if hasattr(response, "usage"):
                used_tokens = getattr(response.usage, "input_tokens", 0)
                self.analytics["total_tokens"] += used_tokens
                logger.info(f"Section {section} actual usage: {used_tokens:,} tokens")

            return response.content[0].text

        except Exception as e:
            raise Exception(f"Error generating {section} summary: {str(e)}")

    def summarize(self, pdf_path):
        """Generate a complete paper summary using sectional analysis."""
        if not Path(pdf_path).exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        # Check file size
        file_size = Path(pdf_path).stat().st_size
        if file_size > 32 * 1024 * 1024:  # 32MB
            raise ValueError("PDF file size exceeds 32MB limit")

        logger.info(f"Processing paper: {pdf_path}")
        pdf_base64 = self._encode_pdf(pdf_path)

        sections = ["overview", "technical", "critique"]
        summary_parts = []
        previous_summaries = ""

        # Create progress bar
        pbar = tqdm(sections, desc="Generating summary", unit="section")

        for section in pbar:
            pbar.set_description(f"Processing {section}")
            try:
                # Add previous summaries as context
                section_prompt = ResearchPrompts.get_prompt(section)
                if previous_summaries:
                    section_prompt = f"""Previous section summaries:
    {previous_summaries}

    Using the context above, {section_prompt}"""

                section_summary = self.summarize_section(pdf_base64, section_prompt)
                if section_summary:
                    summary_parts.append(section_summary)
                    # Update context for next section
                    previous_summaries += f"\n\n{section}: {section_summary}"
                else:
                    logger.warning(f"Empty summary for section: {section}")
            except Exception as e:
                logger.error(f"Error in section {section}: {str(e)}")
                continue

        complete_summary = "\n\n".join(summary_parts)
        logger.info(f"Total tokens used: {self.analytics['total_tokens']:,}")
        return complete_summary

    def save_summary(self, pdf_path, summary):
        """Save the summary to a markdown file."""
        pdf_name = Path(pdf_path).stem
        output_dir = Path("paper_summaries")
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / f"{pdf_name}_summary.md"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary)

        logger.info(f"Summary saved to: {output_path}")
        return output_path


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Summarize AI research papers with PDF support and prompt caching"
    )
    parser.add_argument("pdf_path", help="Path to the PDF file")
    args = parser.parse_args()

    try:
        summarizer = Sumrize()
        summary = summarizer.summarize(args.pdf_path)
        output_path = summarizer.save_summary(args.pdf_path, summary)
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
