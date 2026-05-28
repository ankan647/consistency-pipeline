# 🚀 Real-AI Consistency Pipeline 

## 📌 Project Overview
Character consistency is the foundation of high-quality narrative data. This project implements an advanced, multi-agent validation ecosystem that analyzes character stability through psychological, physical, and causal dimensions.

By combining a **6-Gate Heuristic Framework** with a **Narrative Intelligence Suite**, this system detects contradictions while intelligently identifying and pardoning valid character growth arcs.

---

## 🧠 System Architecture: Multi-Layered Arbitration
The pipeline is divided into specialized agents, moving from fast symbolic checks to deep contextual reasoning.

### 1. The Core Logic Tier (`pipeline/`)
The foundational layer responsible for *"hard"* consistency and factual verification.
* **Consistency Checker & Validator:** The primary gates for sentiment and identity verification.
* **Chronology & Physicality:** Ensures no violations of time or physical laws (via `chronology.py` and `physical.py`).
* **Belief State Engine:** Tracks character motivations and internal logic to ensure baseline stability (via `belief_state.py`).

### 2. Narrative Intelligence Suite (`pipeline/narrative_intelligence/`)
A specialized layer for "soft" consistency—analyzing context, evolution, and social dynamics.
* **Relationship Monitor:** Tracks interpersonal dynamics for unexplained shifts (via `relationships.py`).
* **Stylometry Lab:** Monitors linguistic fingerprints and speech patterns to ensure voice consistency (via `stylometry.py`).
* **Arc Validator:** Distinguishes between accidental inconsistency and intentional character growth.
* **Causal Chains:** Maps the cause-and-effect relationship of actions to ensure narrative logic.

### 3. Advanced Reasoning Layer (`pipeline/advanced/`)
The final decision-making tier for complex character behavior.
* **Fear Reasoner:** Justifies sudden behavioral shifts based on character-specific phobias and stressors (via `fear_reasoner.py`).Psychological Modeling: Beyond basic sentiment, the system employs a specialized reasoning layer to analyze high-intensity emotional states (such as fear and stress) as valid catalysts for character change.
* **LLM Consultant:** A high-level auditor that performs final arbitration on complex "Pardon" cases using neural reasoning.



---

## 🛠️ Directory Structure
```text
KDSH/
├── main.py                     # Pipeline Orchestrator
├── pipeline/
│   ├── advanced/               # Neural Audit Layer (llm_consultant.py)
│   ├── narrative_intelligence/ # Relationship, Stylometry, and Arc Validation
│   ├── belief_state.py         # Internal Motivation Tracker
│   ├── chronology.py           # Temporal Verification
│   ├── fear_reasoner.py        # Stress/Phobia Analysis
│   ├── physical.py            # Physical Reality Verification
│   └── ...                     # Specialized Validation Agents
├── input_data.csv              # Input Dataset
└── outputs/
    └── results.csv             # Final Audit Report (XAI)
✨ Key Features
Multi-Dimensional Analysis: Goes beyond text-matching to analyze fear, causality, and stylometry.

Neuro-Symbolic Reasoning: Blends hard-coded logic gates with LLM-powered narrative auditing.

Zero-Bias Guardrails: Specifically designed to eliminate "Agreement Bias" in standard LLMs by requiring a multi-gate "Handshake."

Explainable AI (XAI): Detailed rationales in results.csv explain exactly why a story was flagged or pardoned.

🚀 Installation & Setup
1. Install Dependencies:

Bash

pip install -r requirements.txt
2. Download NLP Corpora:

Bash

python -m textblob.download_corpora
3. Execute the Pipeline:

Bash

python main.py
📊 Results Summary
The system produces a binary classification (1 for Consistent, 0 for Inconsistent) based on the consensus of the Logic Gates and the Narrative Audit.

⚖️ Conclusion
This project moves beyond simple "matching" to create a Digital Literary Critic. It ensures that character evolution is respected while strictly enforcing the rules of the narrative world.
