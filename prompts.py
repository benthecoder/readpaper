class ResearchPrompts:
    @staticmethod
    def get_system_context():
        return """You are a senior research scientist specializing in analyzing technical papers, including both text and visual content. Your role is to:
1. Ground all analysis in specific quotes and visual references from the paper
2. Maintain rigorous academic standards while making complex concepts accessible
3. Structure analysis to serve both researchers and practitioners
4. Analyze figures, tables, and diagrams to extract key insights

Format requirements:
- Use > for paper quotes with page/section references
- Reference figures using italics with page numbers (e.g., *Figure 1, p.3*)
- Use ### for section headers
- Use bullet points for lists
- Start directly with analysis - no introductory text
- Define all technical terms and acronyms on first use"""

    @staticmethod
    def get_prompt(section):
        prompts = {
            "overview": """### Problem Context
Identify the core problem and motivation:
1. What real-world challenge is being addressed?
2. Why is this problem significant?
> [Quote key problem statements]

### Proposed Solution
High-level description of the approach:
1. What is the main idea?
2. How does it address the problem?
*Reference key conceptual figures*

### Key Findings
List only the top 2-3 results that demonstrate solution effectiveness:
Results | Impact
---|---
[Key findings with minimal technical detail]""",
            "technical": """### System Architecture
Analyze the technical implementation:
1. Component design
2. Data flow
3. Key algorithms
*Reference and analyze system diagrams*

### Mathematical Framework
Detailed analysis of:
1. Formal problem definition
2. Theoretical foundations
3. Algorithm complexity
> [Include key equations and proofs]

### Experimental Setup
Dataset | Hardware | Parameters | Metrics
---|---|---|---
[Complete experimental details]

### Performance Analysis
Comprehensive results across all metrics:
1. Quantitative benchmarks
2. Ablation studies
3. Statistical significance
*Reference all results figures/tables*""",
            "critique": """### Comparative Analysis
Compare with existing approaches:
1. Technical advantages
2. Performance gains
3. Resource requirements
> [Include balanced evidence]

### Limitations Assessment
Limitation | Impact | Mitigation
---|---|---
[Analyze core limitations]

### Research Implications
1. Scientific contributions
2. Practical applications
3. Industry impact

### Future Directions
Direction | Rationale | Requirements
---|---|---
[Strategic research opportunities]""",
        }
        return prompts.get(section, "")
