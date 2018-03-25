# Functions are first-class objects

from nltk.corpus import stopwords

# Note: For the following example to work, we need to install
# nltk (natural language toolkit) corpus on our local machine
# see https://www.nltk.org/data.html:
# install nltk module: pipenv install nltk
# call method below - choose Collections - `popular` packages
# or command line: sudo python -m nltk.downloader -d /usr/local/share/nltk_data popular
# /usr/local/share/nltk_data (Mac); and /usr/share/nltk_data (Unix)
#
# Such goodies as: http://www.nltk.org/howto/twitter.html


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


def remove_non_words(all_content):
    print('Input size: %d' % len(all_content))
    words = [w for w in all_content if w.isalpha()]
    print('Output size: %d' % len(words))
    return words


def count_frequency(words):
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict


def reverse_sort_by_freq(freq_dict):
    return sorted(freq_dict.items(), key=lambda t: t[1], reverse=True)


def print_results(top_ten):
    tuples = [str(t) for t in top_ten]
    print('\n'.join(tuples))


def step_by_step(emma_all):
    emma_words = remove_non_words(emma_all)
    emma_lower = lower(emma_words)
    emma_nonstop = remove_stopwords(emma_lower)
    emma_freqs = count_frequency(emma_nonstop)
    word_counts = reverse_sort_by_freq(emma_freqs)
    top_ten = word_counts[:10]
    return top_ten


def process_pipeline(emma_all, pipeline):
    result = emma_all
    for p in pipeline:
        result = p(result)
    top_ten = result[:10]
    return top_ten


def main():
    from nltk.corpus import gutenberg
    emma_all = gutenberg.words('austen-emma.txt')
    top_step = step_by_step(emma_all)
    print_results(top_step)

    pipeline = [remove_non_words, lower, remove_stopwords, count_frequency, reverse_sort_by_freq]
    top_pipe = process_pipeline(emma_all, pipeline)
    print_results(top_pipe)


if __name__ == "__main__":
    main()
