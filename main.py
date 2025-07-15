import requests
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# === Configuration ===
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "a44cbd0a-ec9a-4168-964a-fbf2c217c9f7"  # Your Langflow App ID
FLOW_ID = "8f0b8449-1e7f-4af7-a2db-9d63c6e0499a"       # Your Flow ID
ENDPOINT = FLOW_ID  # The endpoint is your Flow ID

APPLICATION_TOKEN = os.environ.get("APP_TOKEN")  # Make sure to set this in your .env file

def run_flow(message: str) -> dict:
    """
    Sends a POST request to the Langflow API with the user's message.
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an error for HTTP issues
    return response.json()

def main():
    st.title("📚 Onboarding Support Chatbot")
    st.markdown("Ask anything about your organization, team, or projects!")

    message = st.text_area("Your Question", placeholder="e.g., What is NovaIQ?")
    
    if st.button("Ask"):
        if not message.strip():
            st.error("Please enter a message")
            return

        try:
            with st.spinner("Thinking..."):
                response = run_flow(message)

            # Parse chatbot reply
            reply = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(f"**Bot:** {reply}")
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
