# HireLens: AI-Powered Resume Analysis 📄🤖

## Overview

HireLens is an intelligent resume analysis tool that leverages AI to provide comprehensive insights for job seekers. The application helps candidates optimize their resumes by analyzing ATS compatibility, identifying missing keywords, and generating personality insights.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-green)
![AI Powered](https://img.shields.io/badge/AI-Powered-orange)

## Features

- 🤖 ATS Score Analysis
- 👤 Candidate Personality Insights
- 🔑 Missing Keywords Detection
- 📄 PDF Resume Support
- 🌐 User-Friendly Web Interface

## Prerequisites

- Python 3.8+
- Streamlit
- Google Gemini API Access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Shantnu-singh/Hire-Lens
cd app
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root with the following variables:

```env
# Google Gemini API Configuration
GOOGLE_API_KEY=your_gemini_api_key_here

# PDF Processing Settings
POPPER_DIRECTORY_PATH =/path/to/popper/Library/bin

```

### API Key Setup

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key for Gemini
3. Copy the API key to your `.env` file

## Running the Application

```bash
streamlit run app.py
```


## Usage

1. Navigate to the web interface
2. Paste the job description
3. Upload your PDF resume
4. Choose analysis type:
   - ATS Score
   - Candidate Profile
   - Missing Keywords

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

