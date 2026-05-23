# pipeline/physical.py

def check_physical_consistency(backstory_text, novel_text):
    """
    Checks for biological/physical contradictions.
    """
    # Pairs of (Backstory Limitation, Novel Contradiction)
    physical_clashes = [
        ("blind", "saw"), ("blind", "noticed the color"),
        ("deaf", "heard"), ("deaf", "listened"),
        ("mute", "spoke"), ("mute", "shouted"),
        ("paralyzed", "ran"), ("paralyzed", "walked"),
        ("allergic", "ate"), ("allergic", "consumed"),
        ("injured", "fought")
    ]
    
    back_low = backstory_text.lower()
    nov_low = novel_text.lower()
    
    for limit, action in physical_clashes:
        if limit in back_low and action in nov_low:
            return {
                "is_consistent": False,
                "reason": f"Physical Inconsistency: Backstory mentions character is '{limit}', but novel says they '{action}'."
            }
            
    return {"is_consistent": True, "reason": None}