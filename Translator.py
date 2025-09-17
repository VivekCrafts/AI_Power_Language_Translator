import os
from secreat_key import GOOGLE_API_KEY
os.environ['API_KEY']= GOOGLE_API_KEY
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0,google_api_key=GOOGLE_API_KEY)

# prompt template

prompt= PromptTemplate(
    input_variables=["word"],
    template = '''You are friendly language translator.Your job is to translate any given word,phrase, or sentence from any language into clear and simple English.
    Rules:
    1.You have to automatically detect the language of {word}.
    2.Keep the translation short,clear,and beginner-friendly.
    Output format should be:
    Original: "{word}"  \n
    Language Detected: <Language Name>  \n
    English Translation: <Short & Simple Translation>  \n
    Explanation: <One-line beginner-friendly explanation>'''
)

response =prompt.format(word='word')
response =llm.invoke(response)
print(response.content)