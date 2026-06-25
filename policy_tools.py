from langchain_core.tools import tool

@tool
def get_policy(policy_query: str) -> str:
    """
    Retrieve company policy information.
    """
    query = policy_query.lower()

    with open("data/policies.txt", "r", encoding="utf-8") as file:
        data = file.read()

    sections = data.strip().split("\n\n")

    for section in sections:
        lines = section.split("\n")
        title = lines[0].replace(":", "").lower()

        title_words = title.split()

        if any(word in query for word in title_words):
            return section

    return "Policy not found."

    