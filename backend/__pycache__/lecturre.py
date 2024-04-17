import dis

# Charge le fichier .pyc en tant qu'objet de code Python
with open('device_scanner.cpython-310.pyc', 'rb') as f:
    code = f.read()

code_obj = compile(code, '<string>', 'exec')

# Désassemble le code objet
dis.dis(code_obj)
