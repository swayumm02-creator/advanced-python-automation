import json
import math

class MatrixValidator:
    """Simulates a space-tech telemetry matrix processor to clean multi-dimensional scientific array nodes."""
    
    def __init__(self, sensor_data=None):
        
        self.sensor_data = sensor_data or [
            {"node": "Alpha", "coordinate": [12.5, 45.1, 102.4], "intensity": 850},
            {"node": "Beta", "coordinate": [0.0, 0.0, 0.0], "intensity": 0},          # Null node anomaly
            {"node": "Gamma", "coordinate": [14.2, 43.8, 98.1], "intensity": 920}
        ]

    def optimize_and_filter_nodes(self):
        print("[*] Initiating high-precision matrix spatial transformation matrix...")
        processed_matrix = []
        
        for record in self.sensor_data:
            coords = record["coordinate"]
        
            if sum(coords) == 0.0 or record["intensity"] <= 0:
                print(f"  [Matrix Anomaly] Dropping inactive sensor array coordinate: {record['node']}")
                continue
                
            # Compute vector magnitude (spatial distance formula)
            distance = math.sqrt(coords[0]**2 + coords[1]**2 + coords[2]**2)
            
            optimized_node = {
                "sensor_node": record["node"],
                "vector_magnitude": round(distance, 4),
                "scaled_intensity": round(record["intensity"] * 1.15, 2),
                "validated": True
            }
            processed_matrix.append(optimized_node)
            
        print("\n[+] Spatial Matrix Compilation Complete:")
        print(json.dumps(processed_matrix, indent=4))
        return processed_matrix

if __name__ == "__main__":
    validator = MatrixValidator()
    validator.optimize_and_filter_nodes()
