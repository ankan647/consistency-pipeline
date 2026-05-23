from dataclasses import dataclass

@dataclass
class BeliefState:    # <--- Make sure 'B' and 'S' are Capitalized
    pathway: str      
    subject: str      
    original_text: str 
    polarity: int