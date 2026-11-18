def build_context(top_three_results):
    context = ""
    for result in top_three_results:
        print(result["source"])
        print("-------------")
        context += f"[Source: {result["source"]}]\n"
        context += f"data from result: {result["chunked_text"]}\n\n"
    return context

def build_prompt(top_three_results, question):
    context = build_context(top_three_results)
    prompt = f"""
        you are the helper of handbook assistance for a company

        Rules:
        - Only answer based on the context. Do not guess
        - If the answer in not in the context, say exactly: "I couldn't find that in the context"
        - Do not guess nor use knowledge outside of the provided context
        - When applying for math, look for the limitation such as maximum or minimum
        - when applying for days, unit, etc, make sure the current amount is apply. 
        - Short answer only. 1-3 lines per answer
        - End the answer with this format. The source file: x. Replace x with the actual source file from the context
        - If the context has an exception (like ‘X is not covered’), say what is covered and what is not covered
        - Use the source only from the context. Do not guess the source

        context: {context}

        question:{question}
    """
    return prompt