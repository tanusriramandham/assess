import pandas as pd
from data_pipeline.Error_Handling import log_error

def save_to_csv(data, file_path):
    try:
        if data is None or data.empty:
            log_error("ERR003", f"Processing error - No data to save for {file_path}")
            return

        data.to_csv(file_path, index=False)
        print(f"Report saved to {file_path}")

    except Exception as e:
        log_error("ERR003", f"Failed to save report - {e}")

