import jieba
import logging
import time
import os

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

docs_path = os.getcwd() + '\\' + 'wikijianzh.txt'
out_path = os.getcwd() + '\\' + 'tokenize_zhwiki.txt'

if __name__ == '__main__':
    zh_docs = []
    count = 0
    with open(docs_path, encoding='utf-8') as f:
        start_time = time.clock()
        for doc in f.readlines()[200000:]:
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
            if count >= 100000:
                break
    end_time = time.clock()
    tokenize_time = end_time - start_time
    print('tokenize totally cost' + str(tokenize_time) + 's')
    print('-----------------tokenize end-----------------------')
    with open(out_path, 'a', encoding='utf-8') as f:
        space = ' '
        count = 0
        for i in zh_docs:
            count += 1
            doc = space.join(i) + "\n"
            f.write(doc)
            if count % 1000 == 0:
                print('doc write' + str(count))
    print('-----------------write end-----------------------')

