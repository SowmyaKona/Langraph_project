from typing_extensions import TypedDict

class AgentState(TypedDict):
    query: str
    route: str
    retrieved_data: str
    response: str

    