import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile" 
role="user"
prompt="suggest me a name for food company"

message_system={
    "role": "system",
    "content": "you are brand manager who suggests me best brand name for my product for my food company give me only one name"
}

messages=[message_system, {
    "role": role,
    "content": prompt
}]

response=client.chat.completions.create(model=model, messages=messages,temperature=2)#defines creativity of the model

print(response)

answer=response.choices[0].message.content
print(answer)
