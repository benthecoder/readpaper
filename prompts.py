class ResearchPrompts:
    @staticmethod
    def get_system_context():
        return """You are a senior research scientist specializing in analyzing technical papers, including both text and visual content. Your role is to:
1. Ground all analysis in specific quotes and visual references from the paper using > blockquotes for text
2. Maintain rigorous academic standards while making complex concepts accessible
3. Provide balanced critical analysis identifying both strengths and limitations
4. Structure analysis to serve both researchers and practitioners
5. Analyze figures, tables, and diagrams to extract key insights

Format requirements:
- Use > for paper quotes with page/section references
- Reference figures using italics with page numbers (e.g., *Figure 1, p.3*)
- Use ### for section headers
- Use tables with | for structured comparisons
- Use bullet points for lists
- Start directly with analysis - no introductory text
- Define all technical terms and acronyms on first use"""

    @staticmethod
    def get_prompt(section):
        prompts = {
            "overview": """### Core Problem Statement
First, identify and quote key passages and relevant figures that define:
1. The problem being addressed
2. Current limitations
3. Proposed solution
> [Include 2-3 relevant quotes with section references]
*Reference key diagrams/figures that illustrate the problem with page numbers*

Analysis:
- Current challenges and their significance
- Limitations of existing approaches
- Real-world implications
- Technical constraints

### Key Innovation
Quote passages and reference figures describing:
1. Main technical contributions
2. Novel aspects
3. Implementation approach
> [Include relevant technical quotes]
*Reference architecture diagrams or methodology figures with page numbers*

Analysis:
- Technical novelty
- Implementation advantages
- Performance improvements
- Resource requirements

### High-Level Results
Results | Supporting Evidence | Impact
---|---|---
[List 2-3 key results with supporting quotes and figure references]""",
            "technical": """### Architecture Details
Quote key technical specifications and reference relevant diagrams:
1. System architecture
2. Algorithm design
3. Implementation details
> [Include relevant technical quotes]
*Reference and analyze system diagrams with page numbers*

Analysis:
- Component interactions
- Design decisions and rationale
- Optimization methods
- Resource requirements

### Mathematical Framework
> [Quote relevant equations and mathematical formulations]
*Reference and explain key mathematical figures/tables with page numbers*

Key Elements:
- Training objectives
- Loss functions
- Complexity analysis
- Optimization approach

### Empirical Results
Dataset | Size | Results | Training Time | Performance
---|---|---|---|---
[List experimental details with references to figures and tables]

### Implementation Details
Hardware | Configuration | Performance | Resource Usage
---|---|---|---
[List implementation specifics with references to results]""",
            "critique": """### Critical Analysis
Quote passages and reference figures highlighting:
1. Main strengths
2. Key limitations
3. Performance trade-offs
> [Include balanced selection of quotes]
*Reference relevant performance graphs/comparisons with page numbers*

### Strengths Assessment
Strength | Evidence | Validation | Impact
---|---|---|---
[List 3-4 key strengths with supporting quotes and figure references]

### Limitations Analysis
Limitation | Impact | Evidence | Potential Solutions
---|---|---|---
[List 3-4 key limitations with evidence]

### Future Directions
Research Direction | Rationale | Current Evidence | Requirements
---|---|---|---
[List 3-4 promising future directions]

### Final Assessment
**Key Contributions:**
- List major advances with evidence
- Note technical innovations
- Highlight practical impact

**Open Challenges:**
- List remaining issues
- Note resource constraints
- Identify research gaps""",
        }
        return prompts.get(section, "")
