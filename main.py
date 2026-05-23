import os
import logging
import pandas as pd
from pipeline.retriever import setup_retriever
from pipeline.belief_extractor import extract_beliefs
from pipeline.consistency_checker import check_consistency
from pipeline.entity_knowledge import extract_identities
from pipeline.validator import validate_identity
from pipeline.chronology import check_chronology
from pipeline.stylometry import check_style_consistency 
from pipeline.relationships import check_social_consistency
from pipeline.physical import check_physical_consistency
from pipeline.narrative_intelligence.arc_validator import validate_narrative_arc
from pipeline.advanced.llm_consultant import consult_llm_on_arc

# --- Professional Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    # 1. Setup Paths
    base_dir = os.getcwd()
    novels_dir = os.path.join(base_dir, "data", "novels")
    backstories_dir = os.path.join(base_dir, "data", "backstories")
    output_dir = os.path.join(base_dir, "outputs")
    os.makedirs(output_dir, exist_ok=True)

    logger.info("🚀 Starting Real-AI Consistency Pipeline [Track A]")

    # 2. Initialize Pathway
    pathway_table = setup_retriever(novels_dir)
    if pathway_table is None:
        logger.error("Failed to initialize Pathway. Exiting.")
        return

    results = []

    # 3. Process Stories
    backstory_files = [f for f in os.listdir(backstories_dir) if f.endswith(".txt")]
    
    for filename in backstory_files:
        story_id = filename.replace(".txt", "")
        logger.info(f"--- 🧠 Analyzing Story ID: {story_id} ---")

        with open(os.path.join(backstories_dir, filename), 'r', encoding='utf-8') as f:
            backstory_text = f.read()
        
        # STEP A: Extraction
        beliefs = extract_beliefs(backstory_text)
        identities = extract_identities(backstory_text)
        
        # Load Novel
        novel_path = os.path.join(novels_dir, f"{story_id}.txt")
        if not os.path.exists(novel_path):
            continue
            
        with open(novel_path, 'r', encoding='utf-8') as f:
            novel_text = f.read()
            novel_chunks = [novel_text] 

        # --- STEP B: THE THREE GATES OF CONSISTENCY ---
        final_prediction = 1
        final_rationale = "Consistent behavior, identity, and chronology."

        # GATE 1: Chronology (Check Time Facts First)
        chrono_check = check_chronology(backstory_text, novel_text)
        if not chrono_check["is_consistent"]:
            final_prediction = 0
            final_rationale = chrono_check["reason"]
        
        # GATE 2: Identity (Check if they are who they say they are)
        if final_prediction == 1: 
            validation = validate_identity(identities, novel_text)
            if not validation["is_valid"]:
                final_prediction = 0
                final_rationale = validation["reason"]

        # GATE 3: Semantic/Sentiment (Check if they act how they feel)
        if final_prediction == 1:
            for belief in beliefs:
                check_result = check_consistency(belief, novel_chunks)
                if check_result["prediction"] == 0:
                    final_prediction = 0
                    final_rationale = check_result["rationale"]
                    break 
        # GATE 4: Stylometry (The 'Voice' Check)
        if final_prediction == 1:
            style_check = check_style_consistency(backstory_text, novel_text)
            if not style_check["is_consistent"]:
                final_prediction = 0
                final_rationale = style_check["reason"]
        # GATE 5: Social/Relationship Gate
        if final_prediction == 1:
            social_check = check_social_consistency(backstory_text, novel_text)
            if not social_check["is_consistent"]:
                final_prediction = 0
                final_rationale = social_check["reason"]
        if final_prediction == 1:
            phys_check = check_physical_consistency(backstory_text, novel_text)
            if not phys_check["is_consistent"]:
                final_prediction = 0
                final_rationale = phys_check["reason"]
        # --- NUCLEAR OPTION: STRICT APPEAL STAGE ---
        # --- 🚀 ENHANCED ATTRACTIVE APPEAL STAGE ---
        if final_prediction == 0:
            # Save the original reason from the Gates
            gate_reason = final_rationale
            
            is_major_clash = "contradicts" in gate_reason.lower()

            # 1. LAYER 1: Narrative Intelligence (Local Arc Check)
            if not is_major_clash:
                arc_check = validate_narrative_arc(gate_reason, novel_text)
                if arc_check["is_valid_arc"]:
                    final_prediction = 1
                    final_rationale = f"✅ PARDONED: {arc_check['reason']}"
            
            # 2. LAYER 2: LLM Supreme Court (Deep Verification)
            # --- 🚀 THE IRONCLAD AUDIT SYSTEM ---
            if final_prediction == 0:
                llm_opinion = consult_llm_on_arc(final_rationale, novel_text)
                
                # Use strict matching for the pardon
                # We ONLY change it to 1 if BOTH 'CONSISTENT' and 'GROWTH ARC' are present
                if "CONSISTENT" in llm_opinion.upper() and "GROWTH ARC" in llm_opinion.upper():
                    final_prediction = 1
                    final_rationale = f"✅ [PARDONED] -> {llm_opinion}"
                else:
                    # IMPORTANT: Keep the gate_reason so we know WHY it failed
                    final_prediction = 0 
                    final_rationale = f"❌ [GATE FAIL]: {gate_reason} | ⚖️ [AUDIT]: {llm_opinion}"
        results.append({
            "story_id": story_id,
            "prediction": final_prediction,
            "rationale": final_rationale
        })
        logger.info(f"Final Decision for {story_id}: {final_prediction}")

    # 4. Save to CSV
    df = pd.DataFrame(results)
    output_path = os.path.join(output_dir, "results.csv")
    df.to_csv(output_path, index=False)
    logger.info(f"✅ Pipeline complete. Results saved to: {output_path}")

if __name__ == "__main__":
    main()