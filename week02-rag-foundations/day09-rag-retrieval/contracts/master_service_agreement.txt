sections = [
    ("PARTIES", """
This Master Service Agreement ("Agreement") is entered into between Alpha Technologies Private Limited ("Client")
and Beta Solutions Private Limited ("Service Provider").
"""),

    ("SERVICES", """
The Service Provider shall provide software development, maintenance, testing,
deployment, infrastructure support, consulting services, artificial intelligence development,
machine learning model development, data processing and analytics services.
""" * 20),

    ("PAYMENT TERMS", """
The Client shall pay all undisputed invoices within thirty (30) days from the date of invoice.
Late payments may attract interest at the rate of one percent (1%) per month.
The Service Provider shall submit invoices on a monthly basis.
""" * 20),

    ("CONFIDENTIALITY", """
Each Party agrees to maintain all Confidential Information in strict confidence.
Confidential Information shall not be disclosed to any third party without prior written consent.
The confidentiality obligations shall survive termination of this Agreement for five years.
""" * 30),

    ("INTELLECTUAL PROPERTY", """
All Intellectual Property Rights created under this Agreement shall belong exclusively to the Client.
The Service Provider hereby assigns all rights, title and interest in deliverables to the Client.
""" * 30),

    ("DATA PROTECTION", """
The Parties shall comply with applicable privacy laws and data protection regulations.
Personal Data shall only be processed for authorized business purposes.
Appropriate technical and organizational security measures shall be implemented.
""" * 30),

    ("LIMITATION OF LIABILITY", """
Neither Party shall be liable for indirect, incidental, consequential or punitive damages.
The aggregate liability shall not exceed the fees paid under this Agreement during the preceding twelve months.
""" * 30),

    ("INDEMNIFICATION", """
The Service Provider shall indemnify and hold harmless the Client from claims,
damages, liabilities, costs and expenses arising from breach of this Agreement.
""" * 30),

    ("TERMINATION", """
Either Party may terminate this Agreement upon thirty (30) days prior written notice.
The Client may immediately terminate the Agreement for material breach.
All confidential information shall be returned upon termination.
""" * 30),

    ("FORCE MAJEURE", """
Neither Party shall be liable for delays caused by events beyond reasonable control,
including natural disasters, war, terrorism, pandemics and government restrictions.
""" * 20),

    ("GOVERNING LAW", """
This Agreement shall be governed by and construed in accordance with the laws of India.
Any disputes shall be subject to the exclusive jurisdiction of courts located in Mumbai.
""" * 20),
]

with open("contracts/master_service_agreement.txt", "w") as f:
    f.write("MASTER SERVICE AGREEMENT\n\n")

    for title, content in sections:
        f.write(f"\n{'='*80}\n")
        f.write(f"{title}\n")
        f.write(f"{'='*80}\n")
        f.write(content)
        f.write("\n")