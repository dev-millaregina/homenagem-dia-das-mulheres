# Dia Internacional da Mulher - Gerador de Homenagens

![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge\&logo=github\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Microsoft Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge\&logo=microsoft-azure\&logoColor=white)

## 📌 Sobre o Projeto

Este projeto foi desenvolvido durante o curso Microsoft Azure Cloud Native 2026, promovido pela Digital Innovation One.

A aplicação consiste em um gerador de homenagens para o Dia Internacional da Mulher, permitindo que o usuário crie mensagens personalizadas para mulheres importantes em sua vida. Além da geração da mensagem, o sistema também recomenda livros escritos por autoras, acompanhados de uma frase inspiradora na obra.

O objetivo do projeto é demonstrar o desenvolvimento de uma aplicação web em Python, containerizada com Docker e publicada na nuvem utilizando serviços da Microsoft Azure, com acesso público via URL.

## Estrutura do Projeto

```
homenagem-mulheres
│
├── app.py                - Aplicação principal em Streamlit
├── livros.py             - Base de livros e função de recomendação
├── requirements.txt      - Dependências do projeto
├── Dockerfile            - Configuração do container Docker
├── script.ps1            - Registro dos comandos utilizados no deploy
└── img/                  - Capturas de tela da aplicação
```

## 📷 Screenshots

#### 1️⃣ Página inicial da aplicação

<img src="img/1-site.png" width="70%" />

#### 2️⃣ Formulário preenchido

<img src="img/2-dados-preenchidos.png" width="60%" />

#### 3️⃣ Resultado da homenagem gerada

<img src="img/3-retorno.png" width="60%" />

## ▶️ Como Rodar o Projeto

Para rodar o projeto e reproduzir o deploy, foi utilizado:

* Terminal PowerShell no Visual Studio Code
* Extensão PowerShell no VS Code
* Azure CLI autenticado na conta da Microsoft Azure
* Docker Desktop

O passo a passo completo de build da imagem Docker, execução local, criação dos recursos na nuvem e publicação do container está documentado no arquivo `script.ps1`.

## 🌐 Acesso à Aplicação Web

A aplicação foi publicada na nuvem utilizando Azure Container Apps, permitindo acesso público via navegador. Após o deploy, o Azure gera automaticamente uma URL pública para acesso à aplicação.

Exemplo:

```
https://homenagem-streamlit-app--faiimsi.calmsea-2a22d05c.eastus.azurecontainerapps.io/
```

Toda a aplicação roda dentro de um container Docker, hospedado na infraestrutura da Microsoft Azure.

## 🤖 Uso de Inteligência Artificial

Durante o desenvolvimento do projeto foi utilizado o ChatGPT como ferramenta de apoio para auxiliar em algumas etapas do desenvolvimento.

O uso de IA foi um requisito proposto na atividade do curso, sendo utilizado principalmente para:

* apoio na estruturação de partes do código Python
* auxílio na criação e organização do `README.md`
* suporte na criação do `script.ps1` com os comandos utilizados no deploy
* revisão e sugestões de melhoria na documentação

## Tecnologias

| Tecnologia | Finalidade |
| --------- | --------- |
| Python | Desenvolvimento da aplicação |
| Streamlit | Interface web interativa |
| Docker | Containerização da aplicação |
| Microsoft Azure | Hospedagem da aplicação |
| Azure Container Registry | Armazenamento da imagem Docker |
| Azure Container Apps | Publicação do container com URL pública |

## 💡 Aprendizados

* Desenvolvimento de aplicações web com Python e Streamlit
* Containerização de aplicações com Docker
* Publicação de imagens no Azure Container Registry
* Deploy de aplicações web usando Azure Container Apps
* Criação de aplicações acessíveis publicamente na nuvem

## Autora

Milla Regina Lopes Vieira - [LinkedIn](https://www.linkedin.com/in/milla-regina-468020206/)