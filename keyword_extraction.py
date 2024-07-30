import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(text, num_keywords=5):
    # Tokenize the text and convert to lowercase
    words = word_tokenize(text.lower())
    # Remove stopwords and non-alphabetic words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in stop_words]
    # Count word frequencies and return the most common keywords
    word_freq = Counter(words)
    return [word for word, freq in word_freq.most_common(num_keywords)]
