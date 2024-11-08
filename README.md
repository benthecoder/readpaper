# readpaper 🔬

Instantly generate PhD-level research paper summaries powered by Claude 3.5 Sonnet. Built for researchers and practitioners who need deep technical analysis, fast.

## ✨ Key Features

- **Intelligent Analysis**: Automatically extracts core problems, innovations, and technical details
- **Evidence-Based**: Every insight backed by direct paper quotes and references
- **Technical Depth**: Detailed architecture analysis, mathematical frameworks, and empirical results
- **Resource-Aware**: Includes implementation requirements and computational trade-offs
- **PDF Support**: Handles research papers up to 32MB with native PDF processing

## 🎯 Perfect For

- 📚 Academic Researchers
- 💻 ML Engineers
- 🔧 Industry Practitioners
- 📊 Research Teams

## 🚀 Why This Matters

Traditional paper analysis is time-consuming and can miss critical details. This tool:

- Cuts analysis time from hours to minutes
- Ensures consistent, structured evaluation
- Captures both high-level insights and technical nuances
- Generates publication-ready summaries

## 📊 Output Format

- Core Problem Analysis
- Technical Framework
- Implementation Details
- Empirical Results
- Future Research Directions

## 🛠️ Built With

- Claude 3.5 Sonnet (Latest API)
- PDF Processing Beta Features
- Prompt Caching for Efficiency
- Markdown-based Output

I'll help you add installation and setup instructions to the README. I'll reference the existing requirements and code structure from the provided files.

Here's the additional content to add to the README:

````markdown
## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- uv (recommended) or pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/benthecoder/readpaper.git
cd readpaper
```
````

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

### Sample Output

Check out [`sample_summary/word2vec.pdf`](sample_summary/word2vec.pdf) for an example of the generated analysis format.

## 📝 Output Structure

Each summary includes:

1. Core Problem Analysis

   - Problem statement
   - Current limitations
   - Proposed solution

2. Technical Framework

   - Architecture details
   - Mathematical foundations
   - Implementation specifics

3. Critical Evaluation
   - Empirical results
   - Strengths and limitations
   - Future research directions
