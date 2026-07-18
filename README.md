# 🌍 Wooma African RAG Assistant

Un package Python complet développé par et pour la communauté africaine (Wooma CI), combinant un vectoriseur de documents et un assistant conversationnel (RAG) propulsé par l'IA.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🎯 Fonctionnalités

- **Vectoriseur de documents (GUI)** : Interface graphique élégante pour extraire et vectoriser vos données (PDF, DOCX, XLSX, CSV, JSON, TXT) vers ChromaDB.
- **Chat Assistant (Web UI)** : Interface web réactive avec streaming, historique, copie de code et coloration syntaxique.
- **Prêt pour l'intégration** : Utilisable en ligne de commande (CLI) ou importable en tant que module dans vos propres scripts Python.
- **FastAPI Ready** : Montez le chat directement comme une sous-application dans vos propres projets FastAPI.

## 🚀 Installation

Installez simplement le package via pip :

```bash
pip install wooma-rag-assistant

Note : Assurez-vous d'avoir Ollama installé et lancé en arrière-plan pour l'inférence des modèles LLM.

💻 Cas d'utilisation

1. En ligne de commande (CLI)

Une fois installé, vous disposez de deux commandes globales dans votre terminal :

Lancer le vectoriseur (Interface Graphique) :

rag-vectorizer

Lancer le serveur Web de Chat :

rag-chat --port 8080 --model llama3.2

2. Importation dans vos propres scripts Python

Vous pouvez réutiliser la logique d'extraction de documents dans vos projets Data Science :

from pathlib import Path
from rag_assistant import DocumentProcessor, CollectionManager

# Extraire le texte et les métadonnées d'un fichier
fichier = Path("mon_document_afrique.pdf")
processeur = DocumentProcessor()
lignes, metadonnees = processeur.process_file(fichier)

print(f"Extractions : {len(lignes)} fragments.")

# Voir vos collections ChromaDB
manager = CollectionManager()
print(manager.list_collections())

3. Intégration dans une API (FastAPI)

Vous développez déjà une API FastAPI ? Montez notre application RAG en une seule ligne de code :

import uvicorn
from fastapi import FastAPI
from rag_assistant import app as rag_app

mon_api = FastAPI()

@mon_api.get("/hello")
def hello():
    return {"message": "Bienvenue sur mon API"}

# Intégrer l'assistant RAG sous l'URL /rag
mon_api.mount("/rag", rag_app)

if __name__ == "__main__":
    uvicorn.run(mon_api, host="0.0.0.0", port=8000)

Rendez-vous ensuite sur http://localhost:8000/rag/ !

🤝 Contribution

Vos contributions (Pull Requests) sont les bienvenues pour améliorer cet outil !

---

### 2. Procédure pour mettre à jour sur PyPI (v0.1.2)

1.  **Modifiez `setup.py`** : Changez la ligne `version='0.1.1'` en `version='0.1.2'`.
2.  **Nettoyez et Recompilez** :
    ```bash
    rm -rf dist/ build/ *.egg-info
    python -m build
    ```
3.  **Envoyez sur PyPI** :
    ```bash
    twine upload dist/*
    ```
4.  **Synchronisez GitHub** :
    ```bash
    git add README.md setup.py
    git commit -m "docs: ajout de la coloration syntaxique au README"
    git push origin main
    ```

