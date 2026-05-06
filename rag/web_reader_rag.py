import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_APIKEY")

llm = ChatGroq(model="groq/compound-mini")

loader = WebBaseLoader("https://www.bbc.com/news/articles/c5yrq1090p8o")
document_loader = loader.load()


text_splitters = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

docs = text_splitters.split_documents(document_loader)


embeddings = HuggingFaceBgeEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(docs, embeddings)

query = "How is India's IT industry"

result = vectorstore.similarity_search(query)

print(result[0].page_content)
