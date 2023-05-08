import re
import nltk


def preprocess(text):
    sentences = re.split("[\n\t]", text)
    # remove empty lines
    sentences = [sentence for sentence in sentences if sentence]
    # further cleaning
    sentences = [re.sub(r"[^0-9a-zA-Z\s]", "", sentence,
                        re.I | re.A).lower() for sentence in sentences]
    sentences = [sentence.lower().strip() for sentence in sentences]
    wpt = nltk.WordPunctTokenizer()
    stop_words = nltk.corpus.stopwords.words("english")
    output = []
    for sentence in sentences:
        tokens = wpt.tokenize(sentence)
        filtered_tokens = [
            token for token in tokens if token not in stop_words]
        output.append(" ".join(filtered_tokens))
    return " ".join(output)
