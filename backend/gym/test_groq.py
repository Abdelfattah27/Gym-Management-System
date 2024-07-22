import os

from groq import Groq

client = Groq(
    api_key='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',
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": """i will provide you a sentence that describe reason of being absent fromm the gym and you tell me if it acceptable or not 
                            if it acceptable just send me true and it not send me false without explanation
                            the sentence is : 'I was absent from the gym because i'm hungry . Is this acceptable?'
                            """ 
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)