#!/usr/bin/python3

from cryptography.fernet import Fernet
from secrets import choice
from sys import exit
from string import ascii_lowercase,ascii_uppercase
from os import urandom,getcwd,path
import base64
from py_compile import compile


def encoder_data(random5,random4,data,random,random2,file_enc_caracter_random,func_fernet_caracter_random,file_dec_caracter_random,key_caracter_random,compile_code_caracter_random):
    pyc_path = getcwd()
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypt_data = fernet.encrypt(data.encode())
    if choice(range(5)) == 0:
      script_content = f'''#!/usr/bin/python3


{random4} = "{random2}"
import datetime #"{random}"
import time
"{random}"
from cryptography.fernet import Fernet as {random5} #"{random}"
"{random2}"
{key_caracter_random} = {key} #{random4} = "{random2}"
{random4} = "lambda: {choice(range(500))}+{choice(range(15))}"
{file_enc_caracter_random} = {encrypt_data} #{random4} = "{random2}"
"{random}"
def {random4}():
   {random4} = {choice(range(100))}
{func_fernet_caracter_random} = {random5}({key_caracter_random}) #"{random}"
"{random}"
#{random2}
{random4} = "{random2}"
#{random2}
{random4} = "lambda: {choice(range(1000))}+{choice(range(400))}"
{file_dec_caracter_random} = {func_fernet_caracter_random}.decrypt({file_enc_caracter_random}).decode() #"{random}"
"{random2}"
{random4} = "'{random}' if {choice(range(10))} in [1,2,9,6,7] else ''"
exec({file_dec_caracter_random}) #{random4} = "{random2}"
'''
    elif choice(range(5)) == 1:
      script_content = f'''#!/usr/bin/python3

#{random2}
import time #{random}
"{random}"
from cryptography.fernet import Fernet
"{random2}"
{key_caracter_random} = {key} #{random2}
{file_enc_caracter_random} = {encrypt_data} #{random2}
{random4} = "'{random}' if {choice(range(10))} in [1,2,9,6,7] else ''"
"{random}"
{func_fernet_caracter_random} = Fernet({key_caracter_random})
"{random}" #{random2}
{file_dec_caracter_random} = {func_fernet_caracter_random}.decrypt({file_enc_caracter_random}).decode()
"{random2}"
{compile_code_caracter_random} = compile({file_dec_caracter_random}, '<string>', 'exec')
#{random2} #{random2}
exec({compile_code_caracter_random}) #{random2}
'''
    elif choice(range(5)) == 2:
      script_content = f'''#!/usr/bin/python3

import time
"{random}"
import base64,sys #{random}
#{random2}
def {random4}():
   {random4} = {choice(range(100))}
from cryptography.fernet import Fernet as {random5}
"{random2}"
{key_caracter_random} = {key} #{random}
{random4} = "{random2}"
{file_enc_caracter_random} = {encrypt_data} #{random}
"{random}"
{func_fernet_caracter_random} = {random5}({key_caracter_random})
"{random}"
{file_dec_caracter_random} = {func_fernet_caracter_random}.decrypt({file_enc_caracter_random}).decode()
"{random2}"
{compile_code_caracter_random} = compile({file_dec_caracter_random}, '<string>', 'exec')
#{random}
eval({compile_code_caracter_random})
'''

    elif choice(range(5)) == 3:
       script_content = f'''#!/usr/bin/python3
import random,shutil
from cryptography.fernet import Fernet
{key_caracter_random} = {key}
{file_enc_caracter_random} = {encrypt_data}
{random4} = "{random2}"
{func_fernet_caracter_random} = Fernet({key_caracter_random})
{file_dec_caracter_random} = {func_fernet_caracter_random}.decrypt({file_enc_caracter_random}).decode()
{compile_code_caracter_random} = compile({file_dec_caracter_random}, '<string>', 'exec')
eval({compile_code_caracter_random})
'''

    else:
       script_content = f'''#!/usr/bin/python3
{random4} = "lambda: {choice(range(500))}+{choice(range(15))}"
"{random2}"
"{random2}"
import sys,os
from cryptography.fernet import Fernet as {random5} #{random4} = {random2}
"{random2}"
"{random}"
"{random2}"
{key_caracter_random} = {key} #{random4} = {random2}
{file_enc_caracter_random} = {encrypt_data}
"{random}"
"{random}"
"{random}"
"{random}"
{random4} = "{random2}"
{func_fernet_caracter_random} = {random5}({key_caracter_random})
"{random}"
{file_dec_caracter_random} = {func_fernet_caracter_random}.decrypt({file_enc_caracter_random}).decode() #{random4} = {random2}
"{random2}"
"{random}"
def {random4}():
   #{random2}
   {random4} = {choice(range(100))}
"{random}"
"{random}"
{random4} = "{random2}"
exec({file_dec_caracter_random}) #{random4} = {random2}
'''


    with open("encrypted_code.py", "w", encoding="utf-8") as write_file:
        write_file.write(script_content)
    print("The encrypted script 'encrypted_code.py' and its compiled version 'encrypted_code.pyc'have been successfully generated. The .pyc file is more obfuscated")
    compile("encrypted_code.py",path.join(pyc_path,"encrypted_code.pyc"))

def main():
  try:
     characters = ascii_lowercase + ascii_uppercase
     random2 = random =  ''
     random_if_empty = 'vhfferef'

     key_caracter_random = choice(list(characters))
     file_enc_caracter_random = choice(list(characters))
     func_fernet_caracter_random = choice(list(characters))
     file_dec_caracter_random = choice(list(characters))
     compile_code_caracter_random = choice(list(characters))
     random4 = choice(list(characters))
     random5 = choice(list(characters))

     values = [file_enc_caracter_random, func_fernet_caracter_random,
              file_dec_caracter_random, compile_code_caracter_random,
              key_caracter_random,random4,random5]

     for x in values:
      if x in values[0:]:
         key_caracter_random = choice(["uqZ","Md","aqJ","dfs","srr"])
         file_enc_caracter_random = choice(["uHp","oou","i","y","w"])
         func_fernet_caracter_random = choice(["s","th","rAnr","cc","z"])
         file_dec_caracter_random = choice(["seI","h","dd","aa","kk"])
         compile_code_caracter_random = choice(["sqeueI","hvcd","dreqd","aaklu","ksf"])
         random4 = choice(["corn","gskq","shq","bdjshwjw92627","djjdhddh67"])
         random5 = choice(["coffe","gcxq","shgeuq","jftt","asvy"])

     for _ in range(choice(range(20))):
       
       if choice(range(2)) == 0:
          char= str(base64.b64encode(urandom(64)))
          random += char

       elif choice(range(2)) == 1:
          char2= str(base64.b64encode(urandom(64)))
          random2 += char2

     if not random2:
          random2 = random_if_empty

     code_path = input("Enter the full path to your code: ").strip()
     with open(code_path,'r',encoding="utf-8") as read_file:
       data = read_file.read()
       encoder_data(random5,random4,data,random,random2,file_enc_caracter_random,func_fernet_caracter_random,file_dec_caracter_random,key_caracter_random,compile_code_caracter_random)

  except (KeyboardInterrupt,EOFError):
    print()
    exit()
  except FileNotFoundError as e:
    print(f"Error: Path Not Found => {e}")
  except IsADirectoryError as d:
    print(f"Error: Directory detected => {d}")
  except ValueError as F:
    print(f"Type error: {F}")

if __name__ == "__main__":
    main()


