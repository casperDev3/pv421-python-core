from openai import OpenAI

client = OpenAI(
    api_key=""
)


async def test_send_prompt(txt):
    return client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ти повинен спілкуватись тільки українською мовою"},
            {"role": "user", "content": f"{txt}"},
        ]
    )
