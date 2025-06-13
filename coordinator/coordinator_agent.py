from agents.file_agent import handle_query
from agents.details_agent import handle_details_query

def route_query(query, memory):
    # Route queries about 'details' to the details agent
    if 'detail' in query.lower():
        return handle_details_query(query, memory)
    # Fallback to file agent for other queries
    return handle_query(query, memory)
