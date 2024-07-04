from openai import OpenAI

# Initialize OpenAI API key
client = OpenAI(
    api_key = "api-key-here"
)

# Function to parse resume text to JSON using ChatGPT
def parse_resume_to_json(resume_text):
    prompt = f"""
    Take the following resume text as input and parse the content into JSON format:
    
    {resume_text}
    
    The JSON format should include the following fields:
    - Name
    - Title
    - Education
    - Technical Skills
    - Work Experience
    - Certifications
    - Projects
    
    Please provide the JSON output.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            n=1,
            stop=None,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except OpenAI.APIConnectionError as e:
        print("The server could not be reached")
        print(e.__cause__)  # an underlying Exception, likely raised within httpx.
    except OpenAI.RateLimitError as e:
        print("A 429 status code was received; we should back off a bit.")
    except OpenAI.APIStatusError as e:
        print("Another non-200-range status code was received")
        print(e.status_code)
        print(e.response)

# Read the resume text from a file
try:
    with open('resume.txt', 'r') as file:
        resume_text = file.read()
except FileNotFoundError:
    print("The resume.txt file was not found.")
    resume_text = ""

# Parse the resume text if it was successfully read
if resume_text:
    parsed_json = parse_resume_to_json(resume_text)
    print(parsed_json)
