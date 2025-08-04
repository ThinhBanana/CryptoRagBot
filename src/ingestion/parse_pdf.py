import pymupdf
from pathlib import Path


# Read pdf
root = Path(__file__).resolve().parents[2]
(root / "data").mkdir(parents=True, exist_ok=True)
filepath = root / "data" / "bitcoin_whitepaper.pdf"
doc = pymupdf.open(filepath) # open a document

# Parse pdf to plain text
texts = []

with open (root / "data" / "bitcoin_whitepaper_page.txt", 'w', encoding='utf-8') as f:
    for i, page in enumerate(doc.pages()): # iterate the document pages
        text = page.get_text()
        if len(text.strip()) == 0:
            print(f"Page {i+1} is empty.")
        elif len(text.strip()) < 50:
            print(f"Page {i+1} looks very short: '{text.strip()[:30]}...'")
        else:
            texts.append(text)
            f.write(f"\n\n=== Page {i+1} ===\n\n")
            f.write(text)

with open (root / "data" / "bitcoin_whitepaper_full_text.txt", 'w', encoding='utf-8') as f:
    f.write('\n'.join(texts))