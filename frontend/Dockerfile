# Minimal Dockerfile for React frontend
FROM node:20
WORKDIR /app
COPY package.json ./
RUN yarn install --frozen-lockfile
COPY . .
RUN yarn build
RUN yarn global add serve
EXPOSE 3000
CMD ["serve", "-s", "dist", "-l", "3000"]
