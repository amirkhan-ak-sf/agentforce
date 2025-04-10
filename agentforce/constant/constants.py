"""
Constants used throughout the Agentforce SDK.
"""

# Base URL for the Agentforce API
BASE_URL = "https://api.salesforce.com/einstein/ai-agent/v1"

# Base URLs
OAUTH_TOKEN_URL = "https://{salesforceDomain}/services/oauth2/token"
START_SESSION_URL = f"{BASE_URL}/agents/{{agentId}}/sessions"
CONTINUE_SESSION_URL = f"{BASE_URL}/sessions/{{session-id}}/messages"
END_SESSION_URL = f"{BASE_URL}/sessions/{{session-id}}"

# OAuth Constants
GRANT_TYPE = "client_credentials"
CONTENT_TYPE_FORM = "application/x-www-form-urlencoded"
CONTENT_TYPE_JSON = "application/json"

# Default Values
DEFAULT_LOCALE = "en_US"
TIMEZONE = "America/Los_Angeles"
BY_PASS_USER= True
VARS_TYPE = "Text"
VARS_NAME = "$Context.EndUserLanguage"
FEATURE_SUPPORT = "featureSupport"

# Default headers for API requests
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Payload Templates
VARIABLES_TEMPLATE = [
    {
      "name": VARS_NAME,
      "type": VARS_TYPE,
      "value": DEFAULT_LOCALE
    }
  ]

