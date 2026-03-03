from langchain_core.documents import Document
from typing import List, Dict

def text_to_docs(texts: Dict[str, str]) -> List[Document]:
    """
    Convert a dict of tables name and their descriptions to a list of Document obj.
    """
    docs = []

    for key, val in texts.items():
        doc = Document(
            page_content= val,
            metadata = {"table_name": key}
        )
        docs.append(doc)
    return docs