EC2 Management Bot - Telegram Integration
Um bot desenvolvido em Python para gerenciar instâncias EC2 da AWS via Telegram. Este projeto utiliza a API do Telegram e a AWS SDK (boto3) para fornecer comandos simples, como reiniciar instâncias específicas, diretamente através de mensagens no Telegram.

Funcionalidades
Reinício de múltiplas instâncias EC2 de forma assíncrona.
Respostas claras e diretas no Telegram, indicando o sucesso ou falha das operações.
Mensagens personalizadas para guiar o usuário nas opções disponíveis.
Arquivo .env para gerenciamento seguro das credenciais e configurações sensíveis.
Tecnologias Utilizadas
Python: Linguagem principal do projeto.
boto3: Biblioteca da AWS para gerenciar instâncias EC2.
python-telegram-bot: Biblioteca para integração com a API do Telegram.
python-dotenv: Para carregar variáveis de ambiente do arquivo .env.
Como Configurar
Clone o repositório:
bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências:
bash
Copiar código
pip install -r requirements.txt
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
makefile
Copiar código
AWS_ACCESS_KEY=seu_access_key
AWS_SECRET_KEY=sua_secret_key
TOKEN=seu_token_telegram
Execute o bot:
bash
Copiar código
python nome_do_script.py
Como Usar
Inicie o bot no Telegram com o comando /start.
Reinicie as instâncias EC2 com o comando /reiniciar.
Caso o comando seja inválido, o bot orientará com as opções disponíveis.
