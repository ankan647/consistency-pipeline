from typing import List

def contradicts_fear(fear: str, chunks: List[str]) -> bool:
    """
    Check if any chunk contradicts the given fear belief.
    
    Args:
        fear: Fear belief string
        chunks: List of text chunks from the novel
        
    Returns:
        bool: True if contradiction is found
    """
    # Make fear belief lowercase for case-insensitive comparison
    fear_lower = fear.lower()
    
    # Extract key terms from fear (simple approach)
    fear_keywords = []
    for word in fear_lower.split():
        # Remove common stop words
        stop_words = {'a', 'an', 'the', 'and', 'or', 'but', 'is', 'was', 'were', 'to', 'of', 'in', 'that', 'for'}
        if word not in stop_words and len(word) > 2:
            fear_keywords.append(word)
    
    for i, chunk in enumerate(chunks):
        chunk_lower = chunk.lower()
        
        # Check for explicit contradictions
        contradiction_phrases = [
            'not afraid of', 'no fear of', 'unafraid of', 'brave about',
            'overcame fear of', 'conquered fear of', 'faced their fear of',
            'does not fear', 'never feared', 'without fear of'
        ]
        
        for phrase in contradiction_phrases:
            if phrase in chunk_lower:
                # Check if this phrase is related to the fear
                for keyword in fear_keywords:
                    if keyword in chunk_lower:
                        return True
        
        # More sophisticated check - look for positive statements about the feared thing
        positive_indicators = [
            f'comfortable with', f'enjoys', f'loves', f'admires',
            f'not scared of', f'fearless about', f'confident with'
        ]
        
        for indicator in positive_indicators:
            if indicator in chunk_lower:
                for keyword in fear_keywords:
                    if keyword in chunk_lower:
                        return True
    
    return False