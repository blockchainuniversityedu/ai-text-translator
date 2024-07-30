import nltk

try:
    nltk.download('punkt', download_dir='/usr/local/share/nltk_data')
except Exception as e:
    print(f"Error: [e]")