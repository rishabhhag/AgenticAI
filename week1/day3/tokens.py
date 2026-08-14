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
#3 prompts
prompt1="hi!"
prompt2="explain time travel in short"
prompt3="write an essay on machine learning in 100 words"

prompts=[prompt1, prompt2, prompt3]

for prompt in prompts:
    messages=[{
        "role": role,
        "content": prompt
    }]

    response=client.chat.completions.create(model=model, messages=messages, max_tokens=500)

    answer=response.choices[0].message.content
    #print(answer)

    usage=response.usage
    print(f"Prompt: {prompt} --> Your tokens : {usage.prompt_tokens} Completion tokens used: {usage.completion_tokens} total tokens used: {usage.
        total_tokens} finish Reason: {response.choices[0].finish_reason}")


# prompt="what is ai"

# messages=[{
#     "role": "user",
#     "content": "what is ai"
# }]

# response=client.chat.completions.create(model=model, messages=messages)

# answer=response.choices[0].message.content
# print(answer)
