# mcp_judge

[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
![license - MIT](https://img.shields.io/badge/license-MIT-green)
![site - prazocerto.me](https://img.shields.io/badge/site-prazocerto.me-230023)
![linkedin - @marioluciofjr](https://img.shields.io/badge/linkedin-marioluciofjr-blue)

## Índice

* [Introdução](#introdução)
* [Estrutura do projeto](#estrutura-do-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Requisitos](#requisitos)
* [Como instalar no Claude Desktop](#como-instalar-no-claude-desktop)
* [Links úteis](#links-úteis)
* [Contribuições](#contribuições)
* [Licença](#licença)
* [Contato](#contato)

## Introdução

O **mcp-judge** é um servidor que implementa o Model Context Protocol (MCP) para atuar como um juiz imparcial e rigoroso de saídas de LLMs. Diferente de uma avaliação puramente subjetiva, este projeto utiliza uma ferramenta computacional para aplicar pesos exatos e penalidades lógicas baseadas em critérios como alucinação e precisão. O objetivo é fornecer um veredito matemático ("Aprovado", "Requer Revisão" ou "Reprovado"), punindo erros graves independentemente da qualidade da escrita.

## Estrutura do projeto

É um MCP-Server simples que utiliza somente o pacote FastMCP, seguindo também as orientações do repositório oficial do [Model Context Protol](https://github.com/modelcontextprotocol/python-sdk), da Anthropic.

Este MCP-Server tem as seguintes classes:

### `calcular_veredito` (Tool)
Realiza o cálculo da nota final aplicando pesos e penalidades:
*   **Pesos**: Alucinação (40%), Precisão (30%), Completude (15%), Clareza (15%).
*   **Penalidades**: Notas baixas em Alucinação ou Precisão travam o score final em "Reprovado".

### `prompt_juiz` (Prompt)
Define a persona de um "Juiz Crítico" para o Claude. Instrui o modelo a analisar o input/output, atribuir notas mentais e obrigatoriamente invocar a tool `calcular_veredito` para o resultado oficial.

> [!IMPORTANT]
> Se quiser conversar sobre esse projeto, basta acessar a versão [`TalkToGitHub`](https://talktogithub.com/marioluciofjr/mcp_judge) <br>
> Want to better understand this repository, but you don't speak Portuguese? Check out this complete tutorial: [`Codebase - mcp_judge`](https://code2tutorial.com/tutorial/2a71af2f-9436-4910-8b83-3c2b18665463/index.md)

## Tecnologias utilizadas

<div>
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/c0604008-f730-413f-9c4e-9b06c0912692" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/76e7aca0-5321-4238-9742-164c20af5b4a" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/cf957637-962d-4548-87d4-bbde91fadc22" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://i.namu.wiki/i/kARx1nP9GHaTktx_4yTI4HXLOjmd3JZaKJkHTXgE2bv4UATWXkVlvoE6ktFO4MFI6yMcV50x6z-pisOEDBOUOQ.webp" />&nbsp;&nbsp;&nbsp
 </div><br>

* MCP (Model Context Protocol);
* Python;
* Claude Desktop;
* Antigravity.

## Requisitos

Antes de começar, certifique-se de ter instalado:
*   [Python 3.10](https://www.python.org/downloads/) ou superior.
*   [UV](https://github.com/astral-sh/uv) (Recomendado) ou PIP.
*   [Claude Desktop](https://claude.ai/download).

## Como instalar no Claude Desktop

### 1. Baixar o projeto
Se você não sabe usar o Git, pode simplesmente baixar o projeto clicando no botão verde **Code** no topo da página do GitHub e selecionando **Download ZIP**. Extraia a pasta em um local de sua preferência (Ex: `Área de Trabalho`).

### 2. Configurar o Claude Desktop
Abra o arquivo de configuração do Claude Desktop (`claude_desktop_config.json`).
*   **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Adicione a configuração abaixo. **Importante**: Substitua o caminho em `args` e `--directory` pelo local onde você salvou a pasta extraída (`mcp_judge`).

```json
    "mcp-judge": {
      "command": "uv",
      "args": [
        "--directory",
        "C://Users//meu_usuario//OneDrive//area_de_trabalho//MCPs//mcp_judge",
        "run",
        "server.py"
      ]
    }
```

O comando acima usa o `uv` para criar ambiente e instalar dependências automaticamente antes de rodar.

## Links úteis

* [Documentação oficial do Model Context Protocol](https://modelcontextprotocol.io/introduction) - Você saberá todos os detalhes dessa inovação da Anthropic
* [Site oficial da Anthropic](https://www.anthropic.com/) - Para ficar por dentro das novidaddes e estudos dos modelos Claude
* [Como baixar o Claude Desktop](https://claude.ai/download) - Link direto para download
* [Como instalar o VSCode](https://code.visualstudio.com/download)- Link direto para download
* [Documentação oficial do pacote uv](https://docs.astral.sh/uv/) - Você saberá todos os detalhes sobre o `uv` e como ele é importante no python
* [venv — Criação de ambientes virtuais](https://docs.python.org/pt-br/3/library/venv.html) - Explicação completa de como funcionam os venvs
* [Conjunto de ícones de modelos de IA/LLM](https://lobehub.com/pt-BR/icons) - site muito bom para conseguir ícones do ecossistema de IA
* [Devicon](https://devicon.dev/) - site bem completo também com ícones gerais sobre tecnologia
* [Smolagents](https://github.com/huggingface/smolagents) - documenttação oficial da biblioteca smolagents
* [Como baixar o Antigravity](https://antigravity.google/download) - Página oficial de download da IDE do Google DeepMind
* [LLM as a Judge (Paper)](https://arxiv.org/abs/2306.05685) - Explicação técnica sobre o conceito de usar LLMs para avaliar outros modelos ("Judging LLM-as-a-Judge")

## Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorar este projeto, sinta-se à vontade para fazer um fork do repositório.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/marioluciofjr/mcp_news/blob/main/LICENSE) para detalhes.

## Contato
    
Mário Lúcio - Prazo Certo®
<div>  	
  <a href="https://www.linkedin.com/in/marioluciofjr" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
  <a href = "mailto:marioluciofjr@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://prazocerto.me/contato" target="_blank"><img src="https://img.shields.io/badge/prazocerto.me/contato-230023?style=for-the-badge&logo=wordpress&logoColor=white"></a>
</div> 

