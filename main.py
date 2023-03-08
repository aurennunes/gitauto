import os
import sys
from modules.libs.bootstrapy import Strapy

print(Strapy.INFO + 'Add files\n' + Strapy.END)
os.system('git add .')
print(Strapy.GOOD + 'Success in add files' + Strapy.END + '\n\n')

_list = (
    {"name": "BUILD 📦", "description": "AJUSTE NAS CONFIGURAÇÕES DE BUILD"},
    {"name": "FIX 🐛", "description": "RESOLVE UM BUG"},
    {"name": "FEAT ✨", "description": "INICIA A IMPEMENTAÇÃO DE UMA FUNCIONALIDADE"},
    {"name": "CHORE 🔧", "description": "TRABALHO EM PROGRESSO DE UMA FUNCIONALIDADE"},
    {"name": "REFACTOR 🔨", "description": "AJUSTE SEM MUDAR LÓGICA - REFATORAÇÃO"},
    {"name": "TEST 🚨", "description": "IMPLEMENTA TESTES AUTOMATIZADOS"},
    {"name": "STYLE 💎", "description": "MUDANÇAS DE FORMATAÇÃO DO CÓDIGO - LINT"},
    {"name": "PERF 🚀", "description": "AJUSTES DE PERFORMANCE"},
    {"name": "DOCS 📚", "description": "INSERE DOCUMENTAÇÃO"},
    {"name": "CI 👷", "description": "AJUSTE NAS CONFIGURAÇÕES DO CI"},
)

x = 0
for item in _list:
    print(Strapy.RED +
          f'[{x}] ' + Strapy.END + Strapy.GREEN + f'<{item["name"]}>: ' + Strapy.END + Strapy.BLUE + f'{{{item["description"]}}}' + Strapy.END)
    x += 1

_type = int(input('''

Input the type number: '''))

scope = str(input('Scope: '))
description = str(input('Description: '))


print('\n' + Strapy.INFO + 'Commit in repository\n' + Strapy.END)
os.system(f'git commit -m "<{_list[_type]["name"]}>[{scope}]: {description}"')
print(Strapy.GOOD + 'Success in commit' + Strapy.END + '\n\n')

print(Strapy.INFO + 'Pushing in repository\n' + Strapy.END)
os.system('git push')
print(Strapy.GOOD + 'Success in Pushing' + Strapy.END + '\n\n')
