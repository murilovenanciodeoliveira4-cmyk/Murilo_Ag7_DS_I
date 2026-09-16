# 💧 Sistema de Classificação do Consumo de Água

## 🌱 Sobre o projeto

Este projeto foi desenvolvido para uma campanha de conscientização ambiental de uma companhia de saneamento.

O sistema solicita o tipo de imóvel e o consumo mensal de água em metros cúbicos (m³). Com essas informações, o programa classifica o perfil de consumo e apresenta uma mensagem educativa ao morador.

## 🎯 Objetivo

Classificar o consumo de água de imóveis comerciais e residenciais, ajudando a conscientizar os usuários sobre a importância do uso responsável da água.

## 🐍 Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)

- 🐍 Python
- 🐙 GitHub

## 📋 Funcionamento

O programa solicita:

1. 🏠 Tipo de imóvel:
   - Comercial
   - Casa
   - Apartamento

2. 💧 Consumo mensal de água em m³.

Depois, o sistema verifica as informações e apresenta uma classificação.

## 📊 Regras de classificação

- 🏢 **Comercial:** tarifa comercial aplicada.
- 🏠 **Apartamento com consumo menor que 10 m³:** consumo econômico.
- 🏠 **Apartamento ou casa com consumo de até 25 m³:** consumo moderado.
- ⚠️ **Demais situações:** consumo excessivo.

## ▶️ Como executar

1. Instale o Python no computador.
2. Baixe ou clone este repositório.
3. Acesse a pasta `consumo-agua`.
4. Execute o arquivo `app.py`.

No terminal:

```bash
python app.py
