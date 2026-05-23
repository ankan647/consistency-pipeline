import yaml
import os

yaml_path = os.path.join("config", "model_config.yaml")

model_config_dict = {
    "chunking": {
        "chunk_size": 1200,
        "overlap": 200
    },
    "retrieval": {
        "top_k": 5
    },
    "beliefs": {
        "categories": ["fear", "values", "goals", "worldview"]
    },
    "decision": {
        "contradiction_threshold": 0.4
    }
}

# Ensure config folder exists
os.makedirs("config", exist_ok=True)

# Write YAML
with open(yaml_path, "w", encoding="utf-8") as f:
    yaml.safe_dump(model_config_dict, f, sort_keys=False)

print(f"model_config.yaml successfully written to {yaml_path}")
