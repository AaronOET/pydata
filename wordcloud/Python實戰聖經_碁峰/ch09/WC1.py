from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from collections import Counter
from PIL import Image
import numpy as np
import requests

text = open('travel.txt', "r", encoding="utf-8").read()
jieba.set_dictionary('dict.txt.big.txt')
with open('stopWord_cloud.txt', 'r', encoding='utf-8-sig') as f:
  # with open('stopWord_cloudmod.txt', 'r', encoding='utf-8-sig') as f:
  stops = f.read().split('\n')
terms = []
for t in jieba.cut(text, cut_all=False):
  if t not in stops:
    terms.append(t)
diction = Counter(terms)
fontfile = requests.get(
    "https://drive.google.com/uc?id=1QdaqR8Setf4HEulrIW79UEV_Lg_fuoWz&export=download"
)
with open('taipei_sans_tc_beta.ttf', 'wb') as f:
  f.write(fontfile.content)
wordcloud = WordCloud(font_path='taipei_sans_tc_beta.ttf')
#mask = np.array(Image.open("heart.png"))
#wordcloud = WordCloud(background_color="white",mask=mask,font_path='taipei_sans_tc_beta.ttf')
wordcloud.generate_from_frequencies(frequencies=diction)
# plt.figure(figsize=(10, 10))
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()
# wordcloud.to_file("bookCloud.png")
