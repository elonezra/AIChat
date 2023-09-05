# AIChat doc

## how to install

pip install git+<GitHub_URL>

## how to use

To use the module make sure you have openai installed.

1. call the function ``set_key("")`` and give it the key
2. create a character to talk with by using the functions ``generate_character()``
to let the model generate a model. or ``set_character(chracter_data)`` to write your own characteristics. better to use the following json format:
```
{
    "ethnicity": "",
    "name": "",
    "age": 28,
    "sex": " ",
    "country": " ",
    "city": "",
    "hobbies": ["Reading", "Hiking", "Painting"],
    "appearance": {
        "height": "5\'7\\"", "hairColor": "Blonde","eyeColor": "Blue"},
        "traits": ["Friendly", "Creative", "Empathetic"]
}
```
3. call ``load_prompt_v1()`` in order to load the instructions promt
4. set the user input with the function ``set_user_prompt(user_prompt)``
5. get the response of the character with the function ``printget_character_answer()``
