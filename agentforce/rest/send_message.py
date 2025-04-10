import requests
from typing import Dict
from ..constant.constants import CONTINUE_SESSION_URL, VARIABLES_TEMPLATE
from ..data.message import MessagePayload, SendMessageResponse, Links, MessageResponse, Link

def send_message(
    instance_url: str,
    access_token: str,
    session_id: str,
    message: Dict
) -> SendMessageResponse:
    """
    Send a message to an existing Agentforce session
    
    Args:
        instance_url: The Salesforce instance URL
        access_token: The access token for authentication
        session_id: The ID of the session to send messages to
        message: The message object to send
        
    Returns:
        SendMessageResponse: The response object
    """
    url = CONTINUE_SESSION_URL.replace("{session-id}", session_id)
    
    payload = {
        "message": message,
        "variables": VARIABLES_TEMPLATE
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
        MessageResponse(
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
    
    return SendMessageResponse(
        messages=messages,
        _links=links
    ) 