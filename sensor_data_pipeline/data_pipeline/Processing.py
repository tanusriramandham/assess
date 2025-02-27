import pandas as pd
from utils.Error_Handling import log_error

def compute_monthly_stats(sensor_data):
    try:
        return sensor_data.groupby(["sensor_type", "month"]).agg(
            avg_value=("value", "mean"),
            max_value=("value", "max"),
            min_value=("value", "min")
        ).reset_index()
    except Exception as e:
        log_error("ERR003", f"Processing error - {e}")
        return None
