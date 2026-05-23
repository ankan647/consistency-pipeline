# pipeline/stylometry.py

def analyze_style(text):
    sentences = text.split('.')
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
    
    avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)
    
    # Check for 'Sophistication' (Words longer than 8 characters)
    words = text.split()
    complex_words = [w for w in words if len(w) > 8]
    complexity_score = len(complex_words) / len(words)
    
    return {
        "avg_len": avg_sentence_length,
        "complexity": complexity_score
    }

def check_style_consistency(backstory_text, novel_text):
    b_style = analyze_style(backstory_text)
    n_style = analyze_style(novel_text)
    
    # If the backstory is very complex but the novel is very simple (or vice versa)
    # We flag a 'Voice Inconsistency'
    len_diff = abs(b_style["avg_len"] - n_style["avg_len"])
    comp_diff = abs(b_style["complexity"] - n_style["complexity"])
    
    if len_diff > 15 or comp_diff > 0.15:
        return {
            "is_consistent": False,
            "reason": f"Style Clash: Character voice changed significantly (Complexity Diff: {comp_diff:.2f})."
        }
    
    return {"is_consistent": True, "reason": None}