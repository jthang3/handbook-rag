import chromadb

def create_chroma_db(chunk_data):
    client = chromadb.PersistentClient(path="chroma_data")
    collection = client.get_or_create_collection(
        name="handbook",
        metadata={"hnsw:space": "cosine"})
    add_chunks_to_collection(collection, chunk_data)
    return collection
def get_collection():
    client = chromadb.PersistentClient(path="chroma_data")
    collection = client.get_collection(name="handbook")
    return collection
def add_chunks_to_collection(collection, chunks):
    ids = []
    documents = []
    embeddings = []
    metadatas = []
    for i, data in enumerate(chunks):
        id = f"{data["source"]}-{i}"
        document = data["chunked_text"]
        embedding = data["chunked_embed_text"].tolist()
        metadata = {"source": data["source"]}
        ids.append(id)
        documents.append(document)
        embeddings.append(embedding)
        metadatas.append(metadata)
    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

def search_by_embeded(collection, embed_question, top_n):
    results = collection.query(
        query_embeddings=embed_question.tolist(),
        n_results=top_n
    )
    return clean_up_chroma_results(results)

def clean_up_chroma_results(result):
    top_three_cleaned_results = []
    for i in range(len(result["ids"][0])):
        data = {
            "source": result["metadatas"][0][i],
            "chunked_text": result["documents"][0][i],
            "score": result["distances"][0][i]
        }
        top_three_cleaned_results.append(data)
    return top_three_cleaned_results