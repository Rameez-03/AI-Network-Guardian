import yaml
import pathlib

def load_config(config_path="configs/default.yaml"):
    """
    Load configuration from a YAML file.
    """
    path = pathlib.Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found at {path.absolute()}")
    
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    
    return config
