# Standard libraries
import asyncio
import os

# Third-party libraries
import dotenv

# Generated libraries
import groq_client
from groq_client.api.default import get_models
from groq_client.models.models import Models


async def main():
    dotenv.load_dotenv()

    client = groq_client.AuthenticatedClient(
        base_url="https://api.groq.com/openai/v1",
        token=os.environ.get("GROQ_API_KEY"),
    )

    async with client as client:
        models: Models = await get_models.asyncio(client=client)
        for model in models.data:
            print(model.id)


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
