import openai
import logging

openai.api_key = "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"

def askChatGPT(messages):
    MODEL = "gpt-3.5-turbo"
    
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=1)
    return response['choices'][0]['message']['content']

def transcribe(file_name):
        audio_file = open(file_name, "rb")
        try:
            audio_file.read()  # 尝试读取文件内容
            logging.info("File is open...")  # 如果能够读取，则文件已经被打开
        except FileNotFoundError:
            logging.info("Warning: File is not open.")  # 如果文件未找到，则文件未被打开
            return 0
        audio_file.seek(0)  # f.read()读取文件指针会跑到文件的末端，如果再一次读取，读取的将是空格，所以要重定向文件指针
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        logging.info("Successfully converted...")
        return transcript.text


messages = [{"role": "system", "content": "假设你是一个杰出的英语老师，我会给你一段文章，你需要用尽可能简洁的语言对这段文章进行概述，用英语回答"}]
text = transcribe("audio_file.mp3")
# text = "hello"
print(text)
print()
d = {"role": "user", "content": text}
messages.append(d)
print(askChatGPT(messages))