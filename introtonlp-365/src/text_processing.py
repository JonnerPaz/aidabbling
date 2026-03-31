import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re
import pandas as pd
from pathlib import Path

csv = Path("../txt_files/tripadvisor_hotel_reviews.csv")

data = pd.read_csv(csv)
# data.info()

df = data.head()
df["review_lowercase"] = df["Review"].str.lower()
en_stopwords = stopwords.words("english")
en_stopwords.remove("not")
df["review_no_stopwords"] = df["review_lowercase"].apply(
    lambda x: " ".join([word for word in x.split() if word not in en_stopwords])
)
