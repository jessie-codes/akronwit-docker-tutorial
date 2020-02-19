FROM node:12

EXPOSE 3000
WORKDIR /app
COPY . .
RUN npm ci
CMD ["node", "index.js"]