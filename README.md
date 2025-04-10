# Agentforce SDK

A Python SDK for interacting with the Agentforce API.

## Connected app
You must create a Connected App for your Agentforce Agent(s) to use it with this SDK. Here are the instructions: https://developer.salesforce.com/docs/einstein/genai/guide/agent-api-get-started.html


## Installation

```bash
pip install agentforce
```

## Usage

```python
from agentforce import Agentforce

# Initialize the client
agentforce = Agentforce()

# Authenticate
agentforce.authenticate(
    salesforce_org="your-salesforce-org",
    client_id="your-client-id",
    client_secret="your-client-secret"
)

# Start a session
session = agentforce.start_session(agent_id="your-agent-id")

# Send a message
agentforce.add_message_text("Hello, how can you help me?")
response = agentforce.send_message(session_id=session.sessionId)

# End the session
end_response = agentforce.end_session(session_id=session.sessionId)
```

## Features

- Authentication with Salesforce
- Session management (start/end)
- Message sending (text and reply)
- Type-safe response objects

## License

MIT 