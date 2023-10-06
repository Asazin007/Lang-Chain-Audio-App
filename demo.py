import assemblyai as aai
from langchain.document_loaders import AssemblyAIAudioTranscriptLoader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import os
# replace with your API token
# aai.settings.api_key = f"0ea299f478b542ebab612b83c7afcfda"
# Set your OpenAI API key
# os.environ["OPENAI_API_KEY"] = "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"
import json

# Load API keys from the configuration file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

openai_api_key = config.get('openai_api_key')
assemblyai_api_key = config.get('assemblyai_api_key')

# Check if both keys are present
if not openai_api_key or not assemblyai_api_key:
    raise ValueError("API keys not found in the configuration file.")

# replace with your API token
aai.settings.api_key =assemblyai_api_key 
# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_api_key


# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
loader = AssemblyAIAudioTranscriptLoader(FILE_URL)
docs = loader.load()
llm = OpenAI()
qa_chain = load_qa_chain(llm, chain_type="stuff")
answer = qa_chain.run(input_documents=docs,question="Where did the wildfire start?")
print(answer)