# Agentforce Demo Scripts

This directory contains demo scripts showing how to use the `salesforce-agentforce` package.

## Basic Usage Demo

The `basic_usage.py` script demonstrates the basic functionality of the Agentforce SDK:

1. Authentication with Salesforce
2. Starting a session with an agent
3. Sending messages to the agent
4. Ending the session

### Prerequisites

Before running the demo, you need to set up the following environment variables:

```bash
export SALESFORCE_ORG="your-org.my.salesforce.com"
export SALESFORCE_CLIENT_ID="your-client-id"
export SALESFORCE_CLIENT_SECRET="your-client-secret"
export AGENTFORCE_AGENT_ID="your-agent-id"
```

### Running the Demo

1. Make sure you have the `salesforce-agentforce` package installed:
   ```bash
   pip install salesforce-agentforce
   ```

2. Run the demo script:
   ```bash
   python basic_usage.py
   ```

### Expected Output

The script will output the progress of each operation:

```
Authenticating with Salesforce...
Authentication successful!

Starting a new session...
Session started with ID: abc123...

Sending a text message...
Message sent. Response: SendMessageResponse(...)

Sending a reply message...
Reply sent. Response: SendMessageResponse(...)

Ending the session...
Session ended. Response: EndSessionResponse(...)
```

## Notes

- Make sure your Salesforce credentials have the necessary permissions to access Agentforce
- The agent ID should be a valid Agentforce agent ID in your Salesforce org
- The script uses a try-finally block to ensure the session is always ended, even if an error occurs 