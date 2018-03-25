for ((i=1;i<=100;i++)); do   curl -v --header "Connection: keep-alive" "http://10.0.12.128/temp"; done
for ((i=1;i<=100;i++)); do   curl -v --header "Connection: keep-alive" "http://10.0.12.128/humidity"; done

