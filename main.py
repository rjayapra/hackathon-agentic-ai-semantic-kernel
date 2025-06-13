from memory.memory_loader import load_memory_from_json
from coordinator.coordinator_agent import route_query
from agents.file_agent import FileAgent
from dotenv import load_dotenv
import asyncio
from typing import Annotated
import os
from semantic_kernel.agents import ChatCompletionAgent, ChatHistoryAgentThread
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel import Kernel

load_dotenv(dotenv_path=".env")
USER_INPUTS = [
    "Explain about ENG Tech USQ-Kingston Class Applications?",
    "Thank you"
]


async def main(memory, kernel: Kernel):
    # 1. Create the agent
    agent = ChatCompletionAgent(
        kernel=kernel,
        name="QSPBot",
        instructions="Answer questions about the QSP file.",
        plugins=[FileAgent(memory)],
    )

    # 2. Create a thread to hold the conversation
    # If no thread is provided, a new thread will be
    # created and returned with the initial response
    thread: ChatHistoryAgentThread = None

    for user_input in USER_INPUTS:
        print(f"# User: {user_input}")
        # 4. Invoke the agent for a response
        response = await agent.get_response(messages=user_input, thread=thread)
        print(f"# {response.name}: {response} ")
        thread = response.thread

    # 4. Cleanup: Clear the thread
    await thread.delete() if thread else None


  

if __name__ == "__main__":
    memory = load_memory_from_json("data/sampledata.json")
    print(f"Memory loaded with {len(memory)} entries.")


    # Define the Kernel
    kernel = Kernel()
    print("Kernel initialized.")
    print(os.getenv("AZURE_OPENAI_ENDPOINT"))
    print(os.getenv("AZURE_OPENAI_API_KEY"))
    print(os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"))
    print(os.getenv("AZURE_OPENAI_BASE_URL"))
    print(os.getenv("AZURE_OPENAI_API_VERSION"))
    chatCompletionservice = AzureChatCompletion(
        endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        base_url=os.getenv("AZURE_OPENAI_BASE_URL"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION")
    )
   
    # Add the AzureChatCompletion AI Service to the Kernel
    kernel.add_service(chatCompletionservice)
    print("AzureChatCompletion service added to the Kernel.")
    asyncio.run(main(memory, kernel))
    