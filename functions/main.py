# main.py

# The Cloud Functions for Firebase SDK to create Cloud Functions and set up triggers.
from firebase_functions import https_fn
import json

# The Firebase Admin SDK to access Cloud Firestore.
from firebase_admin import initialize_app
import google.cloud.firestore
from gpt import gen_title, conclude

# Initialize Firebase app
initialize_app()

# Firebase function for GPT-4o to conclude messages
@https_fn.on_request()
def gpt_conclude(req: https_fn.Request) -> https_fn.Response:
    """Endpoint to conclude messages using GPT-4o."""
    request_body = req.get_json(silent=True)
    if not request_body or "messages" not in request_body:
        return https_fn.Response("Invalid request body", status=400)
    
    messages = request_body.get("messages", "")
    response_text = conclude(messages)
    
    return https_fn.Response(response_text, status=200)

# Firebase function for GPT-4o to generate titles
@https_fn.on_request()
def gpt_generate_title(req: https_fn.Request) -> https_fn.Response:
    """Endpoint to generate titles using GPT-4o."""
    request_body = req.get_json(silent=True)
    if not request_body or "messages" not in request_body:
        return https_fn.Response("Invalid request body", status=400)
    
    messages = request_body.get("messages", "")
    titles_list = gen_title(messages)
    
    return https_fn.Response(json.dumps(titles_list), status=200)

