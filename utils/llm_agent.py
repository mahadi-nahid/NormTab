import os
import tiktoken
from openai import OpenAI
# ---------------------------------------------------------------
# API_KEY = ''


os.environ['OPENAI_API_KEY'] = API_KEY
# openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

client = OpenAI()

# model="gpt-3.5-turbo-0125"
# model="gpt-4-turbo"

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0.7, n=1, max_tokens = 6000):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        n=n,
        stream=False,
        max_tokens=max_tokens,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n\n\n"]
    )
    return response.choices[0].message.content



import os
import google.generativeai as genai

os.environ["GOOGLE_API_KEY"] = ""

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])



def get_completion_gemmini(prompt, temperature=0.7, max_tokens = 8000):
    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
    generation_config = {
        "temperature": temperature,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": max_tokens,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
        history=[
        ]
    )

    response = chat_session.send_message(prompt)
    return  response.text


