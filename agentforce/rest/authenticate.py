import requests
from ..constant.constants import OAUTH_TOKEN_URL, CONTENT_TYPE_FORM, GRANT_TYPE

def authenticate(salesforce_domain: str, client_id: str, client_secret: str) -> dict:
    """
    Authenticate with Salesforce and obtain access token
    
    Args:
        salesforce_domain: The Salesforce domain/org
        client_id: The client ID for authentication
        client_secret: The client secret for authentication
        
    Returns:
        dict: Authentication response containing access token and other details
    """
    url = OAUTH_TOKEN_URL.format(salesforceDomain=salesforce_domain)
    
    payload = {
        "grant_type": GRANT_TYPE,
        "client_id": client_id,
        "client_secret": client_secret
    }
    
    headers = {
        "Content-Type": CONTENT_TYPE_FORM
    }
    
    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()
    
    return response.json() 