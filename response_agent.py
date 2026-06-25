from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from models.state import AgentState

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def response_node(state: AgentState):
    print("\n========== Response Agent ==========")
    print(f"Query : {state['query']}")
    print(f"Retrieved Data :\n{state['retrieved_data']}")

    prompt = f"""
You are an AI Customer Support Assistant.

Use ONLY the retrieved information below to answer the user's question.

If the retrieved information says "Information not found" or "Policy not found",
reply politely that the requested information is unavailable.

User Question:
{state["query"]}

Retrieved Information:
{state["retrieved_data"]}

Generate a concise, professional and user-friendly response.
"""

    response = llm.invoke(prompt)

    return {"response": response.content}