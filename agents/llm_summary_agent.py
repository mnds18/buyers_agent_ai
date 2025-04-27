# agents/llm_summary_agent.py

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Load API key (make sure to set it up via environment variables or dotenv)
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=openai_api_key, temperature=0.5)

summary_template = PromptTemplate(
    input_variables=["property_list"],
    template="You are an expert buyers agent. Summarize these properties for a client in simple, easy-to-understand language:\n\n{property_list}"
)

summary_chain = LLMChain(llm=llm, prompt=summary_template)

def summarize_properties(properties):
    property_text = "\n".join([prop["name"] for prop in properties])
    summary = summary_chain.run(property_list=property_text)
    return summary
