from anthropic import AnthropicVertex # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()

project_id = os.getenv("PROJECT_ID")
region = os.getenv("REGION", "global")

client = AnthropicVertex(region=region, project_id=project_id)
message = client.messages.create(
 max_tokens=1024,
 messages=[{"role": "user", "content": "Hello! Can you help me?"}],
 model="claude-opus-4-6"
)

print(message.content[0].text) # type: ignore
