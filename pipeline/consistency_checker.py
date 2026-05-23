from textblob import TextBlob

def check_consistency(belief, chunks):
    threshold = 0.35 # Sensitivity buffer
    
    for chunk in chunks:
        subject = belief.subject.lower()
        chunk_low = chunk.lower()
        
        if subject in chunk_low:
            blob = TextBlob(chunk)
            sentiment = blob.sentiment.polarity
            
            print(f"   🔎 [DEBUG] Checking Subject: '{subject}' | Novel Sentiment: {sentiment:.2f}")

            # CASE 1: Negative Trait (Fear/Hate) vs Positive Action
            if belief.polarity < 0 and sentiment > threshold:
                return {
                    "prediction": 0, 
                    "rationale": f"Inconsistent: Negative trait for {subject} contradicts positive novel sentiment."
                }
            
            # CASE 2: Positive Trait (Rich/Love) vs Negative Action (Poor/Begging)
            if belief.polarity > 0 and sentiment < -threshold:
                return {
                    "prediction": 0, 
                    "rationale": f"Inconsistent: Positive trait for {subject} contradicts negative novel sentiment."
                }
                
    return {"prediction": 1, "rationale": "Consistent."}