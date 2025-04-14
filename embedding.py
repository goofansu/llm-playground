import llm

embedding_model = llm.get_embedding_model("mpnet")

vector = embedding_model.embed("hello world")

print(vector)
