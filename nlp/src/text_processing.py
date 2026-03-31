import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re
import pandas as pd
from pathlib import Path

nltk.download("stopwords")

csv = Path("../txt_files/tripadvisor_hotel_reviews.csv")
print("my path:", csv)

data = pd.read_csv(csv)

# df = data.head()
# print(df["Review"][0])

# when creating new rows, use the data object, not the dataframe (df)
data["review_lowercase"] = data["Review"].str.lower()

# add new column with stopwords removed
en_stopwords = stopwords.words("english")
en_stopwords.remove("not")
data["review_no_stopwords"] = data["review_lowercase"].apply(
    lambda x: " ".join([word for word in x.split() if word not in en_stopwords])
)

# using regex to cleanup
# axis: tells go to the data row by row
data["review_no_stopwords_no_punct"] = data.apply(
    lambda x: re.sub(r"[*]", "star", x["review_no_stopwords"]), axis=1
)

# remove punctuation
data["review_no_stopwords_no_punct"] = data.apply(
    lambda x: re.sub(r"[^\w\s]", "", x["review_no_stopwords_no_punct"]), axis=1
)

print(data["review_no_stopwords_no_punct"])
