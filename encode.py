#!/usr/bin/python3

import base64
from string import ascii_letters
from cryptography.fernet import Fernet
from secrets import choice
from sys import exit
from os import urandom, getcwd, path
from py_compile import compile


def generate_random_noise():
    """Genera ruido aleatorio como cadenas base64 codificadas."""
    return ''.join(str(base64.b64encode(urandom(128))) for _ in range(choice(range(5, 20))))


def generate_variable_names():
    """Genera nombres aleatorios para variables internas."""
    return {
        'key_var': choice(["uqZ", "Md", "aqJ", "dfs", "srr"]),
        'enc_var': choice(["uHp", "oou", "i", "y", "w"]),
        'fernet_func_var': choice(["s", "th", "rAnr", "cc", "z"]),
        'dec_var': choice(["seI", "h", "dd", "aa", "kk"]),
        'compiled_code_var': choice(["sqeueI", "hvcd", "dreqd", "aaklu", "ksf"]),
        'func_name': choice(["corn", "gskq", "shq", "bdjshwjw92627", "djjdhddh67"]),
        'fernet_class_alias': choice(["coffe", "gcxq", "shgeuq", "jftt", "asvy"])
    }


def generate_script(template_id, names, key, encrypted_data, noise_1, noise_2):
    """Genera el contenido del script basado en una plantilla seleccionada."""
    templates = [
        f"""#!/usr/bin/python3

{names['func_name']} = "{noise_2}"
import datetime
import time
from cryptography.fernet import Fernet as {names['fernet_class_alias']}
{names['key_var']} = {key}
{names['func_name']} = "{noise_1}"
{names['enc_var']} = {encrypted_data}
{names['fernet_func_var']} = {names['fernet_class_alias']}({names['key_var']})
{names['func_name']} = "{noise_1}"
{names['dec_var']} = {names['fernet_func_var']}.decrypt({names['enc_var']}).decode()
exec({names['dec_var']})
""",

        f"""#!/usr/bin/python3
{names['func_name']} = "{noise_1}"
import time
from cryptography.fernet import Fernet
{names['key_var']} = {key}
{names['enc_var']} = {encrypted_data}
{names['func_name']} = "{noise_1}"
{names['fernet_func_var']} = Fernet({names['key_var']})
{names['func_name']} = "{noise_1}"
{names['dec_var']} = {names['fernet_func_var']}.decrypt({names['enc_var']}).decode()
{names['compiled_code_var']} = compile({names['dec_var']}, '<string>', 'exec')
exec({names['compiled_code_var']})
""",

        f"""#!/usr/bin/python3

import time, base64, sys
from cryptography.fernet import Fernet as {names['fernet_class_alias']}
{names['key_var']} = {key}
{names['func_name']} = "{noise_1}"
{names['enc_var']} = {encrypted_data}
{names['fernet_func_var']} = {names['fernet_class_alias']}({names['key_var']})
{names['dec_var']} = {names['fernet_func_var']}.decrypt({names['enc_var']}).decode()
{names['compiled_code_var']} = compile({names['dec_var']}, '<string>', 'exec')
eval({names['compiled_code_var']})
""",

        f"""#!/usr/bin/python3

import random, shutil
from cryptography.fernet import Fernet
{names['key_var']} = {key}
{names['enc_var']} = {encrypted_data}
{names['fernet_func_var']} = Fernet({names['key_var']})
{names['dec_var']} = {names['fernet_func_var']}.decrypt({names['enc_var']}).decode()
{names['compiled_code_var']} = compile({names['dec_var']}, '<string>', 'exec')
eval({names['compiled_code_var']})
""",

        f"""#!/usr/bin/python3

import sys, os
from cryptography.fernet import Fernet as {names['fernet_class_alias']}
{names['key_var']} = {key}
{names['func_name']} = "{noise_1}"
{names['enc_var']} = {encrypted_data}
{names['func_name']} = "{noise_1}"
{names['func_name']} = "{noise_1}"
{names['fernet_func_var']} = {names['fernet_class_alias']}({names['key_var']})
{names['dec_var']} = {names['fernet_func_var']}.decrypt({names['enc_var']}).decode()
exec({names['dec_var']})
"""
    ]
    return templates[template_id]


def encoder_data(data):
    """Codifica el contenido y genera un archivo con el código cifrado."""
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())

    var_names = generate_variable_names()
    random_noise_1 = generate_random_noise()
    random_noise_2 = generate_random_noise() or "fallback_noise"

    template_choice = choice(range(5))
    script_content = generate_script(template_choice, var_names, key, encrypted_data, random_noise_1, random_noise_2)

    with open("encrypted_code.py", "w", encoding="utf-8") as write_file:
        write_file.write(script_content)

    compile("encrypted_code.py", path.join(getcwd(), "encrypted_code.pyc"))
    print("Encrypted script 'encrypted_code.py' and compiled version 'encrypted_code.pyc' generated.")


def main():
    try:
        code_path = input("Enter the full path to your code: ").strip()
        with open(code_path, 'r', encoding="utf-8") as read_file:
            code = read_file.read()
        encoder_data(code)
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Operation canceled.")
        exit()
    except FileNotFoundError as e:
        print(f"[Error] Path not found: {e}")
    except IsADirectoryError as d:
        print(f"[Error] Directory path provided: {d}")
    except ValueError as ve:
        print(f"[Error] Value error: {ve}")


if __name__ == "__main__":
    main()
