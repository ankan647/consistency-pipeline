import yaml
import os

yaml_path = os.path.join("config", "paths.yaml")

paths_dict = {
    "data": {
        "novels_dir": "data/novels",
        "backstories_dir": "data/backstories"
    },
    "output": {
        "results_file": "outputs/results.csv",
        "logs_file": "outputs/logs.txt"
    }
}

# Ensure config folder exists
os.makedirs("config", exist_ok=True)

# Write YAML
with open(yaml_path, "w", encoding="utf-8") as f:
    yaml.safe_dump(paths_dict, f, sort_keys=False)

print(f"paths.yaml successfully written to {yaml_path}")
