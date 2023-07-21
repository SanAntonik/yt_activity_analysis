import re
import nltk


def preprocess(text):
    """
    Summary:
        Preprocesses the input text by removing non-alphanumeric characters,
        converting to lowercase, tokenizing, and filtering out stopwords.

    Parameters:
        text (str): Input text to be preprocessed.

    Returns:
        str: Preprocessed text after removing non-alphanumeric characters,
        converting to lowercase, tokenizing, and filtering out stopwords.
    """
    # Split the text into sentences using
    # newline and tab characters as separators
    sentences = re.split("[\n\t]", text)
    # Remove any empty lines from the list of sentences
    sentences = [sentence for sentence in sentences if sentence]
    # Further cleaning: Remove non-alphanumeric characters
    # and convert to lowercase
    sentences = [re.sub(r"[^0-9a-zA-Z\s]", "", sentence,
                        re.I | re.A).lower() for sentence in sentences]
    # Lowercase and strip leading/trailing whitespaces for each sentence
    sentences = [sentence.lower().strip() for sentence in sentences]
    # Tokenize each sentence using WordPunctTokenizer from NLTK
    wpt = nltk.WordPunctTokenizer()
    # Get the list of stopwords in English from NLTK
    stop_words = nltk.corpus.stopwords.words("english")
    output = []
    # For each sentence, tokenize and filter out stopwords
    # to create a new list of tokens
    for sentence in sentences:
        tokens = wpt.tokenize(sentence)
        filtered_tokens = [
            token for token in tokens if token not in stop_words]
        # Join the filtered tokens into a sentence
        # Then append it to the output list
        output.append(" ".join(filtered_tokens))
    # Join all the processed sentences into a single text string
    return " ".join(output)
