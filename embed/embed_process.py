from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_question(question):
    embed_question_result = model.encode(question)
    return embed_question_result

def embed_chunked_sentences(chunked_data_list):
    embed_result = []
    for chunked_data in chunked_data_list:
        chunked_text = chunked_data["chunked_text"]
        embed_chunked_text = model.encode(chunked_text)
        data = {
            "source": chunked_data["source"],
            "chunked_text": chunked_text,
            "chunked_embed_text": embed_chunked_text
        }
        embed_result.append(data)
    return embed_result
