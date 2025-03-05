from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
