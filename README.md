docker exec -it <container_name_or_id> kafka-topics.sh --create --topic jira-changes --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

docker exec -it 066f870538a9 kafka-topics.sh --create --topic jira-changes --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
