from .rest.authenticate import authenticate
from .rest.start_session import start_session
from .rest.send_message import send_message
from .rest.end_session import end_session
from .data.session import SessionResponse
from .data.message import SendMessageResponse, MessageRequest
from .data.end_session import EndSessionResponse
from typing import Dict
from dataclasses import asdict

class Agentforce:
    """
    Main class for interacting with the Agentforce API
    """
    
    def __init__(self):
        self._access_token = None
        self._instance_url = None
        self._current_message: MessageRequest = None
        self._sequence_id = 1
        
    @property
    def access_token(self) -> str:
        """Get the current access token"""
        return self._access_token
        
    @property
    def instance_url(self) -> str:
        """Get the current instance URL"""
        return self._instance_url
        
    def authenticate(self, salesforce_org: str, client_id: str, client_secret: str) -> None:
        """
        Authenticate with Salesforce and store the access token and instance URL
        
        Args:
            salesforce_org: The Salesforce organization domain
            client_id: The client ID for authentication
            client_secret: The client secret for authentication
        """
        auth_response = authenticate(salesforce_org, client_id, client_secret)
        
        self._access_token = auth_response["access_token"]
        self._instance_url = auth_response["instance_url"]
        
    def start_session(self, agent_id: str) -> SessionResponse:
        """
        Start a new session with the Agentforce API
        
        Args:
            agent_id: The ID of the agent to start the session with
            
        Returns:
            SessionResponse: The session response object
        """
        if not self._access_token or not self._instance_url:
            raise ValueError("Please authenticate first before starting a session")
            
        return start_session(
            instance_url=self._instance_url,
            access_token=self._access_token,
            agent_id=agent_id
        )
        
    def add_message_text(self, text: str) -> None:
        """
        Add a text message to be sent
        
        Args:
            text: The text message to send
        """
        self._current_message = MessageRequest(
            type="Text",
            sequenceId=self._sequence_id,
            text=text
        )
        self._sequence_id += 1
        
    def add_message_reply(self, text: str) -> None:
        """
        Add a reply message to be sent
        
        Args:
            text: The reply message to send
        """
        self._current_message = MessageRequest(
            type="Reply",
            sequenceId=self._sequence_id,
            text=text
        )
        self._sequence_id += 1
        
    def send_message(self, session_id: str) -> SendMessageResponse:
        """
        Send the current message to the session
        
        Args:
            session_id: The ID of the session to send messages to
            
        Returns:
            SendMessageResponse: The response object
        """
        if not self._access_token or not self._instance_url:
            raise ValueError("Please authenticate first before sending messages")
            
        if not self._current_message:
            raise ValueError("No message to send. Please add a message first.")
            
        # Convert MessageRequest object to dictionary
        message_dict = asdict(self._current_message)
            
        response = send_message(
            instance_url=self._instance_url,
            access_token=self._access_token,
            session_id=session_id,
            message=message_dict
        )
        
        # Clear current message after sending
        self._current_message = None
        
        return response
        
    def end_session(self, session_id: str) -> EndSessionResponse:
        """
        End an existing Agentforce session
        
        Args:
            session_id: The ID of the session to end
            
        Returns:
            EndSessionResponse: The response object
        """
        if not self._access_token or not self._instance_url:
            raise ValueError("Please authenticate first before ending a session")
            
        return end_session(
            instance_url=self._instance_url,
            access_token=self._access_token,
            session_id=session_id
        )
