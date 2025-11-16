---
id: vl59xstqw0sfbuhf9vthk7n
title: Data Storage
desc: ''
updated: 1762334984734
created: 1761560874708
---
When you build a data infrastructure system you will consider tradeoffs between cost, efficiency, pattern accessability (online va offline, key:value pair vs relational), volume.

# Data Storage Technologies

AWS has S3 (e.g DataLake), Redshift, MySQL, Cassandra, ElasticSearch.


## S3
AWS service. Cloud storage. Structured (csv, parquet, csv) and Unstructured (images,videos, documents, parquets) data

- Offline availability
- Best for logs, historical data, backup - the defacto option for archives
- Benefits: extremely low $ cost, essentially infinite storage capacity, scales horizontally
- Disadvantages: no built-in query. Need to load it in some other data store to work with the data
- S3 is basically a filesystem (buckets instead of folders)

Can query using additional services like Athena, or you load in spark.

## Datalake
AWS service. Claud storage. Built on top of S3. Structured and Unstructured data. Allows to query data using ATHENA (SQL quering engine for S3)

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

## HDF5

Susquehanna uses this.

- 


# Data Catalog

This is a catalog service =  metadata layer that describes data not the data itself.

Data catalog technologies offer another layer of abstraction on top of data storage technologies. They help you discover, manage and govern your data assets. 

## AWS Glue
AWS Glue is a centralized metadata catalog that allows:
- schema management, track schema versions, schema evolution, register schemas.
- metadata management - catalog of what data exists and where
- data discovery layer - search and discover datasets, and querable by downstream engines.


## Apache Iceberg

Apache is a open source foundation project. Iceberg is a table format for huge analytic datasets. It is designed to improve on the limitations of other table formats like Hive.

Iceberg is supported in AWS. You can create Iceberg tables. For example in CAPI you had to migrate from normal tables in DataLave v1 to DataLake v2 (these are Yelp related datalakes). DLv2 uses Iceberg table format. It allows you to have:
- ACID transactions (marketing)
- Time travel and rollback via its integrated snapshots tooling.
- Multi-partioned tables (dt=2024-01-01/client_id=sephora). More control over partitioning strategies. When you run a backfill you could select which data to change based on partition filters.
- No need for physical deletes (use DELETE statements that mark data as deleted without physically removing it right away)
- tracks schema evolution

Multipartitioning: 
- isolation whenever you insert/update/delete data. Before updating data for one client meant you need to rerun for all.
- 

### Yelp DLv1 to DLv2

Since 2017 Yelp's data lake has used the Hive table format. Since then, Apache Iceberg has gained significant adoption in the industry -- proving to be Hive's successor -- and brings many enhancements.

Like Hive, Iceberg stores Parquet files in S3 and metadata in AWS Glue. Iceberg tables exist in the AWS Glue catalog and work with Spark, Athena, and Redshift just as Hive tables do, but with extra features.

[ICEBERG Tech Spec](https://iceberg.apache.org/spec/#version-1-analytic-data-tables)


One of Iceberg's design goals is to present a data lake table that works as a SQL table does without any surprises, so is not required to know these concepts, however some Iceberg users may be curious to understand them.

Iceberg metadata is stored in a tree structure. The image below may look complicated at first glance, but users of Iceberg do not need to understand it in order to use an Iceberg table.



#### ACID transactions

Hive tables have many areas of undefined behavior which introduce data inconsistencies and data quality issues, especially when multiple processes are reading and writing to a table. Iceberg's provides ACID transactions and guarantees about behaviors for reads and writes.

Iceberg's tables store the S3 path of the current metadata on the Glue table as a table property. This is the basis for the below behaviors.

- Atomic Operations: Data files are added or removed in a single, complete operation, ensuring that writes are never partially visible. Iceberg writes data to S3 and commits changes by updating a metadata reference in the Glue table, which supports atomic updates.

- Consistency & Isolation: Iceberg provides optimistic concurrency and serializable isolation. Readers only access commited data and will see a consistent and correct view of data even while a writer concurrently commits to the table. Serializable isolation ensures that multiple writers will not introduce inconsistent states by ensuring that only one process writes to a table at a time. In some cases serializable isolation can impede workflows, see Iceberg Known Issues and Limitations for alternatives (parallel backfills can be tricky).

-Durable: Once a transaction is committed, it will not be lost. Durability is provided by S3 similarly to Hive tables. 


# HDF5

SIG uses this data format (`.hdf5`). Another technology to manage data.
- HDF5 is a data software library, data management service and storage forhererogeneous data. Built in with fast "I/O" processing.
- storing scientific numerical data

What is HDF5?
- A file specification and associated data model
- A standard library with API access for C++, Python, Java, etc.
- A software ecosystem consisting of client applications using HDF5 and analysis platforms like MATLAB, Python
