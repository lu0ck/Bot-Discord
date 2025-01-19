
# In English:

## **Discord Bot "Jornal Geral" - Real-Time News and Automation Project**

This project involves the creation of a Discord bot designed to fetch and share news in real-time, as well as respond to custom commands. It was designed with a focus on automation, API integration, and best practices for collaborative development.

### **Main Features**
1.  **Custom News Search (`/j`)**
    -   The bot allows searching for news based on terms provided by the user.
    -   Integration with the SerpAPI to fetch the latest news results.
    -   Filtering of already sent news to avoid duplicates.
    -   Local storage of sent news in a JSON file.

2.  **Automatic News Checking**
    -   Every 120 minutes, the bot automatically searches for news related to predefined terms.
    -   Relevant news is sent directly to a specific Discord channel.

3.  **Persistent Data Management**
    -   Local storage using JSON to save and retrieve links of sent news.

4.  **Use of Secure Settings**
    -   Sensitive variables, such as the bot token and API key, are managed using a `.env` file, ensuring security and avoiding exposure in the code.

### **Technologies Used**
-   **Python**: Main language of the project.
-   **Python Libraries**:
    -   `discord.py`: For interactions with Discord.
    -   `requests`: For HTTP calls to the news API.
    -   `dotenv`: For loading environment variables.
-   **Git and GitHub**: For code versioning and collaboration.
-   **Railway**: For hosting and continuous execution of the bot in the cloud.
-   **JSON**: For local management of persistent data.

### **Development Workflow**
1.  **Environment Setup**
    -   Configured a virtual environment in Python to manage dependencies.
    -   Created a `requirements.txt` file to facilitate the installation of libraries.

2.  **Integration with the SerpAPI**
    -   Configured API calls to fetch news based on keywords.
    -   Implemented filters to avoid content duplication.

3.  **Security and Best Practices**
    -   Sensitive variables were stored in a `.env` file and ignored by Git using `.gitignore`.
    -   Resolved merge conflicts in the remote repository after direct editing on GitHub.

4.  **Hosting on Railway**
    -   Configured a production environment on Railway.
    -   Added a custom startup command to run the bot automatically.

5.  **Bug Fixes and Testing**
    -   Debugged and fixed errors related to API configuration and bot behavior.
    -   Tested the commands on Discord to ensure that all functionalities were working correctly.

### **Learnings and Impact**
-   **Technical Learning**:
    -   Configuration of virtual environments and dependency management.
    -   API handling and integration with external systems.
    -   Project management with Git and conflict resolution.

-   **Project Impact**:
    -   The bot provided an automated way to access relevant news, facilitating real-time access to information for users of a Discord server.

---


# Em Português:

## **Bot Discord "Jornal Geral" - Projeto de Automação e Informações em Tempo Real**

Este projeto consiste na criação de um bot para o Discord, desenvolvido para buscar e compartilhar notícias em tempo real, além de responder a comandos personalizados. Ele foi projetado com foco em automação, integração com APIs e boas práticas de desenvolvimento colaborativo.  

### **Funcionalidades Principais**
1. **Busca de Notícias Personalizada (`/j`)**  
   - O bot permite buscar notícias com base em termos fornecidos pelo usuário.  
   - Integração com a API da SerpAPI para buscar resultados de notícias mais recentes.  
   - Filtragem de notícias já enviadas para evitar duplicatas.  
   - Armazenamento local das notícias enviadas em um arquivo JSON.  

2. **Verificação Automática de Notícias**  
   - A cada 120 minutos, o bot busca automaticamente por notícias relacionadas a termos predefinidos.  
   - Notícias relevantes são enviadas diretamente em um canal específico do Discord.  

3. **Gerenciamento de Dados Persistentes**  
   - Armazenamento local utilizando JSON para salvar e recuperar links de notícias enviados.  

4. **Uso de Configurações Seguras**  
   - Variáveis sensíveis, como o token do bot e a chave da API, são gerenciadas usando um arquivo `.env`, garantindo segurança e evitando exposição no código.  

### **Tecnologias Utilizadas**
- **Python**: Linguagem principal do projeto.  
- **Bibliotecas Python**:
  - `discord.py`: Para interações com o Discord.  
  - `requests`: Para chamadas HTTP à API de notícias.  
  - `dotenv`: Para carregamento de variáveis de ambiente.  
- **Git e GitHub**: Para versionamento do código e colaboração.  
- **Railway**: Para hospedagem e execução contínua do bot na nuvem.  
- **JSON**: Para gerenciamento local de dados persistentes.  

### **Fluxo de Desenvolvimento**
1. **Configuração do Ambiente**  
   - Configurei um ambiente virtual no Python para gerenciar dependências.  
   - Criei um arquivo `requirements.txt` para facilitar a instalação de bibliotecas.  

2. **Integração com a API da SerpAPI**  
   - Configurei chamadas à API para buscar notícias com base em palavras-chave.  
   - Implementei filtros para evitar duplicação de conteúdo.  

3. **Segurança e Boas Práticas**  
   - Variáveis sensíveis foram armazenadas em um arquivo `.env` e ignoradas pelo Git utilizando `.gitignore`.  
   - Resolvi conflitos de merge no repositório remoto após a edição direta no GitHub.  

4. **Hospedagem na Railway**  
   - Configurei um ambiente de produção na Railway.  
   - Adicionei um comando de inicialização customizado para executar o bot automaticamente.  

5. **Correção de Erros e Testes**  
   - Debuguei e corrigi erros relacionados à configuração da API e comportamento do bot.  
   - Testei os comandos no Discord para garantir que todas as funcionalidades estavam funcionando corretamente.  

### **Aprendizados e Impacto**
- **Aprendizado Técnico**:
  - Configuração de ambientes virtuais e gestão de dependências.  
  - Manipulação de APIs e integração com sistemas externos.  
  - Gerenciamento de projetos com Git e resolução de conflitos.  

- **Impacto do Projeto**:  
  - O bot trouxe uma forma automatizada de acessar notícias relevantes, facilitando o acesso à informação em tempo real para os usuários de um servidor do Discord.  

---
