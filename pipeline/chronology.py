# pipeline/chronology.py
import re

def check_chronology(backstory_text, novel_text):
    """
    Detects if the novel contradicts 'Time Facts' from the backstory.
    """
    # Look for numbers followed by 'years', 'months', or 'days'
    time_pattern = r'(\d+)\s+(year|month|day|decade)'
    
    back_times = re.findall(time_pattern, backstory_text.lower())
    novel_mentions = re.findall(time_pattern, novel_text.lower())
    
    if back_times and novel_mentions:
        for b_val, b_unit in back_times:
            for n_val, n_unit in novel_mentions:
                # If units match but numbers are drastically different
                # Example: '14 years' in prison vs '2 days' in prison
                if b_unit == n_unit and b_val != n_val:
                    # We only flag if the context is similar (e.g., both mention 'prison')
                    if "prison" in backstory_text and "prison" in novel_text:
                        return {
                            "is_consistent": False,
                            "reason": f"Temporal Clash: Backstory says {b_val} {b_unit}s, but novel says {n_val} {n_unit}s."
                        }
    return {"is_consistent": True, "reason": None}