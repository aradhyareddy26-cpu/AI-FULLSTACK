from sentence_transformers import       util,SentenceTransformers 
model = sentenceTransformer ("all-MiniLM-L6-v2")
sentence=[
    "I love playing football",
    "zzi enjoy playing  soccer",
    " I like eating pizza"
]
sentence_embedding - model.encode(sentences)
similarity1 = util.cos_sim(sentenccce)
]