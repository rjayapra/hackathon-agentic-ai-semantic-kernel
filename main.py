from memory.memory_loader import load_memory_from_json
from coordinator.coordinator_agent import route_query

if __name__ == "__main__":
    memory = load_memory_from_json("data/sampledata.json")
    query = "What procedure does this file explain about?"
    response = route_query(query, memory)
    print(response)
