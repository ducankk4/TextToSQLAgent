from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from src.embedding.google_embed import GoogleEmbedding
from src.config import GOOGLE_API_KEY, EMBEDDING_MODEL
from langchain_core.documents import Document
from src.logger import logger

class QdrantService:
    
    def __init__(self):
        self.url = "http://localhost:6333"
        self.client = QdrantClient(
            url = self.url
        )
        self.embedding = GoogleEmbedding(
            api_key= GOOGLE_API_KEY,
            model_name= EMBEDDING_MODEL
        )
    
    def indexing(self, collection_name: str, docs: Document):
        if self.client.collection_exists(collection_name):
            logger.info(f"Collection '{collection_name}' already exists. Skipping indexing.")
            return self.client.get_collection(collection_name)
        
        else:
            vector_store = QdrantVectorStore.from_documents(
                documents= docs,
                embedding= self.embedding,
                collection_name= collection_name,
                client = self.client
            )
            logger.info(f"Collection '{collection_name}' created and indexed successfully.")
            return vector_store
        
    def load_collection(self, collection_name: str):
        if self.client.collection_exists(collection_name):
            logger.info(f"Collection '{collection_name}' loaded successfully.")
            return QdrantVectorStore(
                collection_name= collection_name,
                embedding= self.embedding,
                client = self.client
            )
        else:
            logger.warning(f"Collection '{collection_name}' does not exist.")
            return None
    
    def similarity_search(self, collection_name: str, query: str, k: int = 5):
        vector_store = self.load_collection(collection_name)

        results = vector_store.similarity_search(query= query, k= k)
        return results
    
