# Day 2 - Advanced Python Legal Document Management System

## Overview

This project is part of the AI Engineer Roadmap.

The goal of this project is to learn advanced Python concepts by building a simple Legal Document Management System. The application reads legal documents from text files, stores them as Python objects, performs search operations, and persists document data into JSON format.

This project introduces concepts that will later be used in:

* RAG (Retrieval Augmented Generation)
* Document Ingestion Pipelines
* Legal AI Systems
* Due Diligence Platforms
* Vector Database Workflows

---

## Features

### Document Management

* Create legal document objects
* Store multiple documents in memory
* Remove documents
* Display all documents

### Search Functionality

* Search documents by title
* Search documents by document type

### JSON Persistence

* Save documents to JSON
* Load documents from JSON

### File Handling

* Read legal documents from text files
* Process document content

### Error Handling

* Handle missing files
* Handle JSON loading errors

---

## Project Structure

```text
day02-advanced-python/

├── legal_document.py
├── document_manager.py
├── main.py
├── README.md
└── data/
    ├── sample_contract.txt
    ├── sample_nda.txt
    └── documents.json
```

---

## Technologies Used

* Python 3
* JSON
* Object-Oriented Programming (OOP)
* File Handling
* Exception Handling

---

## Concepts Practiced

### Python Collections

* Lists
* Dictionaries

### Object-Oriented Programming

* Classes
* Objects
* Constructors
* Methods

### Data Persistence

* JSON Serialization
* JSON Deserialization

### Error Handling

* try
* except
* FileNotFoundError

---

## How to Run

Navigate to the project directory:

```bash
cd day02-advanced-python
```

Run the application:

```bash
python main.py
```

---

## Sample Output

```text
===== LEGAL DOCUMENT MANAGEMENT SYSTEM =====

Document 'Employment Agreement' added successfully.
Document 'Vendor NDA' added successfully.

Listing Documents:

===== DOCUMENT LIST =====

ID: 1
Title: Employment Agreement
Type: Contract

ID: 2
Title: Vendor NDA
Type: NDA

Document Count By Type:

Contract: 1
NDA: 1

Documents saved successfully.
Documents loaded successfully.
```

---

## Learning Outcomes

After completing this project, I learned:

* How to design Python classes
* How to manage collections of objects
* How to read and write files
* How to work with JSON data
* How to implement search functionality
* How to handle exceptions properly
* How legal documents can be represented programmatically

---

## Future Improvements

* Add menu-driven user interface
* Add document classification
* Add PDF document support
* Add document metadata extraction
* Integrate vector databases
* Build a RAG pipeline

---

## Git Commit

```bash
git add .
git commit -m "Day 2 - Advanced Python document management system"
git push
```
