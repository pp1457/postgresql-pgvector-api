import os
from dotenv import load_dotenv
from openai import AzureOpenAI

import json

def load_embeddings(file_path):
    try:
        with open(file_path, 'r') as file:
            embeddings = json.load(file)
    except FileNotFoundError:
        embeddings = {}  # If file does not exist, start with an empty dictionary
    return embeddings

def save_embeddings(embeddings, file_path):
    with open(file_path, 'w') as file:
        json.dump(embeddings, file)

def is_embedded(sentence, embeddings):
    return sentence in embeddings

def compute_embedding(doc, model_name):
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


def get_embedding(doc, model_name):

    file_path = 'data/embeddings.json'

    embeddings = load_embeddings(file_path)

    index = str((doc, model_name))


    # Check if the sentence is already embedded
    if is_embedded(index, embeddings):
        return embeddings[index]
    else:
        embedding_result = compute_embedding(doc, model_name)
        embeddings[index] = embedding_result

        save_embeddings(embeddings, file_path)

        print("Embedding saved.")

def main():
    get_embedding("Hi, I'm Paul", "text-embedding-3-small")

if __name__ == "__main__":
    main()
     
