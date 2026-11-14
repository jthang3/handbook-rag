from search.search_process import search_data
from retrieval.retrive_document import load_all_documents
from chunk.chunk_process import chunk_document
from embed.embed_process import embed_chunked_sentences, embed_question
if __name__ == "__main__":
    documents = load_all_documents("doc")
    final_chunked_documents = []
    for doc in documents:
        chunk_data = chunk_document(doc["source"], doc["text"], 40, 10)
        final_chunked_documents.extend(chunk_data)

    embeded_chunked_data = embed_chunked_sentences(final_chunked_documents)
    embed_question_data = embed_question("How much can I reimbursed fo rmeal during business travel?")
    sorted_data = search_data(embed_question_data, embeded_chunked_data)
    print(sorted_data)