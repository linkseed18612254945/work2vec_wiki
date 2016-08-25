import jieba

docs_path = 'C:/Users/Administrator/PycharmProjects/work2vec_wiki/wikijianzh.text'
out_path = 'C:/Users/Administrator/PycharmProjects/work2vec_wiki/train_zhwiki.text'

if __name__ == '__main__':
    zh_docs = []
    with open(docs_path, encoding='utf-8') as f:
        for doc in f.readlines():
            temp_doc = jieba.lcut(doc)
            zh_doc = []
            for word in temp_doc:
                if ord(word[0]) > 127:
                    zh_doc.append(word)
            zh_docs.append(zh_doc)

