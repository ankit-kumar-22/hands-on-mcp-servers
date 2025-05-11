import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langchain_ibm import ChatWatsonx
#Using Ollama
model = ChatOllama(model="llama3.2:1b")  # Use a model available via Ollama
#Using WatsonX
parameters = {
    "decoding_method": "sample",
    "max_new_tokens": 4000,
    "min_new_tokens": 1,
    "temperature": 1,
    "top_k": 50,
    "top_p": 1,
}

# watsonx_llm = ChatWatsonx(
#     model_id = "ibm/granite-3-8b-instruct",
#     url="",
#     project_id="",
#     apikey="",
#     params=parameters,
# )

# prompt = ChatPromptTemplate.from_messages([
#     SystemMessage(content="You are a helpful assistant. Always share the exact output from any tools."),
#     HumanMessage(content="{input}")
# ])

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],  # Update this path
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            #Use "watsonx_llm" instead of "model" to use WatsonX
            agent = create_react_agent(model, tools)
            # Try out the tools via natural language
            msg1 = {"messages": "What is the total no of shampoo available in our inventory?"}
            # msg2 = {"messages": "My age?"}
            res1 = await agent.ainvoke(msg1)
            print("Response - >:", res1)
            for m in res1['messages']:
                m.pretty_print()
            # res2 = await agent.ainvoke(msg2)
            # # print("Word count result:", res2)
            # for m in res2['messages']:
            #     m.pretty_print()
if __name__ == "__main__":
    asyncio.run(main())