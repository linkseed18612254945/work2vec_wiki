import logging
import gensim
import time

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if __name__ == '__main__':
    in_path = 'C:/Users/Administrator/PycharmProjects/work2vec_wiki/zhwiki-latest-pages-articles.xml.bz2'
    out_path = 'C:/Users/Administrator/PycharmProjects/work2vec_wiki/zhwiki.txt'
    space = " "
    i = 0
    with open(out_path, 'w', encoding='utf-8') as f:
        start_time = time.clock()
        wiki = gensim.corpora.WikiCorpus(in_path, lemmatize=False, dictionary={})
        for text in wiki.get_texts():
            doc = []
            for j in text:
                doc.append(j.decode('utf-8', 'ignore'))
            doc = space.join(doc) + "\n"
            f.write(doc)
            i = i + 1
            if (i % 1000 == 0):
                end_time = time.clock()
                cost_time = end_time - start_time
                print('saved' + str(i) + 'docs.')
                print('cost time:' + str(cost_time) + 's')
    print("Finished Saved " + str(i) + " articles")