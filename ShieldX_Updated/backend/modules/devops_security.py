class DevOpsSecurity:
    def __init__(self):
        self.vulnerabilities = []

    def analyze_pipeline(self, pipeline_name):
        self.vulnerabilities.append({"pipeline": pipeline_name, "issues": ["Hardcoded Secrets", "Open Ports"]})
        return {"pipeline": pipeline_name, "issues": ["Hardcoded Secrets", "Open Ports"], "message": "Análise realizada."}
