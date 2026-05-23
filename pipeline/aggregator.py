class ConsistencyAggregator:
    def __init__(self): self.findings = []
    def add_finding(self, finding): self.findings.append(finding)
    def aggregate(self):
        for f in self.findings:
            if f["prediction"] == 0: return f
        return {"prediction": 1, "rationale": "Consistent."}
