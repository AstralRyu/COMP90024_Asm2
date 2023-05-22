docker run -d --name=grafana -p 3000:3000 \
--restart=always \
-v /home/ubuntu/grafana/grafana.ini:/etc/grafana/grafana.ini \
-e "GF_PANELS_DISABLE_SANITIZE_HTML=true" \
grafana/grafana