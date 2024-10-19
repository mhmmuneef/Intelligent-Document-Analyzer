# Intelligent Document Analyzer

## Description

The Intelligent Document Analyzer is a web application that allows users to upload documents (PDF or DOCX) and extract relevant entities using Azure's Text Analytics service. This application can help analyze and understand documents by identifying key entities within the text.

## Features

- Upload PDF and DOCX documents.
- Extract text from uploaded documents.
- Analyze text to identify entities using Azure Text Analytics.
- Display results with entity details, including text, category, and confidence score.
- Save document and analysis results to a database.

## Technologies Used

- **Frontend**: HTML, CSS (with a responsive design)
- **Backend**: Flask (Python web framework)
- **Database**: SQLAlchemy with a Microsoft SQL Server backend
- **Cloud Services**: Azure Text Analytics API
- **Dependencies**:
    - Flask
    - PyPDF2
    - python-docx
    - SQLAlchemy
    - azure-ai-textanalytics
    - python-dotenv
    - PyCryptodome (for PDF handling)

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/mhmmuneef/intelligent-document-analyzer.git
   cd intelligent-document-analyzer
