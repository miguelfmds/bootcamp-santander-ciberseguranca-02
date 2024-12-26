<h1>
    <a href="https://web.dio.me/track/santander-ciberseguranca-2024/">
     <img align="center" width="100px" src="https://assets.dio.me/mXe9Ce9ajHOrzggSjtSD7fubZXjG3zEZs_X8r9xJ9jg/f:webp/h:120/q:80/L3RyYWNrcy9mODRlOWQxZS04ZWQ1LTQ2ZjctYjlhMC1kY2Y1YTAzOTZmMzMucG5n"></a>
    <span> Detecção de Tentativas de Invasão em Logs</span>
</h1>

# Desafio: 
Você é responsável por implementar um sistema de monitoramento de segurança para um sistema de acesso. Seu objetivo é analisar registros de log de tentativas de acesso para detectar possíveis invasões. Cada registro contém um identificador de usuário e um status que indica se a tentativa de acesso foi bem-sucedida ou falhou.

A detecção de tentativas de invasão é essencial para a segurança do sistema, e a análise de logs é uma prática comum para identificar comportamentos suspeitos. O sistema deve emitir um alerta se detectar mais de 3 tentativas consecutivas de falha para o mesmo usuário.

## Instruções:
Entrada: Uma lista de registros de log no formato id_usuario:status, onde:

id_usuario é uma string que representa o identificador do usuário (exemplo: "user1").

status pode ser uma das seguintes strings:
- "sucesso" – indica que a tentativa de acesso foi bem-sucedida.
- "falha" – indica que a tentativa de acesso falhou.

A lista pode conter qualquer número de registros.

Saída: O sistema deve retornar:

O id_usuario que teve mais de 3 tentativas consecutivas de falha.

Se nenhum usuário tiver mais de 3 tentativas de falha consecutivas, o sistema deve retornar a mensagem "Nenhum invasor detectado".
