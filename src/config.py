from dotenv import load_dotenv
import os

# load enviroment variables 
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# model name
EMBEDDING_MODEL = "gemini-embedding-001"
 # generative model 
GEMINI_MODEL = "gemini-2.0-flash"

TABLE_DESC_COLLECTION = "table_descriptions"
EXAMPLE_QA_COLLECTION = "example_qa"

top_k = 5