from sentence_transformers import SentenceTransformer
import chromadb
model = SentenceTransformer("all-MiniLM-L6-v2")
file_name = "ai_sample.txt"
print("Model loaded successfully.")
with open("ai_sample.txt", "r") as file:
    text = file.read()
# print(text)
# print("No of characters:",len(text))
chunks=[]
chunk_size = 25
chunk_overlap=10
step = chunk_size - chunk_overlap
for i in range(0,len(text),step):
    chunk=text[i:i+chunk_size]
    chunks.append(chunk)
# for chunk in chunks:
# print(chunk)
# for i in range(len(chunk)):
#     print(f"chunk {i} -> {chunk[i]}")


#Embeddings
embeddings = model.encode(chunks)
# print("Embeddings created succussfully.")
# print(len(embeddings))
# print(embeddings[0])
# print(embeddings.shape)


#chromadb
client=chromadb.PersistentClient(path="./chroma_db")
collection=client.get_or_create_collection(name="My_documents")
#print("collection created successfully.")
ids=[]
for i in range(len(chunks)):
    ids.append(f"{file_name}_{i}")
collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist()
