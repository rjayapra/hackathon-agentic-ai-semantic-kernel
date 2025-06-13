from memory.memory_loader import search_memory

def handle_query(query, memory):
    results = search_memory(memory, query)
    if results:
        return f"[CustomerAgent] Found {len(results)} matching entries:\n" + "\n".join(str(r) for r in results[:5])
    else:
        return "[CustomerAgent] No matching entries found."
