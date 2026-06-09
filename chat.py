import requests

response = requests.post(
    "https://api.inceptionlabs.ai/v1/chat/completions",
    headers={
        "Authorization": "Bearer sk_8f77ee4d98563e4b167d529d84e9e63d",
        "Content-Type": "application/json"
    },
    json={
        "model": "mercury-2",
        "messages": [
            {
                "role": "system",
                "content": "You are an expert in Artificial Intelligence and employment trends. Provide detailed, balanced, and informative answers."
            },
            {
                "role": "user",
                "content": "Discuss how Artificial Intelligence (AI) is causing unemployment among youth. Explain its impact, advantages, disadvantages, and possible solutions."
            },
            {
                "role": "assistant",
                "content": "AI can automate repetitive tasks, reducing the need for human workers in some industries. However, it also creates new job opportunities in technology, data science, and AI development."
            }
        ]
    }
)

print(response.json())