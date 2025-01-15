import random

class ThreatPredictor:
    def __init__(self):
        self.threat_types = ["Phishing", "Ransomware", "Ataque DDoS", "Malware"]

    def predict_threats(self):
        simulated_data = [
            {
                "threat_type": random.choice(self.threat_types),
                "likelihood": f"{random.randint(30, 90)}%"
            }
            for _ in range(3)
        ]
        return simulated_data