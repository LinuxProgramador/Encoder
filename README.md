Polymorphic Encoder for Python 3

Disclaimer
The author assumes no responsibility for any misuse of this tool. It was developed strictly for educational and research purposes.

RECOMMENDATION: Run encode.py first and then pass obfuscate.py to it, also recommended one round each

Dependencies:

Make sure you have the following installed:

    Python3

    pip for Python 3


Installation:

To install the required dependencies, run:

    python3 -m pip install cryptography

Usage:

To encrypt a Python script, run:

    python3 encode.py

Method for Executing Obfuscated Code from an Executable Using the exec() Function

Note: In the executable, ensure that all necessary modules from the obfuscated code are imported, including cryptography.fernet, as shown in the example below:

    from cryptography.fernet import Fernet
    import base64, hashlib
    
    with open('encrypted_code.py', 'r') as read_file:
    
      script = read_file.read()
      
      exec(script)
