
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
#upload raw pdf file
pdfs_directory="pdfs/"
def upload_pdf(file):
    with open(pdfs_directory+file.name,"wb") as f:
        f.write(file.getbuffer())
        
def load_pdff(file_path):
    loader=PDFPlumberLoader(file_path)
    return loader.load()

file_path='universal_declaration_of_human_rights.pdf'
documents=load_pdff(file_path)
# print(f"number of pages in the pdf: {len(documents)}")

#step 2: create Chunks

def create_chunks(documents):
    text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True
    )
    text_chunks=text_splitter.split_documents(documents)
    return text_chunks

text_chunks=create_chunks(documents)
# print("chunks count",len(text_chunks))


#step 3: setup embeddings model(use deepseek r1 with ollama)

ollama_model_name="deepseek-r1:1.5b"
def get_embedding_model(ollama_model_name):
    embedding=OllamaEmbeddings(model=ollama_model_name)
    return embedding
    
#step 4 index documents ** store embeddings in FAISS (vector store)
FAISS_DB_PATH="vectorstore/db_faiss"
faiss_db=FAISS.from_documents(text_chunks,get_embedding_model(ollama_model_name))
faiss_db.save_local(FAISS_DB_PATH)