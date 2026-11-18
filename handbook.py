from search.search_process import search_data
from retrieval.retrive_document import load_all_documents
from chunk.chunk_process import chunk_document
from embed.embed_process import embed_chunked_sentences, embed_question
from prompts.prompt_process import build_prompt
from llm.llm_process import ask_llm
from chroma_data.chroma_process import create_chroma_db, search_by_embeded
if __name__ == "__main__":
    documents = load_all_documents("doc")
    final_chunked_documents = []
    for doc in documents:
        chunk_data = chunk_document(doc["source"], doc["text"], 40, 10)
        final_chunked_documents.extend(chunk_data)

    embeded_chunked_data = embed_chunked_sentences(final_chunked_documents)
    """question = input("What is your question? \n")
    while (question != "QUIT"):
        embed_question_data = embed_question(question)
        sorted_data = search_data(embed_question_data, embeded_chunked_data)
        prompt = build_prompt(sorted_data, question)
        answer = ask_llm(prompt)
        print(answer + "\n")
        question = input("What is your question? \n")"""
    collection = create_chroma_db(embeded_chunked_data)
    question = input("What is your question? \n")
    while (question != "QUIT"):
        embed_question_data = embed_question(question)
        results = search_by_embeded(collection, embed_question_data, 3)
        prompt = build_prompt(results, question)
        answer = ask_llm(prompt)
        print(answer + "\n")
        question = input("What is your question? \n")
