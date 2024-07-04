# Resume Parser

This project is a simple resume parser that uses the OpenAI GPT-4 model to convert resume text into a structured JSON format. The parser extracts key information such as Name, Title, Education, Technical Skills, Work Experience, Certifications, and Projects.

## Requirements

- Python 3.x
- OpenAI Python client library (version 1.35.10 or later)

## Installation

1. Clone the repository or download the script.
2. Create and activate a virtual environment (optional but recommended).
3. Install the required packages:

```sh
pip install openai
```

## Usage

1. Add your OpenAI API key in the script:

```python
openai.api_key = "your-api-key-here"
```

2. Place the resume text in a file named `resume.txt` in the same directory as the script.

3. Run the script:

```sh
python resumeParser.py
```

The parsed JSON output will be printed to the console.

## Example

### Input (resume.txt)

```
John Doe
Software Engineer

Education:
- B.Sc. in Computer Science, University XYZ, 2016

Technical Skills:
- Python, Java, SQL

Work Experience:
- Software Engineer at ABC Corp, 2017-present

Certifications:
- AWS Certified Solutions Architect

Projects:
- Developed a web application for managing tasks
```

### Output

```json
{
    "Name": "John Doe",
    "Title": "Software Engineer",
    "Education": [
        "B.Sc. in Computer Science, University XYZ, 2016"
    ],
    "Technical Skills": [
        "Python",
        "Java",
        "SQL"
    ],
    "Work Experience": [
        "Software Engineer at ABC Corp, 2017-present"
    ],
    "Certifications": [
        "AWS Certified Solutions Architect"
    ],
    "Projects": [
        "Developed a web application for managing tasks"
    ]
}
```

## Notes

- Make sure to replace `"your-api-key-here"` with your actual OpenAI API key.
- This project is an assignment by [PiBit AI](https://www.pibit.ai/).

## License

This project is licensed under the MIT License.
