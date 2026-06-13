print("Hello from main.py!")
import json

from nda import NDA
from report import DueDiligenceReport
from classifier import DocumentClassifier


def main():

    try:

        nda = NDA(
            title="Vendor NDA",
            parties=["Lexlegis", "ABC Corp"],
            confidentiality_period="2 Years"
        )

        report = DueDiligenceReport(
            company_name="ABC Corp",
            risk_score=7,
            review_status="Under Review"
        )

        classifier = DocumentClassifier()

        classification = classifier.classify("nda.pdf")

        response = {
            "classification": classification,
            "nda_details": nda.get_nda_details(),
            "report_summary": report.generate_summary()
        }

        print(json.dumps(response, indent=4))

    except ValueError as e:
        print(f"Validation Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()