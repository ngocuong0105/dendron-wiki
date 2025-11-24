
# Latency vs Throughput

Throughput is measured in transactions per second (TPS) or requests per second RPS . It is the amount of information processed, transmitted or stored in a given amount of time.

Latency is measured in milliseconds . It is time it takes a single piece of data to travel from source to destination.

High throughput means the system can handle multiple data at the same time. Low latency means that system can handle single data quickly.


**High Throughput, Acceptable Latency**: Batch processing systems (e.g., data ingestion systems) where large volumes of data are processed together, and immediate response is not critical.  

**Low Latency, Acceptable Throughput**: Real-time applications (e.g., video conferencing) where rapid responses are more important than processing high volumes of data consistently.