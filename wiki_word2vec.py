import gensim
import time
import logging
import os

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
doc_path = os.getcwd() + '\\' + 'tokenize_zhwiki.txt'
model_path = os.getcwd() + '\\' + 'word2vec_zhwiki_model'

if __name__ == '__main__':
    count = 0
    with open(doc_path, encoding='utf-8') as f:
        docs = []
        for i in f.readlines():
            count += 1
            doc = i.split()
            docs.append(doc)
            if count % 3000 == 0:
                print('read doc' + str(count))
    start_time = time.clock()
    print('--------------------training start-------------------')
    wiki_model = gensim.models.Word2Vec(docs)
    cost_time = time.clock() - start_time
    print('training totally cost' + str(cost_time) + 's')
    wiki_model.save(model_path)
    print('mode saved')
