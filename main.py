from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# .env ファイルから環境変数を読み込む
load_dotenv()

azure_endpoint = os.getenv("CHATBOT_AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("CHATBOT_AZURE_OPENAI_API_KEY")
deployment_name = "gpt-4o-mini"# Azure OpenAI Studio上で作成したデプロイ名と一致することを確認してください
api_version = "2025-01-01-preview"# 使用している API バージョン

# Azure OpenAI クライアントを作成
client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version=api_version 
)

# チャット履歴を保持するリスト
chat_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# ユーザーからのメッセージに対して応答を生成する関数
def get_response(message):
    chat_history.append({"role": "user", "content": message})
    response = client.chat.completions.create(
        model=deployment_name,
        messages=chat_history
    )
    assistant_message = response.choices[0].message.content.strip()
    chat_history.append({"role": "assistant", "content": assistant_message})
    return assistant_message

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("ChatGPT:", get_response(user_input))
