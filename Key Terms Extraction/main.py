import string

import nltk as nltk
from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

list_of_article = []


def lemma(text):
    stemmer = WordNetLemmatizer()
    stop_words = stopwords.words('english') + ['ha', 'wa', 'u', 'a'] + list(string.punctuation)
    lemma_text = [stemmer.lemmatize(word) for word in text]
    normal_text = [word for word in lemma_text if word not in stop_words]

    noun_word = [word for word in normal_text if nltk.pos_tag([word])[0][1] == 'NN']
    list_of_article.append(" ".join(noun_word))


def tf_idf(text):
    vectorized = TfidfVectorizer(input='content', analyzer='word')
    weighted_matrix = vectorized.fit_transform(text)
    terms = vectorized.get_feature_names_out()
    tfidf_matrix = weighted_matrix.toarray()
    for articles_metric in tfidf_matrix:
        some_list = []
        for term, metric in zip(terms, articles_metric):
            some_list.append((term, metric))

        some_list.sort(reverse=True)
        some_list.sort(key=lambda x: x[1], reverse=True)

        yield [i[0] for i in some_list[:5]]


def main():
    xml_file = 'news.xml'
    parse_xml = etree.parse(xml_file).getroot()
    articles = parse_xml[0]
    for article in articles:
        lemma(word_tokenize(article[1].text.lower()))

    terms = tf_idf(list_of_article)
    for i in articles:
        print(i[0].text + ':')
        print(*(next(terms)))


if __name__ == '__main__':
    main()