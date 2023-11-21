###########
# BUILDER #
###########

FROM node:latest AS builder

WORKDIR /app

COPY Interface_Calloux .

RUN npm install -g npm@latest && npm install && npm run build

#########
# FINAL #
#########

# nginx state for serving content
FROM nginx:latest
# Set working directory to nginx asset directory
WORKDIR /usr/share/nginx/html
# Remove default nginx static assets
RUN rm -rf ./*
EXPOSE 5173
# Copy static assets from builder stage
COPY --from=builder /app/dist .
# Containers run nginx with global directives and daemon off
ENTRYPOINT ["nginx", "-g", "daemon off;"]
