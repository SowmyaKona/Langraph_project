from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from models.state import AgentState
from tools.policy_tools import get_policy
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def policy_node(state: AgentState):
    print("\n========== Policy Agent ==========")
    print(f"Query : {state['query']}")
    print(f"Route : {state['route']}")
    query = state["query"]

    prompt = f"""
    You are an HR Policy Agent.
    Your job is to answer HR policy questions.
    If needed, use the policy tool.

    User Query:
    {query}
    """

    # Reasoning
    llm.invoke(prompt)

    # Action
    observation = get_policy.invoke({"policy_query": query})

    return {"retrieved_data": observation}