class ResearchPrompts:
    @staticmethod
    def get_system_context():
        return """You are a senior research scientist specializing in analyzing technical papers. Your role is to:
1. Ground all analysis in specific quotes from the paper using > blockquotes
2. Maintain rigorous academic standards while making complex concepts accessible
3. Provide balanced critical analysis identifying both strengths and limitations
4. Structure analysis to serve both researchers and practitioners

Format requirements:
- Use > for paper quotes with page/section references
- Use ### for section headers
- Use tables with | for structured comparisons
- Use bullet points for lists
- Start directly with analysis - no introductory text
- Define all technical terms and acronyms on first use"""

    @staticmethod
    def get_prompt(section):
        prompts = {
            "overview": """### Core Problem Statement
First, identify and quote key passages that define:
1. The problem being addressed
2. Current limitations
3. Proposed solution
> [Include 2-3 relevant quotes with section references]

Analysis:
- Current challenges and their significance
- Limitations of existing approaches
- Real-world implications
- Technical constraints

### Key Innovation
Quote passages describing:
1. Main technical contributions
2. Novel aspects
3. Implementation approach
> [Include relevant technical quotes]

Analysis:
- Technical novelty
- Implementation advantages
- Performance improvements
- Resource requirements

### Technical Framework
Component | Innovation | Evidence | Trade-offs | Resource Requirements
---|---|---|---|---
[List 3-4 key technical elements with specific evidence]

### Empirical Validation
Experiment | Method | Results | Statistical Significance | Limitations
---|---|---|---|---
[List key experimental results]

### Initial Assessment
**Key Strengths:**
- List strengths with supporting quotes
- Focus on empirical evidence
- Include performance metrics
- Note resource efficiency

**Limitations & Future Work:**
- List limitations with evidence
- Note computational constraints
- Identify open challenges
- Suggest research directions""",
            "technical": """### Architecture Details
Quote key technical specifications:
1. System architecture
2. Algorithm design
3. Implementation details
> [Include relevant technical quotes]

Analysis:
- Component interactions
- Design decisions and rationale
- Optimization methods
- Resource requirements

### Mathematical Framework
> [Quote relevant equations and mathematical formulations]

Key Elements:
- Training objectives
- Loss functions
- Complexity analysis
- Optimization approach

### Implementation Details
Hardware | Configuration | Performance | Resource Usage
---|---|---|---
[List implementation specifics]

### Empirical Results
Dataset | Size | Preprocessing | Training Time | Results
---|---|---|---|---
[List experimental details]

### Technical Assessment
**Success Factors:**
- Performance enablers
- Critical optimizations
- Scaling considerations
- Resource efficiency

**Implementation Challenges:**
- Technical bottlenecks
- Resource constraints
- Scaling limitations
- Deployment considerations""",
        }
        return prompts.get(section, "")
