
import os
import base64
from openai import AzureOpenAI

endpoint = os.getenv("ENDPOINT_URL", "https://learnopenai-rj.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "chat")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY","XXX")

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)


#Prepare the chat prompt
chat_prompt = [
    {
        "role": "user",
        "content": "Write a short story about a time traveler who accidentally changes a major historical event."
    },
    {
        "role": "assistant",
        "content": "In the year 2150, a brilliant scientist named Dr. Emily Wells had created a revolutionary time machine that could transport people to any point in history. Eager to test her invention, she decided to travel back to the year 1963, hoping to witness the famous speech given by Martin Luther King Jr. during the March on Washington.\n\nAs Dr. Wells arrived in Washington D.C. on the day of the march, she couldn't contain her excitement. She blended in with the crowd and listened intently as Martin Luther King Jr. delivered his iconic \"I Have a Dream\" speech. However, in a moment of distraction, Dr."
    }
]

# Include speech result if speech is enabled
messages = chat_prompt

# Generate the completion
completion = client.chat.completions.create(
    model=deployment,
    messages=messages,
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(completion.to_json())
    