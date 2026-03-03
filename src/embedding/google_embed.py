from langchain_core.embeddings import Embeddings
from typing import List
from google import genai

class GoogleEmbedding(Embeddings):

    def __init__(self, api_key, model_name):
        self.api_key = api_key
        self.model_name = model_name
        self.client = genai.Client(api_key= api_key)

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
        
    