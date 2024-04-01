# Use uma imagem oficial do Node.js como imagem base
FROM node:14

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo package.json e package-lock.json para o diretório de trabalho
COPY package*.json ./

# Instale as dependências da aplicação
RUN npm install

# Copie o restante do código-fonte da aplicação
COPY . .

# Exponha a porta 3000 para fora do contêiner
EXPOSE 3000

# Defina o comando padrão a ser executado quando o contêiner for iniciado
CMD ["npm", "start"]
