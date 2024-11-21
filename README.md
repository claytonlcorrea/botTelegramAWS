# EC2 Management Telegram Bot

Um bot desenvolvido em Python para gerenciar instâncias EC2 da AWS via Telegram. Este projeto utiliza a API do Telegram e a AWS SDK (boto3) para fornecer comandos simples, como reiniciar instâncias específicas, diretamente através de mensagens no Telegram.

## Funcionalidades
- Reinício de múltiplas instâncias EC2 de forma assíncrona.
- Respostas claras e diretas no Telegram, indicando o sucesso ou falha das operações.
- Mensagens personalizadas para guiar o usuário nas opções disponíveis.
- Arquivo `.env` para gerenciamento seguro das credenciais e configurações sensíveis.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **boto3**: Biblioteca da AWS para gerenciar instâncias EC2.
- **python-telegram-bot**: Biblioteca para integração com a API do Telegram.
- **python-dotenv**: Para carregar variáveis de ambiente do arquivo `.env`.

## Como Configurar
1. Clone o repositório:
   ```bash
   https://github.com/claytonlcorrea/botTelegramAWS.git

2. instalar dependencias:
   ```bash
   pip install -r requirements.txt

3. Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
  ```bash
   AWS_ACCESS_KEY=seu_access_key
   AWS_SECRET_KEY=sua_secret_key
   TOKEN=seu_token_telegram

