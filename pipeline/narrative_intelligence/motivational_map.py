# pipeline/narrative_intelligence/motivational_map.py

def resolve_motivation(trait, action_context):
    """
    Checks if a high-level motivation (Saving a life) 
    overrides a low-level trait (Fear of heights).
    """
    # Define a hierarchy: Life Preservation > Personal Fear
    overrides = {
        "fear": ["save", "protect", "rescue", "help", "sacrifice"],
        "hate": ["forgive", "pity", "mercy", "understand"],
        "lazy": ["duty", "urgent", "must", "forced"]
    }
    
    for core_trait, valid_overrides in overrides.items():
        if core_trait in trait.lower():
            if any(word in action_context.lower() for word in valid_overrides):
                return True # Conflict resolved by motivation
    return False