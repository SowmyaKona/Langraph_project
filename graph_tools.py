from langchain_core.tools import tool

@tool
def get_employee_info(query: str) -> str:
    """
    Retrieve employee, department, manager and ticket information.
    """
    
    employees = {
        "ai department": "AI Department is managed by Anil.",
        "hr department": "HR Department is managed by Priya.",
        "john": "John works in the AI Department.",
        "ticket 101": "Ticket 101 is assigned to Rahul."
    }

    query = query.lower()

    for key, value in employees.items():
        if key in query:
            return value

    return "Information not found."