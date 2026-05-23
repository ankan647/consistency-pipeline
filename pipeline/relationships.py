# pipeline/relationships.py

def analyze_relationship_context(text, keywords):
    """
    Realistic Feature: Extracts only the sentences where key social 
    interactions are happening, rather than looking at the whole book.
    """
    sentences = text.split('.')
    relevant_context = []
    
    for sent in sentences:
        if any(word in sent.lower() for word in keywords):
            relevant_context.append(sent.strip())
            
    return " ".join(relevant_context)

def check_social_consistency(backstory_text, novel_text):
    """
    Checks if the social dynamic between characters shifts 
    unrealistically based on contextual analysis.
    """
    # 1. Define the relationship pairs to watch for
    # Format: (Backstory Keyword, Novel Keyword, Rationale)
    inconsistent_shifts = [
        ("friend", "enemy", "Social Inconsistency: 'Friend' in backstory, but acts as 'Enemy' in novel."),
        ("loves", "hates", "Social Inconsistency: Character's love interest shifted to hatred."),
        ("loyal", "betray", "Social Inconsistency: Established loyalty was replaced by betrayal."),
        ("stranger", "brother", "Social Inconsistency: A stranger is treated as a brother.")
    ]

    # 2. Use the analysis function to find the 'Novel Context'
    all_keywords = [pair[1] for pair in inconsistent_shifts]
    novel_context = analyze_relationship_context(novel_text.lower(), all_keywords)
    backstory_low = backstory_text.lower()

    # 3. Perform the consistency check on that context
    for back_word, nov_word, reason in inconsistent_shifts:
        if back_word in backstory_low and nov_word in novel_context:
            return {
                "is_consistent": False, 
                "reason": reason
            }
    
    return {"is_consistent": True, "reason": "Social relationships are stable."}