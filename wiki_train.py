import jieba
import gensim
import logging
import time
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
save_path = 'C:/Users/51694/PycharmProjects/work2vec_wiki/wiki_model'
docs_path = 'C:/Users/Administrator/PycharmProjects/work2vec_wiki/wikijianzh.text'
out_path = 'C:/Users/Administrator/PycharmProjects/work2vec_wiki/train_zhwiki.text'

if __name__ == '__main__':
    zh_docs = []
    count = 0
    with open(docs_path, encoding='utf-8') as f:
        start_time = time.clock()
        for doc in f.readlines():
            temp_doc = jieba.lcut(doc)
            zh_doc = []
            for word in temp_doc:
                if ord(word[0]) > 127:
                    zh_doc.append(word)
            zh_docs.append(zh_doc)
            count += 1
            if count % 1000 == 0:
                end_time = time.clock()
                cost_time = end_time - start_time
                print('tokenize doc:' + str(count))
                print('cost time:' + str(cost_time) + 's')
    end_time = time.clock()
    tokenize_time = end_time - start_time
    print('tokenize totally cost' + str(tokenize_time) + 's')
    print('-----------------tokenize end-----------------------')
    with open(out_path, encoding='utf-8') as f:
        space = ' '
        for i in zh_docs:
            doc = space.join(i) + "\n"
            f.write(doc)
    print('-----------------write end-----------------------')
    # start_time = time.clock()
    # wiki_model = gensim.models.Word2Vec(zh_docs)
    # cost_time = time.clock() - start_time
    # print('training totally cost' + str(tokenize_time) + 's')
    # wiki_model.save(save_path)
    # print('mode saved')
