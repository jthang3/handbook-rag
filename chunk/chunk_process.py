def clean_chunk_paragraph(original_chunk_paragraph):
    clean_paragraph = []
    for text in original_chunk_paragraph:
        clean_text = text.strip()
        clean_paragraph.append(clean_text)
    return clean_paragraph

def paragaph_chunk_process(file_text, file_name):
    text_paragraphs = file_text.split("\n\n")
    data = []
    clean_paragraphs = clean_chunk_paragraph(text_paragraphs)
    for text in clean_paragraphs:
        chunked_data = {
            "source": file_name,
            "chunked_text": text
        }
        data.append(chunked_data)
    return data

def chunk_by_size(file_name, file_text, chunk_size, overlap):
    final_chunked_data = []
    text_data = file_text.split()
    step = chunk_size - overlap
    for start in range(0, len(text_data), step):
        chunked_text = text_data[start:start + chunk_size]
        chunked_text = " ".join(chunked_text)
        data = {
            "source": file_name,
            "text": chunked_text
        }
        final_chunked_data.append(data)
    return final_chunked_data

def chunk_document(file_name, file_text, chunk_size, overlap, paragraph_chunk = True):
    final_chunk = []
    if (paragraph_chunk):
        final_chunk = paragaph_chunk_process(file_text, file_name)
    else:
        final_chunk = chunk_by_size(file_name, file_text, chunk_size, overlap)
    return final_chunk
