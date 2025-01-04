from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from typing import Any, Dict
import requests

def send_request(url: str) -> str:
    """Send a GET request to a URL and return the response content.
    
    Args:
        url: The URL to send the request to
        
    Returns:
        The response content as a string
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: Failed to fetch content: {str(e)}"

def write_to_file(file_path: str, content: str) -> str:
    """Write content to a file.
    
    Args:
        file_path: Path to the file to write to
        content: Content to write to the file
        
    Returns:
        A message indicating success or failure
    """
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return f"Content written to {file_path} successfully"
    except Exception as e:
        return f"Failed to write to file: {str(e)}"


web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[send_request, write_to_file],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Get the visible content from https://example.com and write it to a file named output.txt", stream=True)
