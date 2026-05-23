# pipeline/narrative_intelligence/causal_chains.py

def check_causality(novel_text):
    """
    Checks if an 'out-of-character' moment was caused by an event.
    Example: He was scared (Backstory), but then he 'saw the fire' (Event), 
    so he 'jumped' (Action).
    """
    # Looking for 'Causal Connectives'
    causal_markers = ["because", "since", "due to", "witnessed", "after seeing"]
    
    for marker in causal_markers:
        if marker in novel_text.lower():
            return True # There is a narrative cause for the change
    return False