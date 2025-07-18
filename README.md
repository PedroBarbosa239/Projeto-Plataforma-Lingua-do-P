# 🗣️ Tradutor da Língua do P com Reconhecimento de Voz

Este projeto em Python escuta uma frase falada, transforma-a em texto com reconhecimento de voz offline e converte o resultado para a "Língua do P", uma brincadeira linguística onde se insere a letra "P" antes de cada sílaba da palavra.

---

## 🎯 Objetivo

Demonstrar o uso de bibliotecas de reconhecimento de voz com Python e aplicar regras simples de transformação linguística, gerando um tradutor divertido e funcional para a “Língua do P”.

---

## 🧰 Tecnologias e Bibliotecas Utilizadas

- [Python 3.12](https://www.python.org/)
- [Vosk](https://github.com/alphacep/vosk-api) — Reconhecimento de fala offline.
- [SoundDevice](https://pypi.org/project/sounddevice/) — Captura de áudio via microfone.
- Modelo de voz: [`vosk-model-small-pt-0.3`](https://alphacephei.com/vosk/models)

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/lingua-do-p.git
cd lingua-do-p
```
### 2. Crie um ambiente virtual (opcional, mas recomendado)
```bash
Copiar
Editar
python -m venv venv
venv\Scripts\activate  # Windows
```
### 3. Instale as dependências
```bash
pip install vosk sounddevice
```
## 🚀 Como Usar
Com tudo instalado, execute o script principal:
```bash
python "Gerador de lingua do p.py"
```
