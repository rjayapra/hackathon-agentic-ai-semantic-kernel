from agents.file_agent import handle_query

def route_query(query, memory):
    # For demonstration, route everything to the file agent
    return handle_query(query, memory)
