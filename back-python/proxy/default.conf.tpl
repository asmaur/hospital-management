
upstream sistemia{
    server web:${APP_PORT};
}

server {
    listen ${LISTEN_PORT};


    location /static {
        alias /vol/static; 
    }

    location / {
        proxy_pass  http://sistemia;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;    
        client_max_body_size    10M;
    }
}