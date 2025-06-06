#!/usr/bin/python3

import os
import random
import base64
import hashlib
import marshal

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

    pools = ["sdf", "bnb", "mnc", "iuu", "hgf", "jaq", "daq", "apr",
             "pou", "gsy", "bry", "sqf", "weq", "yhf", "ñlk", "bcd"]
    random.shuffle(pools)
    letter_random_1 = pools[0]
    letter_random_2 = pools[1]
    letter_random_3 = pools[2]
    letter_random_4 = pools[3]

    try:
        with open(path, 'r', encoding='latin-1') as f:
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
        h = hashlib.sha256(v.encode('utf-8')).hexdigest()
        inverse_table_items.append(f"    '{h}': '{k}'")
    inverse_table_str = "{\n" + ",\n".join(inverse_table_items) + "\n}"

    inner_code = []
    inner_code.append("import hashlib")
    inner_code.append(f"{letter_random_3} = '''")
    inner_code.append(obfuscated)
    inner_code.append("'''")
    inner_code.append(f"{letter_random_4} = {inverse_table_str}")
    inner_code.append(f"{letter_random_2} = ''")
    inner_code.append("i = 0")

    for _ in range(12):
        inner_code.append("#Z2JlamRzanNzaGhzanNoc2hzYmhzaGhhaHNoc2h6aHpoWmhoaGhoZ2dnZ2dndnZ2Ygo=")

    inner_code.append(f"while i < len({letter_random_3}):")
    for _ in range(7):
        inner_code.append("    #Z2JlamRzanNzaGhzanNoc2hzYmhzaGhhaHNoc2h6aHpoWmhoaGhoZ2dnZ2dndnZ2Ygo=")

    inner_code.append(f"    ss = {letter_random_3}[i:i+2]")
    inner_code.append(f"    h = hashlib.sha256(ss.encode('utf-8')).hexdigest()")
    for _ in range(7):
        inner_code.append("    #Z2JlamRzanNzaGhzanNoc2hzYmhzaGhhaHNoc2h6aHpoWmhoaGhoZ2dnZ2dndnZ2Ygo=")

    inner_code.append(f"    if h in {letter_random_4}:")
    for _ in range(7):
        inner_code.append("        #Z2JlamRzanNzaGhzanNoc2hzYmhzaGhhaHNoc2h6aHpoWmhoaGhoZ2dnZ2dndnZ2Ygo=")
    inner_code.append(f"        {letter_random_2} += {letter_random_4}[h]")
    inner_code.append("        i += 2")
    inner_code.append("    else:")
    inner_code.append(f"        {letter_random_2} += {letter_random_3}[i]")
    for _ in range(7):
        inner_code.append("        #Z2JlamRzanNzaGhzanNoc2hzYmhzaGhhaHNoc2h6aHpoWmhoaGhoZ2dnZ2dndnZ2Ygo=")
    inner_code.append("        i += 1")
    inner_code.append(f"exec({letter_random_2})")

    inner_code_str = "\n".join(inner_code)

    code_obj_inner = compile(inner_code_str, '<string>', 'exec')
    marshalled_inner = marshal.dumps(code_obj_inner)
    code_base64_bytes = base64.b64encode(marshalled_inner)
    code_base64_str = code_base64_bytes.decode('utf-8')

    final_code_lines = [
        "import base64",
        "import marshal",
        "",
        f"buffer = '''{code_base64_str}'''",
        "",
        "marshalled = base64.b64decode(buffer)",
        "code_obj = marshal.loads(marshalled)",
        "exec(code_obj, globals(), locals())"
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
