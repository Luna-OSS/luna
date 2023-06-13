"""The prompt module contains the demo "conversation" messages used to provide an example for the
AI of how to respond to the user."""

import os
import json

messages = [
    {'role': 'system', 'content': """You program Python projects by providing every file's
contents, a documentation in the form of a Markdown file as well as a list of all files.

It is really important that also tests are provided, which check the functionality of the
project! The tests should check the functionality of the project, and should be created at the end.
The first file content to provide is the README.md file, which should contain a description of the
project, as well as a simple documentation on how to run the project, as well as how it works.

For example, for a web app, you should not only provide the commands to run the project, but also
the URL paths and what they do.

Keep in mind to also use a nice CSS design if the project is a web app!
Completely avoid using APIs which require an API key, as this would make it impossible to run the project!
Whenever possible, use APIs which are free to use and don't require an API key instead!
"""}
]

def generate_messages():
    """Generates the messages for the AI "conversation".
    """

    for example in os.listdir('luna/training'):
        example_path = f'luna/training/{example}'

        with open(f'{example_path}/_prompt.luna.txt', encoding='utf8') as prompt_file:
            prompt = prompt_file.read()

        messages.append({
            'role': 'user',
            'content': f'[FILE-STRUCTURE]: {prompt}'
        })

        contents = {}

        for root, _, files in os.walk(example_path):
            for file_ in files:
                file_path = os.path.join(root, file_)\
.replace('\\', '/').replace(example_path + '/', '')

                if '__pycache__' in file_path or '.luna.' in file_path:
                    continue

                contents[file_path] = open(os.path.join(root, file_), encoding='utf8').read()

        structure = ''

        for file_path in contents:
            structure += f'{file_path}\n'

        messages.append({
            'role': 'assistant',
            'content': structure
        })

        for file_path, content in contents.items():
            messages.append({
                'role': 'user',
                'content': f'[FILE-CONTENT]: {file_path}'
            })

            messages.append({
                'role': 'assistant',
                'content': content
            })

    return messages
        
if __name__ == '__main__':
    json.dump(generate_messages(), open('luna/prompts.json', 'w', encoding='utf8'), indent=4)
