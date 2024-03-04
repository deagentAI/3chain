from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from glob import glob
from tqdm import tqdm
import yaml

def load_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

config = load_config()

def load_embeddings(model_name=config["embeddings"]["name"],
                    model_kwargs = {'device': config["embeddings"]["device"]}):
    return HuggingFaceEmbeddings(model_name=model_name, model_kwargs = model_kwargs)

def load_documents(directory : str):
    """Loads all documents from a directory and returns a list of Document objects
    args: directory format = directory/
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = config["TextSplitter"]["chunk_size"], 
                                                   chunk_overlap = config["TextSplitter"]["chunk_overlap"])
    documents = []
    for item_path in tqdm(glob(directory + "*.pdf")):
        loader = PyPDFLoader(item_path)
        documents.extend(loader.load_and_split(text_splitter=text_splitter))

    return documents

def load_db(embedding_function, save_path=config["faiss_indexstore"]["save_path"], index_name=config["faiss_indexstore"]["index_name"]):
    db = FAISS.load_local(folder_path=save_path, index_name=index_name, embeddings = embedding_function)
    return db

def save_db(db, save_path=config["faiss_indexstore"]["save_path"], index_name=config["faiss_indexstore"]["index_name"]):
    db.save_local(save_path, index_name)
    print("Saved db to " + save_path + index_name)