import pandas as pd
from utils.Error_Handling import log_error

def detect_outliers(sensor_data, thresholds):
    try:
        outliers = sensor_data.merge(thresholds, on="sensor_type", how="left")

        if outliers["min_threshold"].isnull().any() or outliers["max_threshold"].isnull().any():
            log_error("ERR004", "Thresholds not defined for some sensor types.")
            return None

        outliers = outliers[(outliers["value"] < outliers["min_threshold"]) | (outliers["value"] > outliers["max_threshold"])]
        outliers["threshold_exceeded"] = outliers.apply(
            lambda row: "Min" if row["value"] < row["min_threshold"] else "Max", axis=1
        )
        return outliers[["date", "sensor_type", "value", "unit", "location_id", "threshold_exceeded"]]

    except Exception as e:
        log_error("ERR003", f"Processing error in outlier detection - {e}")
        return None
