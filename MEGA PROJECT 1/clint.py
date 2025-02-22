from openai import OpenAI

client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a vertual assistant. name subho"},
        {
            "role": "user",
            "content": "what is coding."
        }
    ]
)
print(completion.choices[0].message.content)
