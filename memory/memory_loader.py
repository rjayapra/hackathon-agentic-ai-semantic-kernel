import json

def load_memory_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def search_memory(memory, query):
    query = query.lower()
    results = []

    def search_in_item(item):
        if isinstance(item, dict):
            return any(query in str(value).lower() for value in item.values())
        elif isinstance(item, list):
            return any(query in str(element).lower() for element in item)
        else:
            return query in str(item).lower()

    if isinstance(memory, list):
        for entry in memory:
            if search_in_item(entry):
                results.append(entry)
    elif isinstance(memory, dict):
        for key, value in memory.items():
            if search_in_item(value) or query in key.lower():
                results.append({key: value})

    return results

def ai_search_memory(memory, ai_search_fn, query):
    """
    Search memory using an AI-based search function.

    Args:
        memory: The memory data (list or dict).
        ai_search_fn: A function that takes (item, query) and returns a relevance score or boolean.
        query: The search query.

    Returns:
        List of items from memory that match the query according to ai_search_fn.
    """
    results = []

    if isinstance(memory, list):
        for entry in memory:
            score = ai_search_fn(entry, query)
            if score:
                results.append({"item": entry, "score": score})
    elif isinstance(memory, dict):
        for key, value in memory.items():
            score = ai_search_fn({key: value}, query)
            if score:
                results.append({"item": {key: value}, "score": score})

    # Sort results by score if score is numeric, otherwise return as is
    if results and isinstance(results[0]["score"], (int, float)):
        results.sort(key=lambda x: x["score"], reverse=True)

    return results

def ai_search_fn(item, query):
    """
    A simple AI-based search function that checks if the query is in the item.
    This is a placeholder for more complex AI logic.
    """
    return query in str(item).lower()
    