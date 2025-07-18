import requests
import os

urls = ['https://www.gutenberg.org/cache/epub/50373/pg50373.txt']

os.makedirs("text", exist_ok=True)  # Create the directory if it doesn't exist

for i in range(len(urls)):
    response = requests.get(urls[i])
    if response.status_code == 200:
        with open(f'text/text-content-{i}.txt', 'w', encoding='utf-8') as f:
            f.write(response.text)
    else:
        print(f"Failed to download: {urls[i]} (Status code: {response.status_code})")
