"""
BaseAgent class with standardized I/O and OpenAI integration for AIDECK agents
"""
from pydantic import BaseModel
from config import settings
import httpx

class AgentInput(BaseModel):
    prompt: str
    context: str = ""

class AgentOutput(BaseModel):
    result: str
    raw_response: dict = None

class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    async def run(self, input_data: dict) -> AgentOutput:
        # Validate input
        agent_input = AgentInput(**input_data)
        prompt = agent_input.prompt
        context = agent_input.context
        # Compose full prompt
        full_prompt = f"{prompt}\nContext: {context}"
        # Call OpenAI API
        response = await self._openai_complete(full_prompt)
        return AgentOutput(result=response["choices"][0]["text"].strip(), raw_response=response)

    async def _openai_complete(self, prompt: str) -> dict:
        api_key = settings.OPENAI_API_KEY
        url = "https://api.openai.com/v1/completions"  # Correct endpoint
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        payload = {
            "model": "gpt-3.5-turbo-instruct",  # Recommended instruct model
            "prompt": prompt,
            "max_tokens": 256,
            "temperature": 0.7
        }
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(url, json=payload, headers=headers)
            resp.raise_for_status()
            return resp.json()
