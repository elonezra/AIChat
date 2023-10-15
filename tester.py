from AIChat import ChatbotAgent  # Replace 'chatbot_agent_module' with the actual name of the module
# import AIChat
# Example: Create a chatbot with specific characteristics and a memory size of 6
character_details = """{
    "name": "John",
    "age": 30,
    "sex": "Male",
    "country": "USA",
    "city": "New York",
    "hobbies": "Reading, Traveling",
    "appearance": "Tall, with brown hair",
    "traits": "Friendly, outgoing"
}"""

character_details1 = """{
    "name": "Samir",
    "age": 30,
    "sex": "Male",
    "country": "USA",
    "city": "New York",
    "hobbies": "Reading, Traveling",
    "appearance": "Tall, with brown hair",
    "traits": "Friendly, outgoing"
}"""
memory_size = 6
chatbot = ChatbotAgent(character_details1, memory_size)
chatbot2 = ChatbotAgent(character_details, memory_size)
api_key = "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"
# AIChat.set_key(api_key)
# AIChat.set_character(character_details)
# AIChat.load_prompt_v1()
# user_message = "my name is Danny    "
# print(AIChat.message_to_response(user_message))

chatbot.set_api_key(api_key)
# chatbot.set_character(character_details)
chatbot.load_prompt_v1()

user_message = "my name is Danny"
response = chatbot.message_to_response(user_message)
print("Character's Response:", response)

user_message = "i want to check if you are aware, do you remember what is my name?"
response = chatbot.message_to_response(user_message)
print("Character's Response:", response)
chatbot.print_prompt()

print("\n===================================\n")

chatbot2.set_api_key(api_key)
# chatbot2.set_character(character_details)
chatbot2.load_prompt_v1()

user_message = "my name is Elon"
response = chatbot2.message_to_response(user_message)
print("Character's Response:", response)

user_message = "i want to check if you are aware, do you remember what is my name?"
response = chatbot2.message_to_response(user_message)
print("Character's Response:", response)
chatbot2.print_prompt()