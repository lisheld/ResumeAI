from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
openai_key = os.getenv('openai')

finetuned = ''
standard = 'gpt-4o-mini'

client = OpenAI(api_key=openai_key)
