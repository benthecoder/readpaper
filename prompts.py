class ResearchPrompts:
    @staticmethod
    def get_system_context():
        return """You are a senior research scientist specializing in analyzing technical papers. Your role is to:
    1. Build upon previous section analyses when provided
    2. Provide distinct, non-overlapping analysis for each section
    3. Ground all analysis in specific quotes and visual references
    4. Maintain academic rigor while ensuring accessibility
    5. Focus each section on its core purpose without repetition
    6. Reference relevant insights from previous sections when applicable

    Format requirements:
    - Use > for paper quotes with page/section references
    - Reference figures using italics with page numbers (e.g., *Figure 1, p.3*)
    - Use ### for section headers
    - Use bullet points for lists
    - Define technical terms on first use only
    - When referencing previous sections, use [Previous Section: insight] format"""

    @staticmethod
    def get_prompt(section):
        prompts = {
            "overview": """Analyze the paper's core contributions and significance. If this is the first section, focus on establishing a foundation for later sections.

### Problem Statement
- Core challenge being addressed
- Significance and impact
> [Quote defining problem statement]

### Conceptual Innovation
- Novel approach overview
- Key differentiators
*Reference main concept figure*

### High-Level Results
Impact | Improvement | Significance
---|---|---
[Key quantitative improvements]""",
            "technical": """Building on the overview section's foundation, provide a detailed technical analysis. Reference specific aspects mentioned in the overview where relevant.

### Technical Architecture
- System components and interactions [Reference overview's conceptual model]
- Data flow pipeline
*Reference architecture diagrams*

### Mathematical Foundation
- Core algorithms supporting the innovations described in overview
- Theoretical proofs
- Complexity analysis
> [Include key equations]

### Implementation Details
Dataset | Method | Metrics
---|---|---
[Technical specifications aligned with overview results]""",
            "critique": """Using insights from both the overview and technical sections, provide a comprehensive critique.

### Critical Analysis
Strength [from previous sections] | Limitation | Future Work
---|---|---
[Balanced evaluation referencing previous sections]

### Research Impact
- Scientific contributions [tied to overview's significance]
- Industry applications [based on technical feasibility]
- Open challenges [considering technical limitations]

### Future Research
Direction | Motivation [from previous analysis] | Requirements
---|---|---
[Research opportunities building on full context]""",
        }
        return prompts.get(section, "")
