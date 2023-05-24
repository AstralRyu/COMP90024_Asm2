docker run -d --name=grafana -p 3000:3000 \
--restart=always \
-e "GF_PANELS_DISABLE_SANITIZE_HTML=true" \
grafana/grafana