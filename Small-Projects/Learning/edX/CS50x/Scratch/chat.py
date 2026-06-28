from openai import OpenAI

client = OpenAI()

user_prompt = input("Prompt: ")
system_prompt = "Limit your answer to one sentence. Pretned you're a cat."

response = client.responses.create(
    input=prompt,
    model="gpt-5"
)

print(response.output_text)