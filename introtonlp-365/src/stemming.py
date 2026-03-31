from nltk.stem import PorterStemmer

# stemming es una técnica de reducir la cantidad de palabras que se usan en una oración

ps = PorterStemmer()

sentence = "The quick brown fox jumps over the lazy dog"
connect_tokens = [
    "connecting",
    "connects",
    "connected",
    "connect",
    "connectivity",
]

learn_tokens = [
    "learning",
    "learn",
    "learns",
    "learned",
    # "learnability",
    # "learnable",
    "learner",
    "learners",
]

likes_tokens = [
    "like",
    "likes",
    "liked",
    "liking",
    "better",
    "worse",
    "liked",
    "liker",
    "likers",
]

for t in likes_tokens:
    print(t, "->", ps.stem(t))
