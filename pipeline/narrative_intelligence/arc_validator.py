# pipeline/narrative_intelligence/arc_validator.py
from .motivational_map import resolve_motivation
from .causal_chains import check_causality

def validate_narrative_arc(trait, novel_text):
    """
    STRICT MODE: Only pardons a contradiction if there is 
    STRONG evidence of a trigger or a high-stakes motivation.
    """
    # 1. Check for a direct cause (e.g., 'Because of the fire...')
    has_cause = check_causality(novel_text)
    
    # 2. Check for high-stakes motivation (e.g., 'To save his friend...')
    has_motivation = resolve_motivation(trait, novel_text)
    
    # 3. STRICT CHECK: We only pardon if the text is long enough to be a real scene.
    # Short sentences usually don't have enough 'weight' to be a valid Arc.
    is_substantial = len(novel_text.split()) > 20

    # LOGIC: It's only an Arc if (Cause OR Motivation) AND it's a detailed scene.
    if (has_cause or has_motivation) and is_substantial:
        return {
            "is_valid_arc": True, 
            "reason": "CONSISTENT: Arc validated via high-stakes situational override."
        }
    
    # Otherwise, stick to the original 'Inconsistent' finding
    return {
        "is_valid_arc": False, 
        "reason": "INCONSISTENT: Change in behavior lacks sufficient narrative justification."
    }