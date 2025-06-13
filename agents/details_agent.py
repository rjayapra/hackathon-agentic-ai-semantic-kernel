from semantic_kernel import Kernel
from semantic_kernel.functions import kernel_function
from typing import Annotated

class DetailsAgent:
    def __init__(self, memory):
        self.memory = memory
        self.name = "DetailsAgent"
    
    @kernel_function(description="Search 'details' in the memory based on the query")
    def details_agent(self, query) -> Annotated[str, "Get information from the Details table"]:
        """
        Search the memory for entries with 'details' based on query.
        """
        print(f"[DetailsAgent] Searching for details with query: {query}")
        results = self.memory.search(query)
        if not results:
            return "[DetailsAgent] No matching files found."
        response_lines = []
        for entry in results[:5]:
            details = entry.get('details')
            if details:
                filename = entry.get('file_name', 'N/A')
                response_lines.append(
                    f"File: {filename}\n"
                    f"  Details: {details}"
                )
        if not response_lines:
            return "[DetailsAgent] No matching details found."
        print(f"[DetailsAgent] Found {len(response_lines)} results.")
        return response_lines
