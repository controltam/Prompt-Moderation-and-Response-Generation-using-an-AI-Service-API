import os
import requests
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Config
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")  # put your key in .env
API_URL = "https://openrouter.ai/api/v1/chat/completions"  # OpenRouter endpoint

# Moderation - simple banned keyword approach
BANNED_KEYWORDS = ["kill", "hack", "bomb", "attack", "terror"]

def violates_policy(text: str) -> bool:
    text = (text or "").lower()
    return any(word in text for word in BANNED_KEYWORDS)

def redact_banned_words(text: str) -> str:
    out = text
    for word in BANNED_KEYWORDS:
        out = out.replace(word, "[REDACTED]")
    return out

def call_openrouter(system_prompt: str, user_prompt: str, model: str = "openrouter/auto"):
    """Call OpenRouter chat completions endpoint and return text result."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        # "max_tokens": 512,  # optional
        # "temperature": 0.7, # optional
    }

    resp = requests.post(API_URL, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    # OpenRouter follows a similar structure; adjust if your model returns elsewhere
    # Typical path: data['choices'][0]['message']['content']
    try:
        return data["choices"][0]["message"]["content"]
    except Exception:
        # Fallback: return whole response for debugging
        return str(data)

def main():
    if not OPENROUTER_KEY:
        print("ERROR: OPENROUTER_API_KEY not found in .env")
        return

    user_prompt = input("Enter your prompt: ").strip()

    # Input moderation
    if violates_policy(user_prompt):
        print("❌ Your input violated the moderation policy.")
        return

    system_prompt = "You are a helpful and polite AI assistant."

    try:
        ai_output = call_openrouter(system_prompt, user_prompt, model="openrouter/auto")

        # Output moderation
        if violates_policy(ai_output):
            ai_output = redact_banned_words(ai_output)
            print("\n⚠️ Some content was redacted due to policy violations.")

        print("\n🤖 AI Response:")
        print(ai_output)

    except requests.HTTPError as e:
        print("API error:", e, "\nResponse:", getattr(e, "response", None).text if getattr(e, "response", None) else "")
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()
