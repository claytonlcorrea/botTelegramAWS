from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters
import boto3
from dotenv import load_dotenv
import os

# AWS
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
REGION = '' # adicione sua regiao, ex: sa-east-1
INSTANCE_ID = ['', ''] # Aqui você pode adicionar uma lista de ids de maquinas caso queira gerenciar mais de uma ex: i-xxxxxx ...
 

# Inicializando cliente boto3
ec2 = boto3.client(
    'ec2',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION
)

# Função para reiniciar a instância
async def reset_instance(update: Update, context: CallbackContext):
    try:
        for instance in INSTANCE_ID:
            ec2.reboot_instances(InstanceIds=[instance])
            await update.message.reply_text("Instância EC2 foi reiniciada com sucesso!")
            print(f'Instância EC2 {instance} foi reiniciada com sucesso!') # Aparecerá apenas no terminal
    except Exception as e:
        await update.message.reply_text(f"Erro ao reiniciar a instância: {e}")
        print(f"Erro ao reiniciar a instância: {e}")
        

# Função para comando /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Bem-vindo ao bot de gerenciamento EC2!"
        "- /start: Exibe esta mensagem de boas-vindas.\n"
        "- /reiniciar: Reinicia a instância EC2."
    )

# Função para lidar com mensagens não reconhecidas
async def unknown_message(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Desculpe, eu não entendi sua mensagem. Aqui estão as opções disponíveis:\n"
        "- /start: Exibe esta mensagem de boas-vindas.\n"
        "- /reiniciar: Reinicia a instância EC2."
    )

# Configuração do bot
TOKEN = '' #token gerado no botFather


def main():
    # Inicializando o bot com o Application
    application = Application.builder().token(TOKEN).build()

    # Adicionando comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("reiniciar", reset_instance))

    # Captura de mensagens desconhecidas
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))

    # Iniciando o bot
    application.run_polling()

if __name__ == '__main__':
    print('rodando ...')
    main()