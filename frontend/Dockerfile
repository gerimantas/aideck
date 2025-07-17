# Minimal Dockerfile for React frontend
FROM node:20-alpine
WORKDIR /app
COPY . /app
RUN npm install --legacy-peer-deps && npm install -g vite && npm run build
EXPOSE 3000
CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0"]
