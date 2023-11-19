import openai

# replace with your api key
openai.api_key = "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"

def generate_text_with_openai(user_prompt):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # you can replace this with your preferred model
        messages=[{"role": "user", "content": user_prompt}],
    )
    return completion.choices[0].message.content

prompt = "Generate 2 catchy youtube titles about [email marketing tricks]"

response = generate_text_with_openai(prompt)

print(response)