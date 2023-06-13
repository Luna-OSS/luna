import ai
import os
import prompts
import testing

from rich import print
from rich.progress import track
from rich.console import Console

OUTPUT_PATH = r'C:\Users\Lynx\Desktop\luna_outp'

console = Console(record=True)

print('[light_steel_blue]Welcome to  [bold]L u n a[/] 💜')

def main():
    """Asks for a project description and generate the project."""

    try:
        prompt = console.input("[orchid1 bold]What kind of project should I create for you? 💬[/] ")
    except KeyboardInterrupt:
        console.print('\n[orange1 bold]Bye! 👋[/]')
        return

    console.print('[yellow2]This might take a while, so go ahead and enjoy a cup of tea. ☕[/]')

    messages = prompts.generate_messages()
    messages.append({
        'role': 'user',
        'content': f'[FILE-STRUCTURE]: {prompt}'
    })

    file_structure = ai.generate(messages).strip()
    file_list = ''.join(['\t' + path for path in file_structure])
    console.print(f'[turquoise2 bold]File structure:[/]\n{file_list}')

    messages.append({
        'role': 'assistant',
        'content': file_structure
    })

    for file_path in track(file_structure.splitlines(), description='[light_steel_blue]Generating files...'):
        messages.append({
            'role': 'user',
            'content': f'[FILE-CONTENT]: {file_path}'
        })

        file_content = ai.generate(messages)

        messages.append({
            'role': 'assistant',
            'content': file_content
        })

        path = os.path.join(OUTPUT_PATH, file_path).replace('\\', '/')
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'w', encoding='utf8') as file_:
            file_.write(file_content)

    console.print('[sea_green1 bold]Done! ✅[/]')

if __name__ == '__main__':
    main()
