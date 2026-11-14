from cosine_similarity.consine_similarity_process import consine_similarity_result

#get question vector
#get list of source vectors
#loop through each source vector
#get score using cosine similarity
#put them in an array
#sort an array by score. Larg to small
#get the top three


def search_data(question_vector, source_vector_list):
    all_data_with_score = []
    for info in source_vector_list:
        score = consine_similarity_result(question_vector, info["chunked_embed_text"])
        data = {
            "source": info["source"],
            "chunked_text": info["chunked_text"],
            "chunked_embed_text": info["chunked_embed_text"],
            "score": score
        }
        all_data_with_score.append(data)
    all_data_with_score.sort(key=lambda x: x["score"], reverse=True)
    top_three = all_data_with_score[:3]
    return top_three