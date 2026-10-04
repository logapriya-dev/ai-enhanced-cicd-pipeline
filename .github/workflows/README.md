# AI-Enhanced CI/CD Pipeline with LLM-Based Code Review

An AI-enhanced CI/CD pipeline that automatically reviews application code using an LLM whenever code is pushed to GitHub.

## 🚀 Project Overview

This project integrates AI-powered code review into a CI/CD workflow.

Whenever code is pushed to the `main` branch, GitHub Actions automatically:

1. Checks out the source code
2. Sets up the Python environment
3. Installs project dependencies
4. Runs the application
5. Sends the source code to an LLM for code review
6. Generates feedback on bugs, security, code quality, and improvements

## 🏗️ Architecture

Developer
   ↓
Git Push
   ↓
GitHub Repository
   ↓
GitHub Actions
   ↓
Python Environment
   ↓
Application Test
   ↓
AI Code Review
   ↓
LLM Feedback

## 🛠️ Technologies Used

- Python
- Git
- GitHub
- GitHub Actions
- OpenAI API
- CI/CD
- YAML

## 📁 Project Structure

```text
ai-enhanced-cicd-pipeline/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── main.py
├── review.py
├── requirements.txt
└── README.md