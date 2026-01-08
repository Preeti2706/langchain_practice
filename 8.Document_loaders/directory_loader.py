from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='8.Document_loaders/books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()  # lazy_load loads on demand, not all documents are loaded at once, they're fetched one at a time as needed

for document in docs:
    print(document.metadata)