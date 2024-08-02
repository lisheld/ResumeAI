from data import data
from vars import openai_key
from openai import OpenAI

client = OpenAI(api_key=openai_key)
def generate_full(*args):
    bullet_points = args
    messages = [
        {'role':'system','content': "You are an expert in creating text summaries from bullet points on a resume. Given a list of bullet points that refer to what the user did for a specific role or project, return a 5 sentence summary in first person."},
        {'role':'user','content': '\n'.join(bullet_points)}
    ]
    response = client.completions.create(
        model='gpt-4o-mini',
        messages=messages
    )
    return response.choices[0].message.content

