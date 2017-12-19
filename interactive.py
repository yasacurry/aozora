import sys
from gensim.models import word2vec

model_name = sys.argv[1]
model = word2vec.Word2Vec.load(model_name)

print("""model.most_similar(positive=["自分"])""")
print(model.most_similar(positive=["自分"]))