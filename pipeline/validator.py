# pipeline/validator.py

def validate_identity(backstory_identities, novel_text):
    """
    Checks if the character's 'Identity Facts' (e.g., Arthur is a Knight)
    are contradicted by the novel's descriptions.
    """
    # Define 'Identity Clashes' (Opposites that shouldn't happen)
    CLASH_MAP = {
        "knight": ["coward", "peasant", "traitor", "farmer"],
        "priest": ["assassin", "atheist", "criminal"],
        "rich": ["poor", "beggar", "penniless"],
        "revenge": ["forgiveness", "mercy", "pity"]
    }

    novel_low = novel_text.lower()
    
    for subject, identity in backstory_identities:
        # If we find a known identity in the backstory (e.g., 'knight')
        if identity in CLASH_MAP:
            # Check if the novel contains any of the 'clash' words
            for clash_word in CLASH_MAP[identity]:
                if clash_word in novel_low:
                    return {
                        "is_valid": False,
                        "reason": f"Factual Contradiction: Backstory defines {subject} as '{identity}', but novel describes them as '{clash_word}'."
                    }
    
    return {"is_valid": True, "reason": "Identity remains consistent."}