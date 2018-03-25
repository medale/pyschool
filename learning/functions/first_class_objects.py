# Functions are first-class objects

from nltk.corpus import stopwords

# Note: For the following example to work, we need to install
# nltk (natural language toolkit) corpus on our local machine
# see https://www.nltk.org/data.html:
# install nltk module: pipenv install nltk
# call method below - choose Collections - `popular` packages
# or command line: sudo python -m nltk.downloader -d /usr/local/share/nltk_data popular
# /usr/local/share/nltk_data (Mac); and /usr/share/nltk_data (Unix)
def install_nltk_corpus():
    import nltk
    nltk.download()


def remove_stopwords(lower_case_words):
    """
    Removes stop words from our list of words.
    :param words: All words must be lower case
    :return: list of words that were not on english stopword list
    """
    english_stopwords = stopwords.words('english')
    non_stopwords = [w for w in lower_case_words if w not in english_stopwords]
    return non_stopwords


def lower(words):
    return [w.lower() for w in words]


def count_frequency(words):
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict


def main():
    from nltk.corpus import gutenberg
    emma_words = gutenberg.words('austen-emma.txt')
    

if __name__== "__main__":
    main()
