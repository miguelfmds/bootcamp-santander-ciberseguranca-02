# Verificação de Integridade de Arquivos com Hashes
 
# Solução Padrão

def verificar_hashes(lista_hashes):
  
    for hash_comparacao in lista_hashes:
        
        hash_calculado, hash_esperado = hash_comparacao.split(",")
        
        # TODO: Verifique se o hash calculado é igual ao hash esperado:
        if hash_calculado.strip() == hash_esperado.strip():
            comparacao = 'Correto'
        else:
            comparacao = 'Inválido'
        
        print(comparacao)
            
hashes_usuario = input()

lista_hashes = hashes_usuario.split(";")
    
verificar_hashes(lista_hashes)

# Pontos de Melhorias

def verificar_hashes(lista_hashes):
  
    for hash_comparacao in lista_hashes:
        
        hash_calculado, hash_esperado = hash_comparacao.split(",")
        
        # TODO: Verifique se o hash calculado é igual ao hash esperado:
        print('Correto' if hash_calculado == hash_esperado else 'Inválido')
            
        
hashes_usuario = input().replace(" ", "") # Remover os espaços em branco
    
verificar_hashes( hashes_usuario.split(";") )
