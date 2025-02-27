import pandas as pd
import os
from utils.Error_Handling import log_error

def load_data(file_path):
    if not os.path.exists(file_path):
        log_error('ERR001', f"File not found - {file_path}")
        return None

    try:
        file_extension = os.path.splitext(file_path)[-1].lower()

        if file_extension == ".csv":
            return pd.read_csv(file_path)
        elif file_extension == ".json":
            return pd.read_json(file_path)
        elif file_extension in [".xlsx", ".xls"]:
            return pd.read_excel(file_path)
        else:
            log_error("ERR002", f"Unsupported file format - {file_path}")
            return None
    except Exception as e:
        log_error("ERR002", f"Invalid data format in {file_path}: {e}")
        return None
