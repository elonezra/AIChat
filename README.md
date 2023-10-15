# AIChat doc

## how to install

```
pip install git+https://github.com/elonezra/AIChat
```

## how to use

First, you need to import the class with:

```
from AIChat import ChatbotAgent
```

To use the module, make sure you have OpenAI installed.

1. To create an agent, use `chatbot = ChatbotAgent(character_details, memory_size)`.
    * `character_details` is a string of character details, see section 3.
    * `memory_size` is the size of the agent's memory, number of messages it save.

2. Call the function `chatbot.set_key("")` and give it the key.

3. (Optional) Create a character to talk with by using the functions:
    * `chatbot.generate_character()` (you can do this now in the constructor).
    * `chatbot.set_character(chracter_data)` to write your own characteristics.\
    It is better to use the following JSON format:

```json
{
    "ethnicity": "",
    "name": "",
    "age": 28,
    "sex": " ",
    "country": " ",
    "city": "",
    "hobbies": ["Reading", "Hiking", "Painting"],
    "appearance": {
        "height": "5\'7\\"",
        "hairColor": "Blonde",
        "eyeColor": "Blue"
    },
    "traits": ["Friendly", "Creative", "Empathetic"]
}
```

4. Call `chatbot.load_prompt_v1()` to load the instructions prompt.

5. To give a message and get a response, use `chatbot.message_to_response(message)`, which takes a string as the user's message and returns the character's response.

**example:**


```python
from AIChat import ChatbotAgent

# Create a chatbot agent with a memory size of 10 messages.
chatbot = ChatbotAgent(character_details="This is a character.", memory_size=10)

# Set the key.
chatbot.set_key("YOUR_API_KEY")

# Generate a character to talk with.
chatbot.generate_character()

# Load the instructions prompt.
chatbot.load_prompt_v1()

# Give a message and get a response.
response = chatbot.message_to_response("Hello, world!")

# Print the response.
print(response)
```
