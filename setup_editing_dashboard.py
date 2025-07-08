import nbformat as nbf
import os

# Create notebooks folder if it doesn't exist
os.makedirs('notebooks', exist_ok=True)

nb = nbf.v4.new_notebook()

nb['cells'] = [
    nbf.v4.new_markdown_cell(
        "# 📖 The Beginning – Editing Dashboard\n"
        "This notebook is your command center for red-pen edits, reflections, and quantum rewriting.\n"
        "\n"
        "## Usage:\n"
        "- Cell 1: Invocation / Intention\n"
        "- Cell 2: Current text chunk\n"
        "- Cell 3: Edits / Revision ideas\n"
        "- Cell 4: Reflections / Thematic notes\n"
        "- Cell 5+: Free space\n"
    ),
    nbf.v4.new_markdown_cell(
        "## ✨ Invocation / Intention\n"
        "> \"I dedicate this editing session to truth, clarity, and planetary healing. May my words rewrite reality with honesty and art.\""
    ),
    nbf.v4.new_markdown_cell(
        "## 📜 Current Text Chunk\n"
        "Paste the text you're working on here."
    ),
    nbf.v4.new_code_cell(
        "# ✅ Edit Suggestions:\n"
        "''' \n"
        "Rewrite your text here, line by line if you want.\n"
        "You can also leave multiple variations to consider.\n"
        "'''"
    ),
    nbf.v4.new_markdown_cell(
        "## 🪶 Reflections / Notes\n"
        "- Subtext?\n"
        "- Themes?\n"
        "- Character psychology?\n"
        "- Scene purpose?\n"
    ),
    nbf.v4.new_markdown_cell(
        "## 🔖 Free Space / Scratchpad\n"
        "Use this section for any random thoughts or notes."
    )
]

with open('notebooks/EditingDashboard.ipynb', 'w') as f:
    nbf.write(nb, f)

print("✅ EditingDashboard.ipynb created in notebooks/")
