from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from utils import load_documents, load_db, save_db, load_embeddings

db = load_db(embedding_function=load_embeddings())
db.add_documents(load_documents("new_document/"))
save_db(db)