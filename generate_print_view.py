#!/usr/bin/env python3
"""
Convert shelf_cut_list_and_plan.md into a print-ready HTML page
with embedded inline SVG blueprint, clean page breaks, and print-optimized CSS.
"""

import re
import markdown

with open("shelf_cut_list_and_plan.md", "r", encoding="utf-8") as f:
    md_content = f.read()

with open("shelf_blueprint.svg", "r", encoding="utf-8") as f:
    svg_content = f.read()

# Replace markdown image reference with inline SVG for crisp vector printing without path issues
pattern = r'!\[.*?\]\(.*?\)'
md_content = re.sub(pattern, '<div class="blueprint-container">' + svg_content + '</div>', md_content, count=1)

# Convert Mermaid diagram code block into a clean styled HTML sequence for printing
mermaid_replacement = """
<div class="assembly-flow">
  <div class="flow-step"><strong>1</strong> Cut Dados in B, C, D</div>
  <div class="flow-arrow">➔</div>
  <div class="flow-step"><strong>2</strong> Attach Runners R to Dividers G</div>
  <div class="flow-arrow">➔</div>
  <div class="flow-step"><strong>3</strong> Glue G between Shelves C &amp; D</div>
  <div class="flow-arrow">➔</div>
  <div class="flow-step"><strong>4</strong> Glue Sides B to C, D, E, F, H</div>
  <div class="flow-arrow">➔</div>
  <div class="flow-step"><strong>5</strong> Mount 2&quot; Top A &amp; Fit Drawers</div>
</div>
"""
md_content = re.sub(r'```mermaid[\s\S]*?```', mermaid_replacement, md_content)

# Convert GitHub blockquotes/alerts to styled callout boxes
md_content = re.sub(
    r'> \[!IMPORTANT\]\s*\n((?:> .*\n?)+)',
    lambda m: '<div class="callout callout-important"><strong>IMPORTANT:</strong> ' + m.group(1).replace('> ', '') + '</div>',
    md_content
)
md_content = re.sub(
    r'> \[!TIP\]\s*\n((?:> .*\n?)+)',
    lambda m: '<div class="callout callout-tip"><strong>SHOP TIP:</strong> ' + m.group(1).replace('> ', '') + '</div>',
    md_content
)

html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

html_full = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Quarter-Sawn Fir Shelf — Printable Shop Plan &amp; Cut List</title>
  <style>
    @page {{
      size: letter portrait;
      margin: 0.5in 0.5in 0.5in 0.5in;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #1a1a1a;
      background: #ffffff;
      margin: 0;
      padding: 0.25in;
      font-size: 10pt;
      line-height: 1.4;
    }}
    .print-actions {{
      margin-bottom: 1rem;
      padding: 0.75rem 1rem;
      background: #f0f4f8;
      border: 1px solid #c2d4e5;
      border-radius: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .print-btn {{
      background: #1e3a5f;
      color: #fff;
      border: none;
      padding: 8px 18px;
      font-size: 13px;
      font-weight: 600;
      border-radius: 4px;
      cursor: pointer;
    }}
    .print-btn:hover {{
      background: #152942;
    }}
    h1 {{
      font-size: 18pt;
      margin-top: 0;
      margin-bottom: 0.4rem;
      color: #2c1d11;
      border-bottom: 2px solid #2c1d11;
      padding-bottom: 4px;
    }}
    h2 {{
      font-size: 13pt;
      margin-top: 1.2rem;
      margin-bottom: 0.4rem;
      color: #2c1d11;
      border-bottom: 1px solid #ccc;
      padding-bottom: 2px;
      page-break-after: avoid;
    }}
    h3 {{
      font-size: 11pt;
      margin-top: 0.8rem;
      margin-bottom: 0.3rem;
      color: #3a2312;
      page-break-after: avoid;
    }}
    .blueprint-container {{
      width: 100%;
      margin: 0.5rem auto 1rem auto;
      text-align: center;
      page-break-inside: avoid;
    }}
    .blueprint-container svg {{
      width: 100%;
      height: auto;
      max-height: 4.8in;
      display: block;
      margin: 0 auto;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 0.6rem 0 1rem 0;
      font-size: 9pt;
      page-break-inside: auto;
    }}
    tr {{
      page-break-inside: avoid;
      page-break-after: auto;
    }}
    th {{
      background: #f4ede4;
      color: #2c1d11;
      font-weight: 700;
      text-align: left;
      padding: 5px 6px;
      border: 1px solid #bda893;
    }}
    td {{
      padding: 4px 6px;
      border: 1px solid #dcd3c8;
      vertical-align: top;
    }}
    tr:nth-child(even) td {{
      background-color: #faf7f2;
    }}
    td:first-child {{
      font-weight: bold;
      text-align: center;
      font-size: 10pt;
    }}
    .callout {{
      padding: 7px 10px;
      margin: 0.6rem 0;
      border-radius: 4px;
      font-size: 8.5pt;
      page-break-inside: avoid;
    }}
    .callout-important {{
      background: #fef3e7;
      border-left: 4px solid #d97706;
      color: #78350f;
    }}
    .callout-tip {{
      background: #eef8f2;
      border-left: 4px solid #16a34a;
      color: #14532d;
    }}
    .assembly-flow {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 6px;
      margin: 0.6rem 0;
      padding: 8px;
      background: #faf7f2;
      border: 1px solid #dcd3c8;
      border-radius: 4px;
      page-break-inside: avoid;
    }}
    .flow-step {{
      background: #fff;
      border: 1px solid #bda893;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 8.5pt;
    }}
    .flow-step strong {{
      background: #2c1d11;
      color: #fff;
      display: inline-block;
      width: 16px;
      height: 16px;
      line-height: 16px;
      text-align: center;
      border-radius: 50%;
      margin-right: 3px;
      font-size: 8pt;
    }}
    .flow-arrow {{
      font-size: 11pt;
      color: #8c6d4f;
      font-weight: bold;
    }}
    ul, ol {{
      margin: 0.3rem 0;
      padding-left: 1.2rem;
    }}
    li {{
      margin-bottom: 0.25rem;
    }}
    .page-break-before {{
      page-break-before: always;
    }}
    @media print {{
      body {{
        padding: 0;
      }}
      .print-actions {{
        display: none !important;
      }}
      a {{
        text-decoration: none;
        color: inherit;
      }}
    }}
  </style>
</head>
<body>
  <div class="print-actions">
    <div>
      <strong>Shop Print View:</strong> Pre-formatted with page margins, vector blueprint, and clear tables.
    </div>
    <button class="print-btn" onclick="window.print()">Print / Save to PDF (Ctrl+P)</button>
  </div>
  {html_body}
</body>
</html>
"""

with open("shelf_print_view.html", "w", encoding="utf-8") as f:
    f.write(html_full)

print("Generated shelf_print_view.html successfully.")

