from gensim import corpora, models
import nltk
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

docs_path = 'C:\\Users\\51694\\PycharmProjects\\work2vec_wiki\\docs.txt'
stop_list_path = 'C:\\Users\\51694\\PycharmProjects\\work2vec_wiki\\stop_list.txt'
with open(docs_path) as f:
    docs = [i.strip().lower() for i in f.readlines()]
with open(stop_list_path) as f:
    stop_list = f.read().split()
texts = []
tokens = []
for i in docs:
    text = [j for j in nltk.word_tokenize(i) if j not in stop_list]
    tokens += text
    texts.append(text)
frequency = nltk.FreqDist(tokens)
final_texts = []
for text in texts:
    freq_word = [word for word in text if frequency[word] > 1]
    final_texts.append(freq_word)
# print(final_texts)
word_id = corpora.Dictionary(final_texts)
# print(word_id.token2id)
corpus = [word_id.doc2bow(i) for i in final_texts]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
for i in corpus_tfidf:
    print(i)
