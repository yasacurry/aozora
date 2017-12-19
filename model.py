import sys
from gensim.models import word2vec

wakati_name = sys.argv[1]
model_name = wakati_name + ".model"

data = word2vec.LineSentence(wakati_name)
model = word2vec.Word2Vec(data, size=200, window=10, min_count=2, sg=1)
model.save(model_name)