class Contract:
    def __init__(self, title, parties):
        if not title:
            raise ValueError("Contract title cannot be empty.")
        if not isinstance(parties, list) or len(parties) < 2:
            raise ValueError("Contract must have at least two parties.")
        self.title = title
        self.parties = parties
