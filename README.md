# GenAI powered Jira Task Change interactor

This README provides comprehensive instructions on how to set up and use the Kafka producer script, including handling Kafka and Zookeeper using Docker and creating the necessary Kafka topic. This should guide users through setting up their environment and running the script effectively.


This Python script simulates Jira task, project, and resource changes by reading from CSV files and producing messages to a Kafka topic named `jira-changes`.

## Requirements

- Python 3.6+
- pandas
- kafka-python

## Setup

1. Ensure Kafka and Zookeeper are running. The Kafka topic `jira-changes` should be created and configured to listen on localhost:9092.
2. Install required Python packages:
   ```bash
   pip3 install -r requriements.txt
