
## **Bot Discord "Jornal Geral" - Projeto de Automação e Informações em Tempo Real**

### **Descrição Geral**
Este projeto consiste na criação de um bot para o Discord, desenvolvido para buscar e compartilhar notícias em tempo real, além de responder a comandos personalizados. Ele foi projetado com foco em automação, integração com APIs e boas práticas de desenvolvimento colaborativo.  

### **Funcionalidades Principais**
1. **Busca de Notícias Personalizada (`/j`)**  
   - O bot permite buscar notícias com base em termos fornecidos pelo usuário.  
   - Integração com a API da SerpAPI para buscar resultados de notícias mais recentes.  
   - Filtragem de notícias já enviadas para evitar duplicatas.  
   - Armazenamento local das notícias enviadas em um arquivo JSON.  

2. **Verificação Automática de Notícias**  
   - A cada 10 minutos, o bot busca automaticamente por notícias relacionadas a termos predefinidos.  
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
