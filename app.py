import streamlit as st

from workflow.graph_workflow import graph

st.set_page_config(
    page_title="Multi-Agent Customer Support",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent Customer Support System")

st.write("Ask questions related to employees, departments, tickets and company policies.")

query = st.text_input("Enter your question")

if st.button("Submit"):

    if query.strip():

        initial_state = {
            "query": query,
            "route": "",
            "retrieved_data": "",
            "response": ""
        }

        result = graph.invoke(initial_state)

        st.success("Answer")

        st.write(result["response"])