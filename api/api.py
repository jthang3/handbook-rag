import re

from fastapi import FastAPI
from pydantic import BaseModel
from embed.embed_process import embed_chunked_sentences, embed_question
from prompts.prompt_process import build_prompt
from llm.llm_process import ask_llm
from search.search_process import search_data
from chroma_data.chroma_process import get_collection, search_by_embeded

app = FastAPI()

@app.get("/hello")
def hello():
    return {"Message": "Hello from my RAG API"}

class Ask_question(BaseModel):
    ask_question: str
    temperature: float = 0.01

class Ask_response(BaseModel):
    answer: str
    sources: list[str]

def getSource(answer):
    print(answer)
    print("---------------")
    #source_path = answer.split("source:")
    source_path = re.split(r"source:", answer, maxsplit=1, flags=re.IGNORECASE)
    print(source_path)
    source = source_path[len(source_path) - 1].strip()
    return source

def get_answer_only(answer):
    #source_path = answer.split("source:")
    source_path = re.split(r"source:", answer, maxsplit=1, flags=re.IGNORECASE)
    answer = source_path[0]
    return answer.strip()

@app.post("/ask")
def ask(request: Ask_question) -> Ask_response:
    question = request.ask_question
    embed_ques = embed_question(question)
    collection = get_collection()
    results = search_by_embeded(collection, embed_ques, 3)
    prompt = build_prompt(results, question)
    answer = ask_llm(prompt)
    source = getSource(answer)
    final_answer = get_answer_only(answer)
    return Ask_response(answer=final_answer, sources=[source])
