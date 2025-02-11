import openai

OPEN_AI_KEY = "*************"

class SearchLLM():
    def __init__(self,words):
        self.words = words


    def get(self):
        # 设置API密钥
        openai.api_key = OPEN_AI_KEY
        # 定义要与模型交互的消息
        messages = [
            {"role": "user", "content": self.words}
        ]
        assistant_reply = "OpenAI API 调用出错"
        try:
            # 调用OpenAI的Chat API
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=messages
            )
            # 提取助手的回复
            assistant_reply = response['choices'][0]['message']['content']
            assistant_reply

        except openai.error.OpenAIError as e:
            # 处理OpenAI API调用过程中可能出现的错误
            print(f"OpenAI API 调用出错: {e}") 
        
        return assistant_reply