from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_outreach(name, problem):

    prompt = f"""
Write a short supportive outreach message.

Person: {name}
Problem: {problem}

Offer a free 20 minute life coaching clarity call.
Keep under 80 words.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
