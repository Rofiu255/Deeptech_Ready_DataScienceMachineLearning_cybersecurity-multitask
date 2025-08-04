# src/task_config.py

task_configs = {
    "attack_type": {
        "target": "Attack Type",
        "model_path": "models/attack_type_model.pkl",
        "task_type": "classification"
    },
    "vulnerability": {
        "target": "Security Vulnerability Type",
        "model_path": "models/vulnerability_model.pkl",
        "task_type": "classification"
    },
    "defense": {
        "target": "Defense Mechanism Used",
        "model_path": "models/defense_model.pkl",
        "task_type": "classification"
    },
    "loss": {
        "target": "Financial Loss (in Million $)",
        "model_path": "models/loss_model.pkl",
        "task_type": "regression"
    },
    "resolution": {
        "target": "Incident Resolution Time (in Hours)",
        "model_path": "models/resolution_model.pkl",
        "task_type": "regression"
    }
}
