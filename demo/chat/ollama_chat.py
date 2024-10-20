import json
import requests

model = "llama3.1:70b"

def chat(messages):
    r = requests.post(
        "http://36.137.165.26:11435/api/chat",
        json={"model": model, "messages": messages, "stream": True},

    )
    r.raise_for_status()
    output = ""
    for line in r.iter_lines():
        body = json.loads(line)
        if "error" in body:
            raise Exception(body["error"])
        if body.get("done") is False:
            message = body.get("message", "")
            content = message.get("content", "")
            output += content
            print(content, end="", flush=True)
        if body.get("done", False):
            message["content"] = output
            return message
def main():
    messages = []
    while True:
        user_input = input("Enter a prompt: ")
        if not user_input:
            exit()
        print()
        messages.append({"role": "user", "content": user_input})
        message = chat(messages)
        messages.append(message)
        print("\n\n")

if __name__ == "__main__":
    main()
