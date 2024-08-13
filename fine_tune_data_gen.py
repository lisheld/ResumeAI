# from data import bullet_dict
from vars import client
from helpers import Summary
from openai import OpenAI
import jsonlines



bullet_dict = {
    "MIT Heavy Ion Lab - Researcher": ["Evaluated and tested 20 cutting-edge machine-learning models on heavy-ion collision data", "Extracted trends in jets from over 1 million heavy-ion collisions using ROOT and C++","Used extracted jet trends to improve model architecture using CERN’s b-hive framework"]
}



def generate_full(bullet_points):
    messages = [
        {'role':'system', 'content': 'You are an expert in creating text summaries from bullet points on a resume. Given a list of bullet points that refer to what the user did for a specific role or project, return a paragraph summary in first person.'},
        {'role':'user','content': '\n'.join(bullet_points)}
    ]
    response = client.beta.chat.completions.parse(
        model='gpt-4o-mini',
        messages=messages,
        response_format=Summary,
    )
    message = response.choices[0].message
    if message.parsed:
        return message.parsed.summary
    else:
        return message.refusal

if __name__ == "__main__":
    finetuning_data = []

    for title, bullet_points in bullet_dict.items():
        finetuning_data.append(
            {
                "messages": [
                    {"role": "system", "content": "You are an expert in creating resume bullet points from a job description. Given a job title and description, return a list of bullet points that describe the responsibilities and qualifications for the role."},
                    {"role": "user", "content": generate_full(bullet_points)},
                    {"role": "assistant", "content": '\n'.join(bullet_points)}
                ]
            }
        )
    print('done generating')
    with jsonlines.open('bulletpointdata.jsonl', mode='w') as writer:
        for data in finetuning_data:
            writer.write(data)
    