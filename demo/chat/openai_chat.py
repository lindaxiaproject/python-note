from openai import OpenAI


client = OpenAI(api_key='a',base_url='http://36.137.165.26:11435/v1')

if __name__ == '__main__':
  completion = client.chat.completions.create(
    model="llama3.1:70b",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "请使用中文,帮我介绍一下北京!"}
    ],
      stream=False
  )
  print(completion.choices[0].message.content)