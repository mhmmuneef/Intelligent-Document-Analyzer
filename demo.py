from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv('https://int01.cognitiveservices.azure.com/')
key = os.getenv('d5f0951d1ca849c58b5bf5fa23d3cdd2Y')

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

try:
    # Test with a simple document
    documents = ["Hello world! This is a test document."]
    response = text_analytics_client.recognize_entities(documents)

    for entity in response:
        if not entity.is_error:
            print(f"Entity: {entity.text}, Category: {entity.category}, Confidence Score: {entity.confidence_score}")
        else:
            print(f"Error: {entity.error}")

except Exception as e:
    print(f"An error occurred: {e}")
