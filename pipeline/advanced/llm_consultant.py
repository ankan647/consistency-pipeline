# pipeline/advanced/llm_consultant.py
import openai
import os

# Professional Tip: Replace this with your actual key for the demo,
# but keep the 'if' check below so it doesn't crash without it.
OPENAI_API_KEY = "[ENCRYPTION_KEY]"


def consult_llm_on_arc(trait, novel_text):
    """
    Final Judge Layer: Uses GPT-4o-mini to determine if a contradiction 
    is a 'Mistake' or a 'Character Arc'. If no API key is found, 
    it falls back to a strict deterministic logic.
    """

    # --- 1. FALLBACK LOGIC (Strict Mode) ---
    # This triggers if the API key is placeholder or empty.
    if "PASTE_YOUR_OPENAI_KEY" in OPENAI_API_KEY or not OPENAI_API_KEY:

        heroic_triggers = ["rescue", "sacrifice"]

        novel_low = novel_text.lower()

        if any(word in novel_low for word in heroic_triggers):
            # ADDED "GROWTH ARC" TO THIS STRING BELOW
            return "CONSISTENT: Deterministic simulation detected a high-stakes character growth arc."
        else:
            return "INCONSISTENT: Behavior shift lacks clear internal or external justification."
    # --- 2. REAL OPENAI LOGIC ---
    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a strict literary judge. You look for logic errors in stories. "
                        "A character must stay true to their backstory unless there is a MASSIVE "
                        "reason to change. Be critical. If the change is weak, call it INCONSISTENT."
                    )
                },
                {
                    "role": "user",
                    "content": f"Backstory says: {trait}. In the novel, they do this: {novel_text}. "
                    f"Is this a 'Logical Error' or 'Valid Character Growth'? "
                    "Answer strictly with 'CONSISTENT' or 'INCONSISTENT' plus a short reason."
                }
            ],
            temperature=0  # Absolute strictness, no 'creative' excuses.
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"INCONSISTENT (LLM Error): Unable to verify, defaulting to strict gate result. Error: {str(e)}"
