# readpaper 🔬

AI-powered research paper summaries that capture technical depth and nuance. Powered by Claude 3.5 Sonnet.

## Why readpaper?

readpaper leverages Claude 3.5's advanced capabilities to deliver comprehensive research paper analysis:

- 🔍 **Deep PDF Analysis**: Process papers up to 32MB with native PDF support ([1](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support))
- ⚡ **Performance Optimized**:
  - Token counting for efficient processing ([2](https://docs.anthropic.com/en/docs/build-with-claude/token-counting))
  - Prompt caching for faster repeated analyses ([3](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching))
- 🧠 **Intelligent Processing**:
  - Multi-stage sectional analysis for thorough understanding
  - Progressive context building across sections
  - Research scientist persona for academic-quality insights
  - Token-optimized prompts for maximum context utilization

### How it Works

1. **Sectional Analysis**: Papers are processed in three key stages:

   - Initial overview and context gathering
   - Detailed technical analysis
   - Synthesis and implications

2. **Progressive Understanding**: Each analysis stage builds upon previous insights, creating a coherent and deep understanding of the paper

3. **Research Scientist Approach**: A specialized research persona guides the analysis style, ensuring academic rigor and technical depth

4. **Optimized Processing**:
   - Efficient PDF handling with Claude's beta capabilities
   - Smart caching for faster repeated analyses
   - Token usage monitoring for optimal context management

## Who is this for?

- 📚 Researchers staying current with literature
- 💻 Engineers implementing papers
- 🔧 Teams doing literature reviews
- 📊 Anyone needing deep technical understanding

## Sample Output

Check out sample summaries for [BERT](sample_summary/bert_summary.pdf) and the [attention](sample_summary/attention_summary.pdf) paper

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- uv (recommended) or pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/benthecoder/readpaper.git
cd readpaper
```

2. Create and activate virtual environment with uv:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
uv pip install -r requirements.txt
```

4. Set up environment variables:

```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### Usage

#### Web Interface

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

#### Command Line

Process papers directly from the command line:

```bash
python main.py path/to/your/paper.pdf
```

The summary will be saved in `paper_summaries/` directory.
