#!/bin/bash

SERVER_IP="127.0.0.1"
SERVER_PORT="8001"
SLEEP_TIME=10

get_cpu_usage() {
    top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}'
}

send_data() {
    local usage=$1
    local url="http://$SERVER_IP:$SERVER_PORT/application/"
    local data="{\"usage\": $usage}"

    curl -X POST -H "Content-Type: application/json" -d "$data" "$url"
}

while true; do
    usage=$(get_cpu_usage)
    send_data "$usage"
    sleep "$SLEEP_TIME"
done