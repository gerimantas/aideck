# Frontend Dockerfile for AIDECK
FROM node:20
WORKDIR /app
COPY package.json ./
RUN yarn install --frozen-lockfile
COPY . .
RUN yarn build
RUN yarn global add serve
CMD ["serve", "-s", "dist", "-l", "3000"]
