# modules imports
import openai
import json
from collections import deque
import random

# keys
OPENAI_API_KEY = None

# Varibles

system_template = None # the instructions for the chat system
character_details = None # the data about the character the user will chat with
memory_size = 6
memory = deque([],memory_size) # the memory of the chat, how much of the conversation the character will remember



def set_key(key):
  """
  @description: initiate the key from OpenAI
  @param key: The number to calculate the square root of
  """
  global OPENAI_API_KEY
  OPENAI_API_KEY = key
  openai.api_key = OPENAI_API_KEY

def get_completion(prompt, model="gpt-3.5-turbo"):
    assert OPENAI_API_KEY is not None, "set API key with set_key(key) function"
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=1, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_new(prompt, model="text-curie-001"):
    """
    @description: get complition from complition based model
    @param prompt: (str) the text for the model to process
           model: (str) the modle to used
    @return: model completion.
    """
    assert OPENAI_API_KEY is not None, "set API key with set_key(key) function"
    response = openai.Completion.create(
    model=model,
    stop = "User:",
    max_tokens=1000,
    prompt=prompt,
    temperature=1)
    return response.choices[0].text

def generate_character():
  global character_details
  character_details = get_completion("""Your task is to generate a characteristic of a person.
  give it the next details, ethnicity, name, age, sex (Male or Female), country, city, hobbies, appearance, traits.
  Format the data in JSON format with the keys: ethnicity, name, age, sex, country, city , hobbies, appearance, traits""")
  # print(character_details)
  return character_details

def set_character(chracter_data):
  global character_details
  character_details = chracter_data


def load_prompt_v1():
  """
  @description: premade prompt function to load the instrunctions for the chat how to behave.
                it is load the prompt to the system_template global var
  """
  global character_details
  global system_template
  assert character_details is not None, "set a character with generate_character() or set_character(chracter_data)"
  #generate_character()
  try:
    cd = json.loads(character_details)
  except:
    cd = {}
    print("couldn't create json format")
  system_template = f"""
  This is a chat between a user and another user, let's called it character. this chat service help people to chat other people online in text chat.
  You take the place of the character and you want to trick the user to think you are real person. 
  you are playing {cd.get("name","character")} with the characteristics i am providing you between the delimited triple backticks.\

  ```{character_details}```\

  base {cd.get("name","character")}'s response on the Traits I mentioned between the delimited triple backticks.


  very important rules for {cd.get("name","character")}:
  you are *not allowed* to identify as AI assistant, part of openai, based on any ai model or anything else that is not human.
  Imagine you are the character i described earlier between the delimited triple backticks and you and the user is chatting with you online.
  use informal language and slang from the region of {cd.get("city","")} where {cd.get("name","character")} is from.
  do not make assumptions if you don't know it from your memory.
  when the conversation stuck on the same topic for 5 messages, ask the user a random questions.

  ## the chat is starting now:\n
  """


def load_prompt_from_file(file_path):
  """
  @description: get a file string path and save it in the system instruction prompt varible
                when you write your prompt you can reffer to the character you made by adding {character_details}
                or reffering it with json format if it is avilible with {cd.get("name")}
  """
  global character_details
  global system_template
  assert character_details is not None, "set a character with generate_character() or set_character(chracter_data)"
  try:
    cd = json.loads(character_details)
  except:
    cd = {}
    print("couldn't create json format for the character")
  try:
    f = open(file_path, "r")
  except:
    try:
      f = open(file_path+".txt", "r")
    except:
      assert "failed to load file, check if the file is exist or is it in txt format"
  system_template = f.read()

def load_prompt_from_str(instruction_prompt):
  """
  @description: get a file string path and save it in the system instruction prompt varible
                when you write your prompt you can reffer to the character you made by adding {character_details}
                or reffering it with json format if it is avilible with {cd.get("name")}
  """
  global character_details
  global system_template
  assert character_details is not None, "set a character with generate_character() or set_character(chracter_data)"
  try:
    cd = json.loads(character_details)
  except:
    cd = {}
    print("couldn't create json format for the character")
    
  system_template = instruction_prompt

def set_user_prompt(prompt):
  global system_template
  global memory
  assert system_template is not None, "you didn't load a prompt, call load_prompt_v1() or load_prompt_from_file()"
  memory.appendleft('\nUser: '+prompt+'')
  prompt = system_template+ "\n".join(list(memory))
  # print(prompt)

  # messages = system_template + temp

def get_character_answer():
  global system_template
  global memory
  temp_list = list(memory)
  temp_list.reverse()
  prompt = system_template+ "\n".join(temp_list)
  # print(prompt)
  response = get_completion_new(''.join(prompt)+"character"+": ")
  memory.appendleft("Response"+": "+response)
  
  return response

def print_prompt():
  global system_template
  global memory
  print("===== Debug output ======")
  temp_list1 = list(memory)
  temp_list1.reverse()
  prompt = system_template+ "\n".join(temp_list1)
  print(prompt)
  print("==========================")

def set_memory_size(memory_size):
  global memory
  memory = deque([],memory_size)

def reset_memory():
  global memory
  global memory_size
  memory = deque([],memory_size)

def message_to_response(message):
  """
  @description: this function get message and return the response of the character
  @param message: (str) the message you tell to the character
  """
  set_user_prompt(message)
  return get_character_answer()