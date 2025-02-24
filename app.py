import streamlit as st
import requests
import uuid
import json

# API endpoint URL for prediction
API_URL = "http://localhost:3000/api/v1/prediction/9719e978-fd79-4050-8bea-99724ecdb992"

# Set page title and overview
st.title("Multi-Agent AI Stock/ETF Analysis Tool 📉 📈")
st.markdown("## 📌 Overview")
st.markdown("""
    Advanced analytics platform combining three AI-powered analysis methodologies:
    A supervisor oversees three workers and delegates tasks to the following workers:
    1. **📊 Fundamental Analysis for {prompt}** - Financial health & valuation metrics  
    2. **📈 Technical Analysis for {prompt}** - Price patterns & trading signals  
    3. **🧠 Sentiment Analysis for {prompt}** - Market psychology & news trends  
""")

# Initialize session state for chat messages, chat ID, and agent messages if not already set
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'chat_id' not in st.session_state:
    st.session_state.chat_id = str(uuid.uuid4())
if 'agent_messages' not in st.session_state:
    st.session_state.agent_messages = {}

# Display chat history from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input for a stock/ETF query
if prompt := st.chat_input("Ask about a stock/ETF..."):
    # Add user's message to session state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Prepare the payload for the API
        payload = {
            "question": prompt,
            "chatId": st.session_state.chat_id,
            "streaming": True
        }

        # Create a placeholder for dynamic response updates
        full_response = ""
        placeholder = st.empty()
        sources = set()

        # Make a streaming POST request to the API
        with requests.post(API_URL, json=payload, stream=True) as response:
            response.raise_for_status()

            # Process streamed chunks from the API
            for chunk in response.iter_lines():
                if chunk:
                    decoded_chunk = chunk.decode('utf-8')
                    
                    # Process only chunks starting with 'data:'
                    if decoded_chunk.startswith('data:'):
                        try:
                            data = json.loads(decoded_chunk[5:])
                            
                            # Process agent reasoning events
                            if data.get('event') == 'agentReasoning':
                                for agent in data.get('data', []):
                                    agent_name = agent.get('agentName', '')
                                    messages = agent.get('messages', [])
                                    if not agent_name or not messages:
                                        continue
                                    
                                    # Determine the section key based on agent name
                                    if "Fundamental Analysis Specialist" in agent_name:
                                        section_key = "📊 Fundamental Analysis"
                                    elif "Technical Analysis Expert" in agent_name:
                                        section_key = "📈 Technical Analysis"
                                    elif "Market Sentiment Analyst" in agent_name:
                                        section_key = "🧠 Sentiment Analysis"
                                    else:
                                        section_key = agent_name  # fallback

                                    # Clean the messages from the agent
                                    new_messages = [msg.replace("**", "").strip() 
                                                    for msg in messages 
                                                    if isinstance(msg, str) and msg.strip()]
                                    
                                    # If in the Technical Analysis section, check for duplicate fundamental content
                                    if section_key == "📈 Technical Analysis" and new_messages:
                                        if new_messages[0].startswith("Fundamental Analysis Report:"):
                                            # Skip updating the Technical Analysis section if it starts with duplicate text
                                            continue

                                    # Replace the entire section with the new cumulative messages
                                    st.session_state.agent_messages[section_key] = new_messages
                            
                            # Rebuild the full_response from current agent messages in session state
                            full_response = ""
                            # Loop through each section in the order they were added
                            for section, msgs in st.session_state.agent_messages.items():
                                full_response += f"\n## {section}\n"
                                for m in msgs:
                                    full_response += m + "\n\n"
                            
                            # Process streaming token events (additional token text)
                            if data.get('event') == 'token':
                                token_data = data.get('data', '')
                                if token_data:
                                    full_response += token_data + "\n\n"
                            
                            # Capture sources if provided
                            if data.get('event') == 'usedTools':
                                for tool in data.get('data', []):
                                    if output := tool.get('toolOutput'):
                                        sources.add(output)
                            
                            # Update the placeholder with the latest full_response
                            placeholder.markdown(full_response + "▌")
                        
                        except json.JSONDecodeError:
                            # Skip this chunk if JSON decoding fails
                            continue

        # Append a sources section if any sources were captured
        if sources:
            full_response += "\n## 🔍 Data Sources\n"
            full_response += "\n".join(f"- {source}" for source in sources)
        
        # Final update of the placeholder and saving the assistant message to session state
        placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(f"Error: {str(e)}")
