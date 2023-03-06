import os

from langchain.llms import OpenAI



def build_prompt(text):
    prompt = "We have a commercial real estate brochure with the following text:\n\n"
    prompt += text

    prompt += "\n\n Create a JSON object that provides the following pieces of data about the listing: \n"
    prompt += "title (string) - a catchy title \n"
    prompt += "address (string) \n"
    prompt += "price (integer) \n"
    prompt += "square footage (integer) \n"
    prompt += "occupancy (integer) \n"
    prompt += "class (string) - the class of the building \n"
    prompt += "description (string) - a brief summary of the listing \n"
    prompt += "contact_name (string) - the name of the person to contact \n"
    prompt += "contact_email (string) - the email of the person to contact \n"
    prompt += "contact_phone (string) - the phone number of the person to contact \n"
    prompt += "contact_company (string) - the company of the person to contact \n"

    prompt += "\n If any data is missing or unclear, put null in the JSON object."

    return prompt


def process_text(text):
    prompt = build_prompt(text)

    llm = OpenAI(model_name="gpt-3.5-turbo")

    return llm(prompt)

def process_description(text, features):
    prompt = build_description_prompt(text, features)

    llm = OpenAI(model_name="gpt-3.5-turbo")

    return llm(prompt)

def build_description_prompt(text, features):
    prompt = '### We have a real estate listing with the following description:\n'

    for feature in features:
        prompt += f'Based on this listing, does the property have the feature titled {feature}?\n'

    prompt += 'Respond with a JSON object containing the {Feature Title} as the key, and {True / False} as the value.\n'
    prompt += '###'

    return prompt
