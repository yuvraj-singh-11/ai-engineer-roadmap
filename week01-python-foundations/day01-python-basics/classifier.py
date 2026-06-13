class DocumentClassifier:
    def classify(self, filename):
        if not filename:
            raise ValueError("Filename cannot be empty.")
        
        filename_lower = filename.lower()
        if "nda" in filename_lower:
            return "NDA"
        elif "report" in filename_lower or "due_diligence" in filename_lower:
            return "Due Diligence Report"
        else:
            return "Other/Unknown Contract"
