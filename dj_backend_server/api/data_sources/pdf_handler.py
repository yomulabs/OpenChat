# views.py
import json
from django.views.decorators.csrf import csrf_exempt
from langchain.text_splitter import RecursiveCharacterTextSplitter
from api.utils import get_embeddings
from langchain.document_loaders.directory import DirectoryLoader
from api.utils import init_vector_store
from langchain.document_loaders import PyPDFium2Loader
import os
from web.utils.delete_foler import delete_folder
from api.interfaces import StoreOptions
@csrf_exempt
def pdf_handler(shared_folder: str, namespace: str):
    try:
        print("PDF_HANDLER STARTING...")
        print(shared_folder)
        print(namespace)
        directory_path = os.path.join("website_data_sources", shared_folder)

        print("directory loader")
        directory_loader = DirectoryLoader(path=directory_path, glob="**/*.pdf", loader_cls=PyPDFium2Loader, use_multithreading=False)

        raw_docs = directory_loader.load_and_split()

        print("text splitter")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200,length_function=len)
        docs = text_splitter.split_documents(raw_docs)

        print("get embeddings..")
        embeddings = get_embeddings()
        print("Init vector store..")

        init_vector_store(docs, embeddings, StoreOptions(namespace))
        
        print("Delete folder..")
        delete_folder(folder_path=directory_path)
        print('All is done, folder deleted')

    except Exception as e:
        import traceback
        print(e)
        traceback.print_exc()
