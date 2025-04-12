---
id: 0xdj2eqmnrxdhq7a3oment4
title: S3 Redshift MySQL
desc: ''
updated: 1744376387254
created: 1744368322753
---

When you build a data infrastructure system you will consider tradeoffs between cost, efficiency, pattern accessability (online va offline, key:value pair vs relational), volume.


# Technologies

AWS has S3 (e.g DataLake), Redshift, MySQL, Cassandra, ElasticSearch

## S3
AWS service. Cloud storage. Structured (csv, parquet, csv) and Unstructured (images,videos, documents, parquets) data

- Offline availability
- Best for logs, historical data, backup - the defacto option for archives
- Benefits: extremely low $ cost, essentially infinite storage capacity, scales horizontally
- Disadvantages: no built-in query. Need to load it in some other data store to work with the data
- S3 is basically a filesystem (buckets instead of folders)

Can query using additional services like Athena, or you load in spark.


## Redshift

AWS service. Columnar data storage, fully manged data warehouse service. Relational db design. Structured data only (tables schemas)

Stores data in clusters.

- Offline availability
- Best for analytics, data exploration and analysis
- Benefits: good options for doing expensive joins. SQL based quering.
- Disadvantages: high cost



## MySQL

Relational database. Used for structured data and transactions, such as user profiles and reviews. Transaction is a row/tuple in sQL table.

- Offline and Online (e.g when Yelp user searches something/ send a message it is directly stored and accessed) availability 
- ACID compliance provides strongest form of data reliability


## Casandra

## ElasticSearch