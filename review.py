import os
import sys
from openai import OpenAI


def review_code(code):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("ERROR: OPENAI_API_KEY is not set.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are an expert software engineer performing a code review.

Review the following Python code and identify:

1. Bugs or potential errors
2. Security issues
3. Code quality problems
4. Performance concerns
5. Recommended improvements

Give the review in a clear, structured format.

CODE:
{code}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python review.py <file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r", encoding="utf-8") as file:
            code = file.read()

        result = review_code(code)

        print("\n========== AI CODE REVIEW ==========\n")
        print(result)
        print("\n====================================\n")

    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
        sys.exit(1)