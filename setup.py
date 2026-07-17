from setuptools import setup, find_packages
import os

# Lecture du fichier requirements.txt
with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

# Lecture du README.md pour la description longue
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='wooma-rag-assistant',
    version='0.1.0',
    description='Une application RAG (Vectoriseur + Chat) créée pour la communauté de développeurs Python en Afrique.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Wooma CI / Communauté Africaine',
    url='https://github.com/bigdahaut/rag-assistant', # Lien vers votre futur repo
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'rag-vectorizer=rag_assistant.rag_vectorizer_gui:run_gui',
            'rag-chat=rag_assistant.rag_chat_app:run_server',
        ],
    },
    python_requires='>=3.8',
)