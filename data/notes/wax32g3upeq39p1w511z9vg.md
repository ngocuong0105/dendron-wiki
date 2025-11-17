
Legendary book about building scalable data systems.
- Chapters 1-4 are a must read.
- Chapter 1 defines what system characteristics we care about: scalability, reliability, maintainability.
- Chapter 2 discusses data models and query languages - from user's perspective how do you work with data.
- Chapter 3 discusses storage and retrieval - how data is stored on disk, B+ trees, LSM trees - from DB-engineer's perspective. DB has two jobs to store data and to return data when queried.
- Chapter 4 discusses encoding and evolution - how data is encoded on disk, serialization formats (JSON, XML, Protobuf, Avro, Thrift), schema evolution. This is about data representation on a computer.
- Part II is about distributed data (a bit harder to read). Chapter 7 is worth reading to understand what transactions are (ACID, where the 'C' is not related to transactions..)
- Chapter 5& 6 are about replication and partitioning and are ok. Chapter 8-9 not worth so much (or at least I'm not at the stage where I could understand and relate to them).
- Chapter 10 about batch processing is great. Starts from Unix batch, explain MapReduce and all this will help you understand the internals of Spark.
