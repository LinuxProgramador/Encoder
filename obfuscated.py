#!/usr/bin/python3

import os
import random
import base64
import sys

CHARACTERS = {
    'd': '€¢',
    'g': '£∆',
    'c': 'π√',
    'w': '¥°',
    'o': '§∆',
    'r': '®™',
    'm': '¥¢',
    's': '§π',
    'x': '€^',
    'p': '©€'
}


def obfuscation():
    path = input("Enter the full path of the file to obfuscate: ").strip()
    if not os.path.isfile(path):
        print("Error: Specified file not found.")
        return

    pools = ["sdf", "bnb", "mnc", "iuu", "hgf", "jaq", "daq", "apr", "pou", "gsy", "bry", "sqf", "weq", "yhf", "ñlk", "bcd"]
    random.shuffle(pools)
    letter_random_1 = pools[0]
    letter_random_2 = pools[1]
    letter_random_3 = pools[2]
    letter_random_4 = pools[3]

    try:
        with open(path, 'r', encoding='utf-8') as f:
            original_code = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    obfuscated = []
    for ch in original_code:
        if ch in CHARACTERS:
            obfuscated.append(CHARACTERS[ch])
        else:
            obfuscated.append(ch)
    obfuscated = ''.join(obfuscated)

    inverse_table_items = []
    for k, v in CHARACTERS.items():
        inverse_table_items.append(f"    '{v}': '{k}'")
    inverse_table_str = "{\n" + ",\n".join(inverse_table_items) + "\n}"


    inner_code = []
    inner_code.append(f"{letter_random_3} = '''")
    inner_code.append(obfuscated)
    inner_code.append("'''")
    inner_code.append("")
    inner_code.append(f"{letter_random_4} = {inverse_table_str}")
    inner_code.append(f"{letter_random_2} = ''")
    inner_code.append("i = 0")
    inner_code.append("")
    inner_code.append(f"while i < len({letter_random_3}):")
    inner_code.append(f"    ss = {letter_random_3}[i:i+2]")
    inner_code.append(f"    if ss in {letter_random_4}:")
    inner_code.append(f"        {letter_random_2} += {letter_random_4}[ss]")
    inner_code.append("        i += 2")
    inner_code.append("    else:")
    inner_code.append(f"        {letter_random_2} += {letter_random_3}[i]")
    inner_code.append("        i += 1")
    inner_code.append("")
    inner_code.append(f"exec({letter_random_2})")

    inner_code_str = "\n".join(inner_code)

    inner_bytes = inner_code_str.encode('utf-8')
    code_base64_bytes = base64.b64encode(inner_bytes)
    code_base64_str = code_base64_bytes.decode('utf-8')

    final_code_lines = [
        "import base64",
        "import random as rnd",
        "import sys as s",
        "",
        "def __system__():",
        "   x = 42",
        "   y = 'x'",
        "   z = [i for i in range(10)]",
        "   for i in z:",
        "        x += i",
        "   return x",
        "def __cores__():",
        "   try:",
        "       val = int('not_a_number')",
        "   except ValueError:",
        "       pass",
        "       return None",
        f"buffer = '''{code_base64_str}'''",
        "system = base64.b64decode(buffer)",
        "exec(system, globals(), locals())"
    ]
    final_code = "\n".join(final_code_lines)

    output_path = os.path.join(os.getcwd(), "obfuscated_code.py")
    try:
        with open(output_path, 'w', encoding='utf-8') as fw:
            fw.write(final_code)
    except Exception as e:
        print(f"Error writing output file: {e}")
        return

    print(f"The file has been successfully obfuscated and saved to:  {output_path}")
    
if __name__ == "__main__":
    obfuscation()
