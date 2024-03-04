from langchain.vectorstores import FAISS
from utils import load_documents, save_db, load_embeddings

embedding_function = load_embeddings()
documents = load_documents("data/")

db = FAISS.from_documents(documents, embedding_function)
print("Index Created")
save_db(db)

print(db.similarity_search("ISO/IEC 27001 standard"))