from contract import Contract

class NDA(Contract):
    def __init__(self, title, parties, confidentiality_period):
        super().__init__(title, parties)
        if not confidentiality_period:
            raise ValueError("Confidentiality period cannot be empty.")
        self.confidentiality_period = confidentiality_period

    def get_nda_details(self):
        return {
            "title": self.title,
            "parties": self.parties,
            "confidentiality_period": self.confidentiality_period
        }
