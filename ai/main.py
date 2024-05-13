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


def generate_img(txt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=txt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    return response.data[0].url


