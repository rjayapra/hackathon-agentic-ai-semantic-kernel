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
