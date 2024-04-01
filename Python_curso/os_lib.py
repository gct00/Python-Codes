import os
print(os.path)
print(os.path.abspath('./test/folder/__init__/py'))

path_test_file = os.path.abspath('./test/folder/__init__/py')
print(os.path.dirname(path_test_file))

# Caminho relativo do arquivo
print(__file__)

# Caminho absoluto do arquivo
print(os.path.abspath(__file__))
