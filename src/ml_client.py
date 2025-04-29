import os
import httpx
import jwt
from azure.identity import DefaultAzureCredential
from src.config import settings
from src.utils import get_logger

logger = get_logger("ml-client")

class MLClient:
    def __init__(self):
        self.endpoint = settings.AML_ENDPOINT
        self.auth_type = settings.AML_AUTH_TYPE.lower()
        self.api_key = settings.AML_API_KEY
        if self.auth_type == "msi":
            self.cred = DefaultAzureCredential()
        else:
            self.cred = None

    async def score(self, payload: dict) -> dict:
        headers = {"Content-Type": "application/json"}
        if self.auth_type == "key":
            headers["Authorization"] = f"Bearer {self.api_key}"
        else:
            token = (await self.cred.get_token("https://management.azure.com/.default")).token
            headers["Authorization"] = f"Bearer {token}"

        async with httpx.AsyncClient() as client:
            resp = await client.post(self.endpoint, json=payload, headers=headers)
            resp.raise_for_status()
            return resp.json()

ml_client = MLClient()