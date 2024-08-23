import os
from dotenv import load_dotenv
from openai import AzureOpenAI

def get_embedding(doc, model_name):
    load_dotenv()
     
    client = AzureOpenAI(
      api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
      api_version = "2024-02-01",
      azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT") 
    )

    response = client.embeddings.create(
        input = doc,
        model= model_name
    )

    return response.data[0].embedding
