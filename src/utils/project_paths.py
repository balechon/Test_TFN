import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = ROOT_DIR / "data"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
FINAL_DATA_DIR = DATA_DIR / "final"

NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
SRC_DIR = ROOT_DIR / "src"
CONFIGS_DIR = ROOT_DIR / "configs"

def get_project_root() -> Path:
    """Retorna la ruta raíz del proyecto."""
    return ROOT_DIR

