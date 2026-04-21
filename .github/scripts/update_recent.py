#!/usr/bin/env python3
import os
import subprocess
import re
from datetime import datetime

MAX_ENTRIES = 8
EXCLUDE_FILES = {"Home.md", "_Sidebar.md", "_Footer.md"}

def get_last_updated_date(filename):
    try:
        result = subprocess.check_output(
            ["git", "log", "-1", "--format=%cd", "--date=short", "--", filename],
            text=True
        ).strip()
        return result
    except subprocess.CalledProcessError:
        return "Unknown"

md_files = [f for f in os.listdir(".") if f.endswith(".md") and f not in EXCLUDE_FILES]

files_with_dates = []
for f in md_files:
    date_str = get_last_updated_date(f)
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        files_with_dates.append((date_obj, date_str, f))
    except:
        files_with_dates.append((datetime.min, date_str, f))

files_with_dates.sort(reverse=True)

lines = ["## Recently Updated", "", "*(Articles updated)*"]
for _, date, filename in files_with_dates[:MAX_ENTRIES]:
    page_name = filename[:-3]
    lines.append(f"- [[{page_name}]] • Last updated: {date}")

new_section = "\n".join(lines) + "\n"

with open("Home.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!-- RECENTLY_UPDATED_START -->.*<!-- RECENTLY_UPDATED_END -->",
    f"<!-- RECENTLY_UPDATED_START -->\n{new_section}<!-- RECENTLY_UPDATED_END -->",
    content,
    flags=re.DOTALL
)

with open("Home.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ Recently Updated section updated")
