from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

from models.state import AgentState
from tools.graph_tools import get_employee_info

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def graph_node(state: AgentState):
    print("\n========== Graph Agent ==========")
    print(f"Query : {state['query']}")
    print(f"Route : {state['route']}")
    query = state["query"]

    prompt = f"""
    You are an Employee Information Agent.
    Answer employee, department, manager and ticket related questions.

    User Query:
    {query}
    """

    # Reasoning
    llm.invoke(prompt)

    # Action
    observation = get_employee_info.invoke({"query": query})

    return {"retrieved_data": observation}