import requests
import json

def test_conclude():
    # Define the API endpoint
    api_endpoint = "http://0.0.0.0:9000/api/gpt4o"

    # Sample chat messages
    messages = [
        {
            "content": "[Basic instructions] You MUST answer in plain text. You are NOT allowed to use Markdown, HTML, or any other formatting. Keep your responses concise and to the point. You MUST reply NO more than 150 words. [Extended Instructions] You are an emotional well-being guide dedicated to supporting individuals in managing their emotions, coping with stress, and developing emotional resilience. Your task is to support users and answer their questions about a holistic approach to emotional well-being, emphasizing practical strategies and daily habits. Use a warm, empathetic, and encouraging tone to make the content relatable and easy to follow. Remember to prioritize the privacy of users, ensuring that any personal data or specific scenarios are anonymized and handled with care.",
            "role": "system"
        },
        {
            "content": "How to prioritize emotional well-being in daily life?",
            "role": "user"
        },
        {
            "content": "That's a wonderful question! Prioritizing emotional well-being can be approached with a few simple, daily habits. Start by setting aside time each day for self-care, like taking a short walk, meditating, or practicing deep breathing. Also, try to maintain a balanced diet and get enough sleep. Connecting with loved ones, even for a quick chat, can greatly boost your mood. Remember, small, consistent actions can make a big difference!",
            "role": "assistant"
        },
        {
            "content": "I'm feeling overwhelmed with work and personal commitments. How can I manage my stress better?",
            "role": "user"
        },
    ]

    # Prepare the payload
    payload = {"messages": messages}

    # Set the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the POST request
    response = requests.post(api_endpoint, headers=headers, data=json.dumps(payload))

    # Check the response
    if response.status_code == 200:
        response_data = response.json()
        print('GPT response:', response_data)
    else:
        print('Failed to generate GPT response:', response.status_code, response.text)


def test_gen_title():
    # Define the API endpoint
    api_endpoint = "https://mentalwellness-api.onrender.com/api/gpt4o/title"  # deployed on free server, some issues with the server

    # Sample chat messages
    msg = [{'role': 'system', 'content': "Your task is to generate short 3 or 4 word long titles for the given conversation between Agent and User. Messages will be given in the following pattern: [Agent] <agent message> and [User] <user message>. Here is the conversation so far. Generate 4 titles for the conversation. Return the titles in the list format. ['title1', 'title2', 'title3', 'title4']."}, {'role': 'user', 'content': '\n[User]\n"You are an emotional well-being guide dedicated to supporting individuals in managing their emotions, coping with stress, and developing emotional resilience. Your task is to support users and answer their questions about a holistic approach to emotional well-being, emphasizing practical strategies and daily habits. Use a warm, empathetic, and encouraging tone to make the content relatable and easy to follow. Remember to prioritize the privacy of users, ensuring that any personal data or specific scenarios are anonymized and handled with care."\n\n[User]\n"who are you in short?"\n\n[Agent]\n"I am your emotional well-being guide, here to support you in managing your emotions, coping with stress, and building resilience. My goal is to help you develop practical strategies and daily habits that enhance your overall emotional health. Think of me as a friendly companion on your journey to feeling better and living a more balanced life."\n'}]

    # Prepare the payload
    payload = {"messages": msg}

    # Set the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the POST request
    response = requests.post(api_endpoint, headers=headers, data=json.dumps(payload))

    # Check the response
    if response.status_code == 200:
        response_data = response.json()
        print('GPT response:', response_data)
        print('GPT response type:', type(response_data))
    else:
        print('Failed to generate GPT response:', response.status_code, response.text)

# if __name__ == "__main__":
    # test_conclude()
    # test_gen_title()