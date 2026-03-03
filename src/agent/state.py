from typing import TypedDict, List, Dict
from pydantic import BaseModel, Field
from langchain_core.documents import Document

class MaskState(TypedDict):
    query: str
    masked_query: str
    relevant_query: List[Document]
    
class SchemaParsingState(TypedDict):
    query: str
    retrived_tables: List[str]
    reranked_tables: List[str]
    
class FullyState(TypedDict):
    query: str
    join_plan: str
    example: List[str]
    execute_plan: str
    reranked_tables: List[str]
    table_columns: Dict[str, List[str]]

class ClarifyStructure(BaseModel):
    reasonse : str = Field(
        description= "Lý do đưa ra kết luận"
    )
    need_additional_info: bool = Field(
        description= "Có cần yêu cầu bổ sung thông tin từ người dùng để làm rõ câu hỏi query hay không"
    )

class MaskingStructure(BaseModel):
    masked_query: str = Field(
        description= "Câu hỏi đã được tổng quát hóa"
    )
    reasonse: str = Field(
        description= "Lý do đưa ra kết luận"
    )

class PlanningStructure(BaseModel):
    plan: str = Field(
        description= "Kế hoạch thực hiện"
    )
    reasonse: str = Field(
        description= "Lý do đưa ra kế hoạch"
    )
