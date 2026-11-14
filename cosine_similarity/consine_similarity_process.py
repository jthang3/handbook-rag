import math
def dot_product_calc(first_vector, second_vector):
    dot_result = 0
    for i in range(0, len(first_vector)):
        dot_result += first_vector[i] * second_vector[i]
    return dot_result


def vector_length_calc(vector):
    vector_square = 0
    for vev in vector:
        vector_square += vev ** 2
    vector_length = math.sqrt(vector_square)
    return vector_length

def consine_similarity_result(question, source):
    dot_product = dot_product_calc(question, source)
    question_vector_len = vector_length_calc(question)
    source_vector_len = vector_length_calc(source)
    total_vector_len = question_vector_len * source_vector_len
    similarity = dot_product / total_vector_len
    return similarity