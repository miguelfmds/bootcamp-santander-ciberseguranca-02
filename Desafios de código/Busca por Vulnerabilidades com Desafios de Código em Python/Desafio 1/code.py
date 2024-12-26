# Detecção de Phishing por Padrões de E-mail

# Solução Padrão

def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click",  "promoção"]
    
    # TODO: Verifique se alguma palavra suspeita está presente no corpo do e-mail:
    analise = 'Seguro'
    for palavra in mensagem:
        palavra = ''.join(letra for letra in palavra if letra.isalnum()) # remover caracteres especiais
        if palavra.lower() in palavras_suspeitas: # letras minúsculas
            analise = 'Phishing'
            break
    return analise
        
email_usuario = input()

email_usuario = email_usuario.split() # Definir uma lista de palavras

resultado = verificar_phishing(email_usuario)

print(f"Classificação: {resultado}")
