from vars import client, standard
import json
from pydantic import BaseModel

class Conversation:
    def __init__(self, opening_prompt = "You are a helpful assistant."):  
        self.conversation_history = [{"role":"system", "content":opening_prompt}]

    def add_message(self, role, content):
        self.conversation_history.append({"role": role, "content": content})
    
    def respond(self, model=standard, output_type='text'):
        if isinstance(output_type, type(str)):
            print('using pydantic model')
            response = client.beta.chat.completions.parse(
                model=model,
                messages=self.conversation_history,
                response_format=output_type
            )
            out = response.choices[0].message.parsed
        else:
            print('using standard model')
            response = client.chat.completions.create(
                model=model,
                messages=self.conversation_history,
                response_format={"type": output_type}
            )
            out = response.choices[0].message.content
        self.add_message("assistant",out)
    
    def messages(self):
        return self.conversation_history

class Summary(BaseModel):
    summary: str

class BulletPoints(BaseModel):
    bullet_points: list[str]

class ResumeSections(BaseModel):
    sections: list[str]

def classify(item, input):
    main = Conversation(f"You are an expert in identifying the {item} the user is talking about in their response. Return the output as a JSON object with one entry of the form 'field': 'example_field' or 'error':'example_error' if the user is not talking about a {item}.")
    main.add_message('user', input)
    main.respond(output_type='json_object')
    out = json.loads(main.conversation_history[-1]['content'])
    if 'error' in out:
        print(out['error'])
    return list(out.values())[0]

