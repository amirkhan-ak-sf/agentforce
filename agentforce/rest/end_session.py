import requests
from ..constant.constants import END_SESSION_URL
from ..data.end_session import EndSessionResponse, EndSessionMessage
from ..data.message import Links, Link

def end_session(
    instance_url: str,
    access_token: str,
    session_id: str
) -> EndSessionResponse:
    """
    End an existing Agentforce session
    
    Args:
        instance_url: The Salesforce instance URL
        access_token: The access token for authentication
        session_id: The ID of the session to end
        
    Returns:
        EndSessionResponse: The response object
    """
    url = END_SESSION_URL.replace("{session-id}", session_id)
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "x-session-end-reason": "UserRequest"
    }
    
    response = requests.delete(url, headers=headers)
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
        EndSessionMessage(
            type=msg["type"],
            id=msg["id"],
            reason=msg["reason"],
            feedbackId=msg["feedbackId"]
        )
        for msg in data["messages"]
    ]
    
    return EndSessionResponse(
        messages=messages,
        _links=links
    ) 