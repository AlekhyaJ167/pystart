from groq import Groq

api_key = "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"

client = Groq(api_key=api_key)

while True:
    answer = input("What do you want? ")
    
    if answer == 'quit':
        break
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": answer
            }
        ],
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        stream=False,
        stop=None
    )
    
    print(completion.choices[0].message.content)
    