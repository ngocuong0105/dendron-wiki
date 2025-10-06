---
id: 03gbxiq9kwvv3tq2zpwbjjo
title: S3 vs DL vs Redshift
desc: ''
updated: 1759739942457
created: 1753101111100
---
# S3 (Simple Storage Service)

- pure storage, no SQL or any analytics
- **Object** Storage. **NOT** columnar, log-structured(LSM), or B-trees
- S3 does not understand tables, rows, columns, indexes, or trees.
- All structuring is defined by how you write/read files (e.g., CSV, Parquet, JSON), not by S3 itself!
- stores objects within buckets
- an object is a file and any metadata that describes the file
- a bucket is a container for objects


# DataLake
- Still Object Storage (in S3)
- Built on top of S3
- An architectural concept or solution—not a product or "service".
- Centralizes and organizes data (usually on S3)
- in AWS you will go to S3 service and you will have many buckets. Some buckets might be data lakes
- DLs often support query tools (Athena/Databricks) for direct analytics!

## Note on S3/DL storage

- DL and S3 are object storages. The objects (files) within might have structure, for example columnar format like **Parquet, Avro** and you can define schema on them.
- **But:** The underlying object store (S3) remains ignorant of the structure; it just stores files. The columnar "magic" happens inside the files themselves.
- you can not have B-trees, LSM-tree storage indexing in S3/DL - you need to use full fledged database management system. 

# Redshift
- Amazon Redshift is a fully managed cloud **data warehouse** service 
- It is not just storage - it is a ful featured SQL analytics database
- **Columnar Storage:**
    - Redshift stores table data in a columnar format (not row-based, not LSM, not B-tree).
    - This means data is stored column by column, which is highly efficient for analytical queries (scanning/aggregating specific columns in very large datasets).

See [[engineering.AWS.How does Yelp store data?]] or practical usage

## Note on parquet vs csv
- parquet files are columnar, meaning they store data in columns rather than rows.
- This is different from CSV files, which are row-based.


# Bottom line

- S3 = object storage, NO index/tree, NO enforced schema, NO columnar unless your files are.
- Data Lake = organization + schema/catalog on S3; columnar if files are (e.g., Parquet); NO B-tree/LSM tree.
- Databases (like Redshift) = implement B-trees/columnar engines internally as part of their design for querying rows and columns efficiently.


# Pricing

**Data Lake**
- Athena and Spark charge based on the amount of **data scanned**, so inefficient queries or large raw datasets can quickly increase costs.
- No infrastructure to manage: You don’t pay for servers or clusters—just for the queries you run.
- Best for
    - Ad hoc queries
    - Infrequent or unpredictable workloads


**Redshift**
- Provisioned clusters: Pay for reserved compute/storage capacity (hourly, regardless of usage). OR
    - Yelp has 4 clusters!!
- Serverless: Pay for compute seconds used per query, plus storage.
- Best for:
    - Frequent, complex analytics
    - Large-scale, repeated reporting
    - BI dashboards and heavy workloads


# HDFS

Hadoop Distributed File System. Like S3 it is used to store large amounts of data.

- Distributed file system that runs on lusters of computers
- Data stored in HDFS can be of any type, but the system automatically splits these files and stores them redundantly across many machines
- HDFS is faster than S3 (no network latency)
- HDFS is a distributed file system you run and maintain on your own cluster, primarily for on-prem or managed Hadoop/Spark environments.

- S3 is not a file system, it is object storage. S3 is a manged service by AWS. HDFS is open source and you have to manage it yourself. It runs on a cluster of connected servers.

- Legacy/On-prem-focused orgs: More likely to use HDFS.
- Cloud/data-driven orgs (most modern tech): Strongly favor S3.