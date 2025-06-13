
def handle_details_query(query, memory):
    """
    Search the memory entries for 'details' field matching the query.
    If no specific matches, list all entries containing details.
    """
    matches = []
    q = query.lower()
    for entry in memory:
        details = entry.get('details')
        if details:
            if q in str(details).lower():
                matches.append({'file_name': entry.get('file_name'), 'details': details})
    if not matches:
        # No specific matches; return all entries with details
        all_details = [
            {'file_name': e.get('file_name'), 'details': e.get('details')}
            for e in memory if e.get('details')
        ]
        if all_details:
            response = "[DetailsAgent] No matches for query; listing all details entries:\n"
            for d in all_details[:5]:
                response += f"{d['file_name']}: {d['details']}\n"
            return response
        else:
            return "[DetailsAgent] No details entries found in memory."
    response = f"[DetailsAgent] Found {len(matches)} matching details entries:\n"
    for m in matches[:5]:
        response += f"{m['file_name']}: {m['details']}\n"
    return response
