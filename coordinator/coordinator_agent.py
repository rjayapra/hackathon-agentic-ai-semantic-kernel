from agents.file_agent import FileAgent

def route_query(query, memory):
    query_lower = query.lower()
    if "file" in query_lower:
        return FileAgent(query, memory)
   
    return "Query type not recognized."