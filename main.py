import pandas as pd
from data_pipeline.Data_Ingestion import load_data
from data_pipeline.Processing import compute_monthly_stats
from data_pipeline.Outlier_Detection import detect_outliers
from utils.Error_Handling import log_error
from utils.Reporting import save_to_csv

sensor_data_file = "data/sensor_data.csv"
thresholds_file = "data/thresholds.csv"
monthly_stats_file = "output/monthly_stats.csv"
outliers_file = "output/outliers.csv"

# Load data (Supports CSV, JSON, Excel)
sensor_data = load_data(sensor_data_file)
thresholds = load_data(thresholds_file)

if sensor_data is not None and thresholds is not None:
    try:
        # Convert value column to numeric
        sensor_data["value"] = pd.to_numeric(sensor_data["value"], errors='coerce')
        sensor_data = sensor_data.dropna()

        # Compute Monthly Statistics
        monthly_stats = compute_monthly_stats(sensor_data)
        save_to_csv(monthly_stats, monthly_stats_file)

        # Detect Outliers
        outliers = detect_outliers(sensor_data, thresholds)
        if outliers is not None:
            save_to_csv(outliers, outliers_file)

    except Exception as e:
        log_error("ERR003", f"Processing error - {e}")
