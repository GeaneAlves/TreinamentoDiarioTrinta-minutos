import logging
from logging.handlers import RotatingFileHandler
import time

#1 configuração do Rotacionador de Logs
# maxbytes=500: o arquivo de log será rotacionado quando atingir 500 bytes
# backupCount=3: manter até 3 arquivos de log antigos
handler_rotativo = RotatingFileHandler(
    filename='app_profissional.log',
    maxBytes=500,
    backupCount=3,
    encoding='utf-8'
)
#Definindo a formatação dos logs (Data | Nível | Mensagem)
formatacao = logging.Formatter('$asctime)s | %(levelname)s | %(message)s')
handler_rotativo.setFormatter(formatacao)

#3Criando o logger e adicionando o handler rotativo
logger = logging.getLogger('logger_rotativo')
logger.setLevel(logging.INFO)
logger.addHandler(handler_rotativo)

print("Iniciando geração massiva de logs...")

#4 Loop para forçar a criação de múltiplos arquivos de log
#Vamos gerar 100 mensagens de log. Como o limite é 500 bytes, isso deve criar vários arquivos de log.
# Isso vai obrigar o Python a criar vários arquivos de log rotacionados.
for i in range(1, 21):
    mensagem = f"Esta é a mensagem de log número {i} - enchendo o arquivo..."
    logger.info(mensagem)
    print(f"Gerando log {i}...")
    time.sleep(0.1) # Pequena pausa para simular tempo entre logs e para não travar

print("\nProcesso concluído! Verifique a pasta do script.")
