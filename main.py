from helpers import Conversation, classify, BulletPoints, ResumeSections

field = classify('professional field', input('What field are you applying in?'))
position = classify('job position', input("What position are you applying for?"))

section_builder = Conversation("You are an expert in identifying the best sections to include on a resume. Given a professional field and a job position, please give the 5 best sections (excluding contact information) to include on a resume.")
section_builder.add_message('user', f'professional field: {field}, job position: {position}')
section_builder.respond(output_type=ResumeSections)
sections = section_builder.messages()[-1]['content'].sections

print(f"I suggest using the sections {', '.join(sections)} on your resume.")