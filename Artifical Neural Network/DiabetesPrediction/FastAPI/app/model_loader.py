from pathlib import Path
import joblib
from tensorflow.keras.models import load_model

BASE_DIR = Path(__file__).resolve().parents[1]  # -> FastAPI/

MODEL_PATH = BASE_DIR / "model" / "best_ann_model.h5"
SCALER_PATH = BASE_DIR / "model" / "scaler.pkl"
COLUMNS_PATH = BASE_DIR / "model" / "columns.pkl"

model = load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
columns = joblib.load(COLUMNS_PATH)