import anthropic

API_KEY = "YOUR_API_KEY"

client = anthropic.Anthropic(api_key=API_KEY)

def get_financial_advice(summary):

    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=300,
        messages=[
            {
                "role":"user",
                "content":f"Give financial advice based on this data: {summary}"
            }
        ]
    )

    return message.content[0].text