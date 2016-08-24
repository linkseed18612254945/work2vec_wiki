import gensim

model_path = 'C:/Users/51694/PycharmProjects/work2vec_wiki/test_model'
new_model = gensim.models.Word2Vec.load(model_path)
print(new_model['man'])
print(new_model.similarity('man', 'man'))