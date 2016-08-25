import logging
import nltk
import gensim
from nltk import corpus

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
save_path = 'C:/Users/51694/PycharmProjects/work2vec_wiki/test_model'


def doc_process(doc):
    new_doc = []
    for i in doc:
        if i.isalpha():
            new_doc.append(i.lower())
    return new_doc


if __name__ == '__main__':
    docs_name = corpus.gutenberg.fileids()
    docs = []
    for i in docs_name:
        doc = doc_process(corpus.gutenberg.words(i))
        docs.append(doc)
    model = gensim.models.Word2Vec(docs)
    model.save(save_path)