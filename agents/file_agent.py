from semantic_kernel import Kernel
from semantic_kernel.functions import kernel_function

from typing import Annotated

class FileAgent:
    def __init__(self, memory):
        self.memory = memory
        self.name = "FileAgent"
        
    @kernel_function(description="Search files in the memory based on the query")
    def file_agent(self, query) -> Annotated[str, "Get information about the QSP file"]:
        """        
        Search files in the memory based on the query.
        Args:
            query (str): The search query.
        Returns:
            str: A formatted string with the search results.
        """
        print(f"[FileAgent] Searching for query: {query}")
        results = self.memory.search(query)
        if not results:
            return "[FileAgent] No matching files found."
        response_lines = []
        for entry in results[:5]:  # Limit to first 5 results
            filename = entry.get('file_name', 'N/A')
            roletitle = entry.get('role_title', 'N/A')
            mite_ids = entry.get('mite_ids', [])
            rdims = entry.get('rdims', [])
            nqual = entry.get('nqual', [])
            pos_count = len(entry.get('Pos', []))
            
            ref_count = len(entry.get('References', []))
            response_lines.append(
                f"File: {filename}\n"
                f"  Role Title: {roletitle}\n"
                f"  MITE IDs: {mite_ids}\n"
                f"  RDIMs: {rdims}\n"
                f"  Positions: {pos_count}\n"
                f"  References: {ref_count}"
            )
        print(f"[FileAgent] Found {len(results)} results.")
        return response_lines
            

