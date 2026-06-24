TEST_QUESTIONS = [
    {
        "question": "What is the notice period for resignation?",
        "expected_sources": ["employment.txt"],
        "expected_keywords": ["90 days", "notice"]
    },
    {
        "question": "Which agreements contain termination clauses?",
        "expected_sources": ["nda.txt", "employment.txt", "msa.txt"],
        "expected_keywords": ["termination", "terminate", "cease", "discontinue", "end"]
    },
]