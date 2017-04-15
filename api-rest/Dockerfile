# Usando a ultima imagem do node
FROM node:lasted

# Creiando o diretorio do APP
RUN mkdir -p /usr/src/app
WORKDIR /user/src/app

# Instalando as dependencias
COPY package.json /usr/src/app/
RUN npm install
RUN npm install -g babel-cli

# Copiando o aplicativo
COPY . /usr/src/app

# Liberando o acesso a porta 5000
EXPOSE 5000

# Iniciando o APP
CMD ["npm", "start"]