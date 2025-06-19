import asyncio

from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("Agent Example")


@fast.agent(
    instruction="Be a helpful assistant.",
    servers=["Demo"],  # server DID is defined in `fastagent.config.yaml`
)
async def main():
    async with fast.run() as agent:
        _response: str = await agent.with_resource(
            "What is in the following resource?",
            "greeting://world",
            "Demo",
        )

        # print(_response)
        await agent()  # interactive session


if __name__ == "__main__":
    asyncio.run(main())  # type: ignore
