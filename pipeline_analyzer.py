import os
import re
import json
from datetime import datetime

class DataPipelineAnalyzer:
    """Simulates an advanced data parsing engine for scientific datasets and cloud infrastructure logs."""
    
    def __init__(self, input_filename="system_raw_data.log", output_filename="clean_metrics.json"):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.processed_records = 0
        self.error_count = 0

    def generate_mock_data(self):
        """Generates raw system anomalies, metrics, and timestamps to process."""
        print("[!] Generating raw dataset logs for evaluation...")
        mock_logs = [
            "TIMESTAMP:2026-09-10T10:14:22Z | METRIC_ID:101 | VALUE:42.58 | STATUS:SUCCESS\n",
            "TIMESTAMP:2026-09-10T10:15:01Z | METRIC_ID:102 | VALUE:ERR_VAL | STATUS:FAILURE\n", 
            "TIMESTAMP:2026-09-10T10:16:15Z | METRIC_ID:103 | VALUE:89.12 | STATUS:SUCCESS\n",
            "INVALID_RECORD_LINE_WITHOUT_PIPE_DELIMITER\n", 
            "TIMESTAMP:2026-09-10T10:17:45Z | METRIC_ID:104 | VALUE:12.04 | STATUS:SUCCESS\n"
        ]
        with open(self.input_filename, "w") as f:
            f.writelines(mock_logs)

    def parse_and_clean_pipeline(self):
        """Parses the data, validates data types, filters anomalies, and aggregates data."""
        if not os.path.exists(self.input_filename):
            self.generate_mock_data()

        print(f"[*] Beginning execution loop on input source: {self.input_filename}")
        cleaned_dataset = []

        with open(self.input_filename, "r") as infile:
            for line_num, line in enumerate(infile, 1):
                if not re.search(r"TIMESTAMP:.*\|.*METRIC_ID:", line):
                    print(f"  [Anomaly Detected] Row {line_num} contains structural corruption. Skipping.")
                    self.error_count += 1
                    continue
                
                try:
                    parts = {part.split(":")[0].strip(): part.split(":")[1].strip() for part in line.strip().split(" | ")}
                    metric_value = float(parts["VALUE"]) 
                    
                    record = {
                        "timestamp": parts["TIMESTAMP"],
                        "metric_id": int(parts["METRIC_ID"]),
                        "value": metric_value,
                        "status": parts["STATUS"],
                        "processed_at": datetime.utcnow().isoformat() + "Z"
                    }
                    cleaned_dataset.append(record)
                    self.processed_records += 1
                    
                except (ValueError, IndexError):
                    print(f"  [Value Error] Row {line_num} contains corrupted metrics. Skipping.")
                    self.error_count += 1
                    continue

        with open(self.output_filename, "w") as outfile:
            json.dump(cleaned_dataset, indent=4, fp=outfile)
            
        print(f"\n[+] Execution Completed Successfully.")
        print(f"    - Clean Records Processed: {self.processed_records}")
        print(f"    - System Anomalies Filtered: {self.error_count}")
        print(f"    - Output Saved To: {self.output_filename}\n")

if __name__ == "__main__":
    analyzer = DataPipelineAnalyzer()
    analyzer.parse_and_clean_pipeline()
