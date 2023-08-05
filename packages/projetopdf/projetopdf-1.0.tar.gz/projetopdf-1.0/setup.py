import setuptools
from pathlib import Path

setuptools.setup(
    # devemos selecionar um nome único do package para não dar conflito com o repositório pypi
    name="projetopdf",
    version=1.0,
    long_description=Path("README.md").read_text(),
    # devemos dizer agora quais packages vão ser destribuidas. Nesse projeto, temos apenar um package e
    # nessa package temos dois modules. Devemos dizer no setuptools sobre os packages e modules que vamos
    # publicar.
    packages=setuptools.find_packages(exclude=["tests", "data"])
    # esse método vai automaticamente achar os packages que definimos. Entretanto, devemos dizer para ele
    # exclui dois diretórios (test e data), pois eles não incluem source code.
)
