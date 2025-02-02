from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import numpy as np
from collections import Counter

# Read text data with explicit encoding
text = open('news1.txt', "r", encoding="utf-8").read()

# Set up jieba dictionary
jieba.set_dictionary('dictionary/dict.txt.big.txt')

# Read stop words
with open('dictionary/stopWord_cloud.txt', 'r', encoding='utf-8-sig') as f:
    stops = f.read().split('\n')
    # Remove any empty strings that might appear from trailing newlines
    stops = [word for word in stops if word.strip()]

# Process terms
terms = []
for t in jieba.cut(text, cut_all=False):
    if t.strip() and t not in stops:  # Check for empty strings and stop words
        terms.append(t)
diction = Counter(terms)

# Create WordCloud with proper settings
font = 'msyh.ttc'
wordcloud = WordCloud(
    font_path=font,
    width=800,
    height=400,
    background_color='white',  # Set white background for better visibility
    # layout_engine='preferred',
    max_words=2000,  # Adjust as needed
    min_font_size=4,
    max_font_size=None    
)

# Generate word cloud
wordcloud.generate_from_frequencies(frequencies=diction)

# Display the word cloud
plt.figure(figsize=(10, 10))  # Larger figure size for better visibility
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# Save the word cloud
wordcloud.to_file("news_Wordcloud.png")