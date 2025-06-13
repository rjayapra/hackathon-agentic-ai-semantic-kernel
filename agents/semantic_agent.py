import json

def handle_semantic_query(query, memory, kernel):
    """
    Orchestrates an agentic AI step using Semantic Kernel to answer queries
    based on the in-memory JSON data.
    """
    # Prepare a limited memory context for the LLM
    context_entries = memory[:20]  # limit to first 20 entries for prompt brevity
    memory_text = json.dumps(context_entries)

    prompt = (
        "You are an AI assistant knowledgeable about the memory data provided. "
        "Use ONLY the JSON context to answer the question.\n"  
        f"Memory JSON: {memory_text}\n"
        f"Question: {query}\n"
        "Answer based solely on the memory context."
    )

    # Invoke the chat service
    result = kernel.run_async(
        "azure_chat",
        prompt
    ).result

    return f"[SemanticAgent] {result}"
