FROM node:10


RUN npm install -g http-server

WORKDIR /usr/src/app/dict_front

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build


EXPOSE 8080

CMD [ "http-server", "dist" ]
