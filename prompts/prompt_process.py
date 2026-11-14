def build_context(top_three_results):
    context = ""
    for result in top_three_results:
        context += f"[Source: {result["source"]}]\n"
        context += f"data from result: {result["chunked_text"]}\n\n"
    return context

def build_prompt(top_three_results, question):
    context = build_context(top_three_results)
    prompt = f"""
        You're an HR representation. Anser the question ONLY from the provided context.

        Rules:
        - If the answer is not in the context say "I don't know"
        - if you have to apply math, show the step throughly and apply maximum and minimum limitation
        - Also provide the source where the answer comes from
        - include related details from the same section if they help the user
        - if the question mean more than one thing, please read clear on the specific item. Do not apply if the information is not provided in the context
        - When there is a limit per unit (per night, per day, per item), apply the limit to each unit first, then multiply.

        context: {context}

        question:{question}
    """
    return prompt