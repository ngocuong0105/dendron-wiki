---
id: 0xdyjxuetx8at7o7eafrfzb
title: How does Yelp store data?
desc: ''
updated: 1676376255488
created: 1676375568620
---

# How does Amazon help us store data

We use two data storage tools:
- Amazon RedShift
- Amazon S3 (Data Lake)

Every second users from all over the world are using Yelp App or Website and generating data. Engineers wrote code to store event logs into S3 (Amazon Simple Storage Service). The data in S3 form a **data lake**.

S3 has a lot of pros:

Very cheap for storage
- Upon writing, there’s no schema required. Any format is accepted
- Upon reading, there’s no barrier between files / tables

But it also have some cons:
- Data quality is not guaranteed. It might require users to clean and write the schema for the data when reading the data. 
- It’s not the fastest 


Therefore, for the data that we have high usage, on a daily basis we clean the logs and write them into **Redshift**, where it is expensive to store but very fast and cheap to query. Redshift ensures the data schema is carefully designed before data is written. 

Problem is Redshift clusters are isolated with each other, you can’t join two tables in different Redshift clusters and drive insights. 


Solutions:

1. Let users load tables into a third place then join them. For example, we can use a jupyter notebook to run queries separately on different clusters, then join them together with pandas. - Very very slow
2. Add tables to the same cluster. - We do it sometimes, that’s why you see the same table in different clusters, but we can’t store all Yelp tables in one cluster, so this can’t completely solve the problem. Plus, this is very very expensive.
For example, in “ad-metrics” cluster, we have a table “ad-slot-metrics”, the same table is copied to “Bunsen” cluster, under “bunsen” folder, “ad_event” table
3. Copy data from Amazon Redshift to Amazon S3. (For example, you can find “ad metrics” in both Redshift and S3: )Then there are a few options:
- People can query the data lake with Amazon Athena. (Athena directly accesses data from S3 using SQL query.)
- People can query data lake directly with Spark
- Set up **Amazon Redshift Spectrum**, which is a connector that connects a Redshift cluster with certain databases / tables in S3. Then people only need to connect with one Redshift cluster and can query tables outside of the cluster just like the tables inside the cluster! (As long as the connection for the specific tables has been set up)