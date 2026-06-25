from langchain_google_genai import ChatGoogleGenerativeAI
from models.schemas import RouteDecision
from models.state import AgentState
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY")
)
structured_llm = llm.with_structured_output(RouteDecision)

# ---------------------
# Create Classifier Node
# ---------------------
def classifier_node(state: AgentState):
    print("\n========== Classifier Agent ==========")
    print(f"Query : {state['query']}")
    query = state['query']

    result = structured_llm.invoke(
        f"""
        You are a query classifier.
        Classify the query into one of these routes:

        policy 
        graph

        policy :
        if query is about -
        - leave policy 
        - notice period
        - work from home policy

        graph:
        if the query is about - 
        - employee information
        - department information
        - manager information
        - ticket information

        Query:{query}
        """
    )
    return {"route":result.route}




