import imaplib
import email
import logging
from email.header import decode_header
from logging.handlers import RotatingFileHandler

#Configurações
EMAIL_USER  = "geanedarc2@gmail.com"
EMAIL_PASS = "pjwf hjbb kgij jsul "

#O que buscar?
REMETENTE = "Imovelweb" 
DATA_INICIO =  "01-Nov-2025"
DATA_FIM = "01-Dec-2025"        # Dica: Coloque o dia 1º do mês SEGUINTE para pegar o mês anterior completo (Nov inteiro).


#   Nome da pasta da lixeira no Gmail (Pode ser '[Gmail]/Trash' ou '[Gmail]/Bin')
PASTA_LIXEIRA = '[Gmail]/Lixeira'

# 1. Configuração de logs
handler = RotatingFileHandler('faxina_email.log', maxBytes=5_000_000, backupCount=3, encoding='utf-8')
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s',datefmt='%d/%m/%y %H:%M:%S')
handler.setFormatter(formatter)

logger = logging.getLogger('FaxinaGmail')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Adiciona log também na tela (Console) para você acompanhar ao vivo
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)

def conectar_gmail():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL_USER, EMAIL_PASS)
        logger.info(f"Conectado com sucesso à conta: [EMAIL_USER]") 
        return mail
    except Exception as e:
        logger.error(f"Falha na conexão: {e}")
        return None

def mover_para_lixeira(mail, email_ids):
    if not email_ids:
        logger.warning("Nenhum email encontrado com os critérios")
        return
    
    logger.info(f"Iniciando remoção de {len(email_ids)} e-mails...")

    contador = 0
    for e_id in email_ids:
        try:
            # 1. Copia para a Lixeira (Segurança do Gmail
            res, _ = mail.copy(e_id, PASTA_LIXEIRA)
            if res == 'OK':
                # 2. Marca como Deletado na Caixa de Entrada original
                mail.store(e_id, '+FLAGS', '\\Deleted')
                contador += 1
                if contador % 10 == 0:
                    logger.info(f"Precessados {contador}/{len(email_ids)}...")
            else:
                logger.error(f"Erro ao mover ID {e_id.decode()}")
        except Exception as e:
            logger.error(f"Erro crítico no e-mail ID {e_id}: {e}")

    # Efetiva a deleção na pasta original
    mail.expunge()
    logger.info(f"SUCESSO: {contador} e-mails movidos para a Lixeira.")

def main():
    mail = conectar_gmail()
    if not mail: return

    try:
        mail.select("INBOX")        #seleciona a caixa de entrada

    # Critério de busca IMAP:
    # FROM "nome" SINCE data BEFORE data
        criterio = f'FROM "{REMETENTE}" SINCE "{DATA_INICIO}" BEFORE "{DATA_FIM}"'

        logger.info(f"Buscando e-mails com critério: {criterio}")
        status, messages = mail.search(None, criterio)

        if status == "OK":
        # Converte a resposta em uma lista de IDs
            email_ids = messages[0].split()
            logger.info(F"Encontrados {len(email_ids)} e-mails de {REMETENTE}.")

            if len(email_ids) > 0:
        # Pergunta de segurança (Opcional - remova se quiser 100% automático)
                confirmacao = input(f"Confirma mover {len(email_ids)} e-mails para a Lixeira? (s/n): ")
                if confirmacao.lower() == 's':
                    mover_para_lixeira(mail, email_ids)
                else:
                    logger.info("Operação cancelada pelo usuário.")
            else:
                logger.info("Nada a fazer, tudo limpo!")
        else:
            logger.error("Erro na busca pelos e-mails.")

    except Exception as e:
        logger.error(f"Erro geral no script> {e}")
    finally:
        mail.logout()
        logger.info("Conexão encerrada.")

if __name__ == "__main__":
    main()