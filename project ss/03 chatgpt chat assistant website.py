import openai
import gradio

openai.api_key= "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"

messages = [{"role": "system", "content":"Your are a programming expert in python,c,java"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "creation of your own chatGPT")

demo.launch(share=True)
