# Script de Upload de Arquivos de Replay para Ballchasing.com

Este script em Python permite o upload automático de arquivos de replay do Rocket League para o Ballchasing.com. Ele verifica se o API do Ballchasing.com está acessível e, em seguida, itera sobre todos os arquivos .replay em uma determinada pasta para fazer o upload de cada um deles. 

## Requisitos

- Python 3.x
- Biblioteca requests

## Configuração

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Instale a biblioteca requests executando o seguinte comando:
  pip install requests
3. Edite o script e defina as seguintes variáveis:
- `folder_path`: Caminho da pasta onde os arquivos .replay estão localizados.
- `auth_token`: Token de autorização da API fornecido pelo Ballchasing.com.

## Utilização

1. Execute o script fornecendo as configurações adequadas.
2. O script verificará a acessibilidade da API do Ballchasing.com e imprimirá o status.
3. Em seguida, percorrerá cada arquivo .replay na pasta especificada e fará o upload de cada um.
4. O resultado de cada upload será exibido no console.
5. Os arquivos que forem carregados com sucesso serão adicionados a uma lista de arquivos já enviados.
6. A lista de arquivos já enviados será armazenada no arquivo `uploaded_files.txt` para evitar uploads repetidos no futuro.

## Observações

- O script trata os códigos de status 200, 201 e 409 como uploads bem-sucedidos. O código 409 indica que o arquivo já foi enviado anteriormente.
- Certifique-se de ter permissão para acessar os arquivos de replay na pasta especificada.
- Certifique-se de fornecer um token de autorização válido fornecido pelo Ballchasing.com.
