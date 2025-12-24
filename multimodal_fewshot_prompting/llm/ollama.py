from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5vl:3b", 
    emperature=0.0,
    num_predict=128,
)
