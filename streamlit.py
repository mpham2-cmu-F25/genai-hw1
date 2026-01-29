from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from src.agent.graph import graph

st.title("HW1 Agent")

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message.type):
    st.write(message.content)

prompt = st.chat_input("Welcome to the agent for homework1!")

if prompt:
  st.session_state.messages.append(HumanMessage(content=prompt))
  with st.chat_message("human"):
    st.write(prompt)

  graph_input = {"messages": [HumanMessage(content=prompt)]}

  with st.chat_message("ai"):
    try:
      result = graph.invoke(graph_input)
      ai_response = result['messages'][-1]
      st.markdown(ai_response.content)
      st.session_state.messages.append(ai_response)
    except Exception as e:
      st.error(f"Error: {e}")
    
  
    

