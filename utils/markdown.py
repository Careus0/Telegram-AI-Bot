from config import constants

def escape_markdown(text: str) -> str:
    parts = text.split('```')
    escaped_parts = [
        ''.join(f'\\{char}' if char in constants.ESCAPE_CHARS else char for char in part)
        for part in parts
    ]
    return '```'.join(escaped_parts) 