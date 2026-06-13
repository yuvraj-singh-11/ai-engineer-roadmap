class DueDiligenceReport:
    def __init__(self, company_name, risk_score, review_status):
        if not company_name:
            raise ValueError("Company name cannot be empty.")
        if not isinstance(risk_score, (int, float)) or not (0 <= risk_score <= 10):
            raise ValueError("Risk score must be a number between 0 and 10.")
        if not review_status:
            raise ValueError("Review status cannot be empty.")
        self.company_name = company_name
        self.risk_score = risk_score
        self.review_status = review_status

    def generate_summary(self):
        return {
            "company_name": self.company_name,
            "risk_score": self.risk_score,
            "review_status": self.review_status
        }
