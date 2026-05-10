from dotenv import load_dotenv
import os 
from google import genai 
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash-lite", 
    contents="What is the capital of France?"
)

print(response.text) 

# from google import genai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# print("API KEY EXISTS:", bool(os.getenv("GEMINI_API_KEY")))

# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )

# models = client.models.list()

# for m in models:
#     print(m.name)