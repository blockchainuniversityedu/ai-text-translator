from fetch_and_extract import fetch_webpage, extract_text
from keyword_extraction import extract_keywords
from highlight_keywords import highlight_keywords

def main(url):
    # Fetch and extract text from webpage
    html_content = fetch_webpage(url)
    text = extract_text(html_content)

    # Extract keywords
    keywords = extract_keywords(text)

    # Highlight keywords in the text
    highlight_text = highlight_keywords(text, keywords)

    # Output results
    print("Extracted Keywords:", keywords)
    print("Highlighted Text:\n", highlight_text)

if __name__ == "__main__":
    url = 'https://example.com'
    main(url)