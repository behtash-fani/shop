FROM nginx:latest


COPY  nginx.conf /etc/nginx/conf.d/default.config
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]