# pipeline/entity_knowledge.py
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_identities(text):
    doc = nlp(text)
    identities = []
    # Looks for 'is a', 'was a', 'became a' relationships
    for token in doc:
        if token.lemma_ == "be":
            subject = [w.text.lower() for w in token.lefts if w.dep_ == "nsubj"]
            attribute = [w.text.lower() for w in token.rights if w.dep_ == "attr"]
            if subject and attribute:
                identities.append((subject[0], attribute[0]))
    return identities