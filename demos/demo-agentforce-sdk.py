import os
from agentforce.agents import Agentforce
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Agentforce client
client = Agentforce()

# Get credentials from environment variables
salesforce_org = os.getenv("SF_ORG")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
agent_id = "0XxKc0000005CBsKAM"

agentforce = Agentforce()
agentforce.authenticate(
    salesforce_org=salesforce_org,
    client_id=client_id,
    client_secret=client_secret
)

# Access the stored values
# print(agentforce.access_token)
print(agentforce.instance_url)

session = agentforce.start_session(agent_id=agent_id)
print(session.sessionId)
print(session.messages[0].message)

# Add messages
agentforce.add_message_text("Can you make a reservation for me?")
# agentforce.add_message_reply("Here are my details...")

# Send messages
response = agentforce.send_message(session_id=session.sessionId)

# Access response
print(response.messages[0].message)

# End the session
end_response = agentforce.end_session(session_id=session.sessionId)
print(end_response.messages[0].reason)