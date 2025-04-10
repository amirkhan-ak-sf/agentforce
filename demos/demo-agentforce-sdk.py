from agentforce.agents import Agentforce

agentforce = Agentforce()
agentforce.authenticate(
    salesforce_org="storm-f10cefd8484239.my.salesforce.com",
    client_id="3MVG9iHJIKsgQcWIBObb7wP9WrrYRH9DmV5WJECvsl8HtiofTx9YLIYbAzFgz62EvHKcJk_URvnvBb9ac6uw2",
    client_secret="E1584074AC9B438DDBD4789F5BC9B133362D5AFE1963BED96E7CF1CB8BD680DB"
)

# Access the stored values
# print(agentforce.access_token)
print(agentforce.instance_url)

session = agentforce.start_session(agent_id="0XxKc0000005CBsKAM")
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