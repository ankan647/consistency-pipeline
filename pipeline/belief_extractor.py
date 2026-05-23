import spacy
from pipeline.belief_state import BeliefState

# This was the missing line!
nlp = spacy.load("en_core_web_sm")

def extract_beliefs(backstory_text: str):
    doc = nlp(backstory_text.lower())
    beliefs = []
    
    # Feeling verbs and Identity indicators
    feeling_verbs = ["hate", "love", "fear", "avoid", "want", "phobia", "enjoys"]
    identity_verbs = ["is", "was", "became"]

    for sent in doc.sents:
        sent_text = sent.text
        if any(v in sent_text for v in feeling_verbs + identity_verbs):
            # Extract nouns as subjects of the belief
            objs = [t.text for t in sent if t.pos_ in ["NOUN", "PROPN"] and len(t.text) > 3]
            
            for obj in objs:
                # Check for negative context (fear, hate, or being poor/penniless)
                is_neg = any(n in sent_text for n in ["hate", "fear", "avoid", "phobia", "poor", "penniless"])
                polarity = -1 if is_neg else 1
                
                beliefs.append(BeliefState(
                    pathway="SEMANTIC",
                    subject=obj,
                    original_text=sent_text,
                    polarity=polarity
                ))
                print(f"   🎯 [DEBUG] Extracted Trait: {obj} (Polarity: {polarity})")
    return beliefs