from vars import client

client.fine_tuning.jobs.create(
  training_file="bulletpointdata.jsonl", 
  model="gpt-4o-mini"
)