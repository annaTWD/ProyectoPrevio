from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

import os

# Meter la clave 

def extract_email_data(email_text):
    prompt_template = PromptTemplate(
        input_variables=["email_text"],
        template="""
        Extract the following details from the email text:
        - Sender
        - Receiver
        - Subject
        - Date
        - Body

        Email:
        {email_text}

        Please return the result in JSON format.
        """
    )

    llm = ChatOpenAI(model_name="gpt-3.5-turbo")



    chain = LLMChain(llm=llm, prompt=prompt_template)

    result = chain.run(email_text)
    
    return result
