from src.agent.state import MaskState, SchemaParsingState, FullyState
from src.vector_store.qdrant import QdrantService
from src.logger import logger
from src.config import EXAMPLE_QA_COLLECTION, TABLE_DESC_COLLECTION, top_k, GOOGLE_API_KEY, GEMINI_MODEL
from src.agent.prompt import MASK_PROMPT, CLARIFY_PROMPT, PLANNING_PROMPT, TEXT_TO_SQL_PROMPT, CRITIC_PROMPT
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

class SchemaParsingNode:
    def __init__(self):
        self.qdrant_service = QdrantService()


    def retrieve_node(self, state: SchemaParsingState) -> SchemaParsingState:
        query = state['query']
        retrieved_tables = self.qdrant_service.similarity_search(
            collection_name= TABLE_DESC_COLLECTION,
            query= query,
            k = top_k
        )
        logger.info(f"Retrieved tables: {retrieved_tables}")
        return {
            'retrived_tables': retrieved_tables
        }
    
    def reranking_node(self, state: SchemaParsingState) -> SchemaParsingState:
        pass

class MaskingNode:
    def __init__(self):
        self.vector_store = QdrantService()
    
    def masking_node(self, state: MaskState) -> MaskState:
        llm = ChatGoogleGenerativeAI(
            model= GEMINI_MODEL,
            api_key= GOOGLE_API_KEY
        )
        chain = ChatPromptTemplate.from_template(MASK_PROMPT) | llm
        response = chain.invoke({

        })
        return {
            'masked_query': response.content
        }
    
    def retrieve_node(self, state: MaskState) -> MaskState:
        query = state['query']
        results = self.vector_store.similarity_search(
            collection_name= EXAMPLE_QA_COLLECTION,
            query= query,
            k = top_k
        )

        return {
            'relevant_query': results
        }
    
class PlanningNode:
    def join_planning_node(self, state: FullyState) -> FullyState:
        pass

    def plainning_node(self, gitstate: FullyState) -> FullyState:
        pass

def clarify_node(state: SchemaParsingState) -> FullyState:
    query = state['query']
    retrieved_tables = state['retrived_tables']
    llm = ChatGoogleGenerativeAI(
        model= GEMINI_MODEL,
        api_key= GOOGLE_API_KEY
    )
    chain = ChatPromptTemplate.from_template(CLARIFY_PROMPT) | llm
    response = chain.invoke({
        'query' : query,
    })

    return {

    }



def text_to_sql_node(state: FullyState) -> FullyState:
    pass

def critic_node(state: FullyState) -> FullyState:
    pass


    