import uuid
import requests
from typing import Dict
from ..constant.constants import START_SESSION_URL, VARIABLES_TEMPLATE, TIMEZONE, FEATURE_SUPPORT
from ..data.session import SessionResponse, Links, Message, Link

def start_session(instance_url: str, access_token: str, agent_id: str) -> SessionResponse:
    """
    Start a new session with the Agentforce Agent by its Id
    
    Args:
        instance_url: The Salesforce instance URL
        access_token: The access token for authentication
        agent_id: The ID of the agent to start the session with
        
    Returns:
        SessionResponse: The session response object
    """
    url = START_SESSION_URL.format(agentId=agent_id)
    
    payload = {
        "externalSessionKey": str(uuid.uuid4()),
        "instanceConfig": {
            "endpoint": instance_url
        },
        "tz": TIMEZONE,
        "variables": VARIABLES_TEMPLATE,
        "featureSupport": FEATURE_SUPPORT,
        "streamingCapabilities": {
            "chunkTypes": ["Text"]
        },
        "bypassUser": "true"
    }
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    
    # Convert response to data classes
    links = Links(
        self=Link(href=data["_links"]["self"]),
        messages=Link(href=data["_links"]["messages"]["href"]),
        messagesStream=Link(href=data["_links"]["messagesStream"]["href"]),
        session=Link(href=data["_links"]["session"]["href"]),
        end=Link(href=data["_links"]["end"]["href"])
    )
    
    messages = [
        Message(
            type=msg["type"],
            id=msg["id"],
            feedbackId=msg["feedbackId"],
            planId=msg["planId"],
            isContentSafe=msg["isContentSafe"],
            message=msg["message"],
            result=msg["result"],
            citedReferences=msg["citedReferences"]
        )
        for msg in data["messages"]
    ]
    
    return SessionResponse(
        sessionId=data["sessionId"],
        _links=links,
        messages=messages
    ) 