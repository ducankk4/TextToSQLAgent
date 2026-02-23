from src.embedding.base import BaseEmbeddingAPI
from typing import List
from google import genai

class GoogleEmbedding(BaseEmbeddingAPI):

    def __init__(self, api_key, model_name):
        super().__init__(api_key, model_name)
        self.client = genai.Client(api_key= self.api_key)

    def embed_query(self, query):
        reponse = self.client.models.embed_content(
            model=self.model_name,
            contents=query
        )
        
        return reponse.embeddings[0].values
    
    def embed_documents(self, texts):
        embeddings = []
        for text in texts:
            embed = self.embed_query(text)
            embeddings.append(embed)

        return embeddings
        
    