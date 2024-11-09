# Import libraries
import nltk
import os
import nest_asyncio
from IPython.display import HTML, display
from llama_index.readers.file import UnstructuredReader
from pathlib import Path
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import SubQuestionQueryEngine
from llama_index.agent.openai import OpenAIAgent
import chainlit as cl
from dotenv import load_dotenv
from typing import Optional


# Download necessary nltk libraries
# nltk.download('all')

# Load environment variables from the .env file
load_dotenv(dotenv_path="./.env")

# Set OpenAI API Key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = openai_api_key

# Apply async settings for notebook
nest_asyncio.apply()


years = [2023, 2022, 2021, 2020]

# Load documents for each year
loader = UnstructuredReader()
doc_set = {}
all_docs = []
for year in years:
    year_docs = loader.load_data(
        file=Path(f"./data1/AAPL/AAPL{year}.htm"), split_documents=False
    )
    for d in year_docs:
        d.metadata = {"year": year}
    doc_set[year] = year_docs
    all_docs.extend(year_docs)

# Initialize settings for embedding and OpenAI model
Settings.chunk_size = 512
Settings.chunk_overlap = 64
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# Create indices for each year
index_set = {}
for year in years:
    storage_context = StorageContext.from_defaults()
    cur_index = VectorStoreIndex.from_documents(
        doc_set[year],
        storage_context=storage_context,
    )
    index_set[year] = cur_index
    storage_context.persist(persist_dir=f"./storage/{year}")

# Load saved indices from disk
index_set = {}
for year in years:
    storage_context = StorageContext.from_defaults(persist_dir=f"./storage/{year}")
    cur_index = load_index_from_storage(storage_context)
    index_set[year] = cur_index

# Create individual query engine tools for each year
individual_query_engine_tools = [
    QueryEngineTool(
        query_engine=index_set[year].as_query_engine(),
        metadata=ToolMetadata(
            name=f"vector_index_{year}",
            description=f"useful for answering queries about the {year} SEC 10-K for Apple",
        ),
    )
    for year in years
]

# Combine tools into a sub-question query engine
query_engine = SubQuestionQueryEngine.from_defaults(
    query_engine_tools=individual_query_engine_tools,
)

# Create an OpenAI Agent using the combined query tools
query_engine_tool = QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(
        name="sub_question_query_engine",
        description="Analyzes multiple SEC 10-K documents for Apple",
    ),
)

tools = individual_query_engine_tools + [query_engine_tool]

# Initialize the OpenAI Agent
agent = OpenAIAgent.from_tools(tools, verbose=True)

# Chainlit Authentication
@cl.password_auth_callback
def auth_callback(username: str, password: str):
    if (username, password) == ("admin", "admin"):
        return cl.User(
            identifier="admin", metadata={"role": "admin", "provider": "credentials"}
        )
    else:
        return None

@cl.on_chat_start
async def start():
    await cl.Message(
        author="Assistant",
        content="Hello! I'm here to assist you. What would you like to know?"
    ).send()

# Chainlit App Logic
@cl.on_message
async def main(message: str):
    response = agent.chat(message.content)
    await cl.Message(content=str(response)).send()



# Run the Chainlit application on localhost
if __name__ == "_main_":
    cl.run(port=8000, headless=False)
