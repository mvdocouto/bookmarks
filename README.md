# Sistema de Gerenciamento de Bookmarks

## Sobre o projeto

Sistema de gerenciamento de bookmarks. Cada usuário pode cadastrar seus bookmarks e consulta-los de maneira facil.
O sistema possui dois niveis de usuarios:
- Administrador: Visualiza os bookmarks de todos os usuários.
- User: Somente gerencia os seus bookmarks. 

O sistema foi dividido em dois módulos:
- API Rest: Desenvolvida em node.js utilizando o framework Express
- API Client: Desenvolvida em Python + Flask utilizando o Twitter Bootstrap no desenvolvimento do layout.


## API Rest

### Instalação

Para instalar o projeto basta clonar o repositorio acessar o diretorio **api-rest** e intalar as dependencias do node com o npm.
```shell
npm install
npm start
```

### Configuração Inicial

Inicialmento o banco de dados não possui nenhum usuário. Será necessário inserir um usuário administrador. Para inserir um usuário administrador do sistema utilize o seguinte comando:
```shell
curl --request POST --url http://localhost:5000/users/ --header 'content-type: application/json' --data '{"name": "adm","email": "adm@adm.com", "password": "adm", "permission": "true"}'
```

### Testes

Os teste foram feitos ultilizando a suite de testes mocha. Para rodar os testes basta rodar o seguinte comando:

```shell
npm test
```

### Docker


## API Client 
