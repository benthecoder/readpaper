import markdown2
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration


def create_markdown_pdf(summary):
    # Convert markdown to HTML with extras enabled
    html = markdown2.markdown(
        summary,
        extras=[
            "tables",
            "numbering",
            "cuddled-lists",
            "break-on-newline",
            "smarty-pants",
        ],
    )

    # Enhanced CSS with smaller margins and better list formatting
    css = """
        body { 
            font-family: "Arial", "Microsoft YaHei", "SimSun", "SimHei", sans-serif; 
            margin: 1cm;
            line-height: 1.4; 
        }
        table { 
            border-collapse: collapse; 
            width: 100%; 
            margin: 0.5em 0; 
        }
        th, td { 
            border: 1px solid #ddd; 
            padding: 6px; 
            text-align: left; 
        }
        ol, ul { 
            padding-left: 15px;
            margin: 0.3em 0;
        }
        li {
            margin: 0.2em 0;
        }
        /* Ensure nested lists are properly indented */
        li > ul, li > ol {
            margin-left: 15px;
        }
        blockquote {
            border-left: 3px solid #666;
            margin: 1em 0;
            padding: 0.5em 1em;
            background-color: #f5f5f5;
        }
    """

    # Create HTML document
    html_content = f"""
        <html>
            <head>
                <style>{css}</style>
            </head>
            <body>
                {html}
            </body>
        </html>
    """

    # Configure fonts and generate PDF
    font_config = FontConfiguration()
    pdf_data = HTML(string=html_content).write_pdf(
        font_config=font_config, presentational_hints=True
    )

    return pdf_data
