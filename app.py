import os
import markdown

# Folders
DOCS_DIR = "docs"
SITE_DIR = "site"

# Create site folder if not exists
os.makedirs(SITE_DIR, exist_ok=True)

# Simple CSS
css = """
body {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: auto;
    padding: 20px;
    line-height: 1.6;
    background: #f4f4f4;
}

h1, h2, h3 {
    color: #333;
}

a {
    color: blue;
    text-decoration: none;
}
"""

# Save CSS file
with open(os.path.join(SITE_DIR, "style.css"), "w") as f:
    f.write(css)

# Store links for index.html
links = []

# Read all markdown files
for filename in os.listdir(DOCS_DIR):

    if filename.endswith(".md"):

        md_path = os.path.join(DOCS_DIR, filename)

        # Read markdown content
        with open(md_path, "r", encoding="utf-8") as f:
            md_text = f.read()

        # Convert markdown to HTML
        html_content = markdown.markdown(md_text)

        # Output HTML filename
        html_filename = filename.replace(".md", ".html")
        html_path = os.path.join(SITE_DIR, html_filename)

        # Full HTML page
        full_html = f"""
        <html>
        <head>
            <title>{filename}</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """

        # Save HTML file
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(full_html)

        # Add link for index page
        links.append(f'<li><a href="{html_filename}">{filename}</a></li>')

# Create index.html
index_html = f"""
<html>
<head>
    <title>Documentation</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Documentation Pages</h1>
    <ul>
        {''.join(links)}
    </ul>
</body>
</html>
"""

# Save index.html
with open(os.path.join(SITE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("Site generated successfully!")