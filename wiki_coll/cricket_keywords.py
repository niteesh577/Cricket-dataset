import requests
from bs4 import BeautifulSoup
import json

def extract_wikipedia_glossary(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    content_div = soup.find('div', class_='mw-parser-output')
    glossary_data = []

    current_term = None
    description_parts = []

    for tag in content_div.find_all(['h2', 'h3', 'dt', 'dd', 'p']):
        if tag.name == 'dt':
            # Save previous term if any
            if current_term and description_parts:
                glossary_data.append({
                    "keyword": current_term.strip(),
                    "content": ' '.join(description_parts).strip()
                })
                description_parts = []

            current_term = tag.get_text(strip=True)

        elif tag.name == 'dd' or tag.name == 'p':
            if current_term:
                description_parts.append(tag.get_text(strip=True))

    # Catch the last term
    if current_term and description_parts:
        glossary_data.append({
            "keyword": current_term.strip(),
            "content": ' '.join(description_parts).strip()
        })

    return glossary_data

# URL of the cricket glossary
url = "https://en.wikipedia.org/wiki/Glossary_of_cricket_terms"
glossary_terms = extract_wikipedia_glossary(url)

# Save as JSON file
with open("cricket_glossary.json", "w", encoding="utf-8") as f:
    json.dump(glossary_terms, f, indent=2, ensure_ascii=False)

# Optional: also save in JSONL format for LLM fine-tuning
with open("cricket_glossary.jsonl", "w", encoding="utf-8") as f:
    for item in glossary_terms:
        json.dump(item, f, ensure_ascii=False)
        f.write("\n")

print(f"Extracted {len(glossary_terms)} glossary terms.")
