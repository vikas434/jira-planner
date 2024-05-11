import pandas as pd
from kafka import KafkaProducer
import json

def produce_messages():
    # Initialize Kafka producer
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    # Load CSV data
    projects_df = pd.read_csv('Projects.csv')
    tasks_df = pd.read_csv('Tasks.csv')
    resources_df = pd.read_csv('Resources.csv')

    # Simulate sending project data
    for _, project in projects_df.iterrows():
        message = {'type': 'project', 'data': project.to_dict()}
        producer.send('jira-changes', message)
        print(f"Sent: {message}")

    # Simulate sending task data
    for _, task in tasks_df.iterrows():
        message = {'type': 'task', 'data': task.to_dict()}
        producer.send('jira-changes', message)
        print(f"Sent: {message}")

    # Simulate sending resource data
    for _, resource in resources_df.iterrows():
        message = {'type': 'resource', 'data': resource.to_dict()}
        producer.send('jira-changes', message)
        print(f"Sent: {message}")

    producer.flush()

if __name__ == '__main__':
    produce_messages()
