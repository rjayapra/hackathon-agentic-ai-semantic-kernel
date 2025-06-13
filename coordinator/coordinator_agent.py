from agents.file_agent import FileAgent
from agents.details_agent import DetailsAgent

def route_query(query, memory):
    query_lower = query.lower()
    # Route queries about 'details' to DetailsAgent
    if "detail" in query_lower:
        return DetailsAgent(memory).details_agent(query)
    # Route file queries to FileAgent
    if "file" in query_lower:
        return FileAgent(memory).file_agent(query)

    return "Query type not recognized."
