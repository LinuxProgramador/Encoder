Polymorphic Encoder for Python 3

Disclaimer
The author assumes no responsibility for any misuse of this tool. It was developed strictly for educational and research purposes.

Description
This tool encrypts Python 3 source code using a polymorphic encoding technique designed to evade rapid detection by antivirus software.

Important Notes:

The script is only for Linux Distros 

In the output of the obfuscated code, "#!/usr/bin/python3" is applied but it is a junk note, you can remove it if you like.

The Python 3 source code is provided via an external file.

The script is obfuscated to avoid being analyzed by antivirus companies and rendered useless. 


Execution
To run the encrypted code, use the following command:

    python3 encrypted_code.py

Supported Architectures

    linux_aarch64

    linux_armv7

    linux_x86_64


Dependencies
Make sure you have the following installed:

    Python 3.10.12

    pip for Python 3


Installation
To install the required dependencies, run:

    python3 -m pip install -r requirements.txt

Usage
To encrypt a Python script, run:

    python3 encoder.py

Method for Executing Obfuscated Code from an Executable Using the exec() Function

Note: In the executable, ensure that all necessary modules from the obfuscated code are imported, including cryptography.fernet, as shown in the example below:

    from bcrypt import checkpw
    
    from cryptography.fernet import Fernet

    with open('encrypted_code.py', 'r') as read_file:
    
      script = read_file.read()
      
      exec(script)
