from aichat import aichat
import os

my_key = os.environ['MY_KEY']

chatbot = aichat.ChatbotAgent( memory_size=10)

# Set the key.
chatbot.set_api_key(my_key)
# print(chatbot.api_key)
chatbot.set_character("")
chatbot.load_prompt_from_file("character_prompt.txt")
response = chatbot.message_to_response("what is the color of the sky?")
print(response)