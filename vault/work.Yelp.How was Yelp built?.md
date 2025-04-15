---
id: 4vzvi1b96nq3mqii7jmjwpp
title: How was Yelp built?
desc: ''
updated: 1744627224076
created: 1677849631052
---

# From monolith code base to service-oriented-architecture

Yelp has 2 main bodies of code - **services** and **yelp-main**. Yelp started with a monorepo yelp-main - a single application like a swiss knife that is doing everything, handling every user and every request. This is very common for tech companies. As their user base grow, their problems grow proportionally. The codebase becomes too complicated, concerns are not cleanly separated, many changes from many engineers go out together and performance of the whole system is measured by the performance of the worst part of the system. It is not scalable. The solution to this problem is services: individual, smaller code bases, running on separate machines with separate deployment cycles, that more cleanly address more targeted problem domains. This is called a Service-Oriented-Architecture: SOA.

As you build out services in your architecture, you will notice that instead of maintaining a single pool of general-purpose application servers, you are now maintaining many smaller pools. This leads to a number of problems. How do you direct traffic to each machine in the pool? How do you add new machines and remove broken or retired ones? What is the impact of a single broken machine on the rest of the application?

Dealing with these questions, across a collection of several services, can quickly grow to be a full-time job for several engineers, engaging in an arduous, manual, error-prone process fraught with peril and the potential for downtime.

## The two Yelp repos

Yelp-main is the monolithic code base that represents the bulk of the existing (now legacy) Yelp app. It has existed since Yelp's inception and we are trying our best to separate functionality into services. This repo is not owned by any team. Teams own different parts of the repo. And we use **fork and pull model** [[engineering.git]]

Services at Yelp are applications that provide a set of functionality via a well defined  interface. All code development happens in the same repository. Developers share development work via git branches. This is described as the **shared repository model**. The master branch contains the latest stable changes.

**Move to Micro Services architecture**

Yelp has moved to Microservices architecture. Initially Yelp started with a monolith web application called “yelp-main”.

So when you visit yelp and start searching for any specific business or topic, you would hit their auto completion service as you type the search query. Then on searching, it would hit their backend service that would try to understand the query semantics and finds the suitable results matching the query. After the search results are displayed it is possible to select a specific business and order anything. This would result in hitting their payment service and also other services required for communicating to the partners.

As they broke the monolith “yelp-main”, the “yelp-main” become more of a frontend application, responsible for aggregating and rendering data from their growing number of backend services.



# PaaSTA was born

PaaSTA is Yelp’s defacto platform for running services and containerized batches. It is open-sourced [repo](https://github.com/Yelp/paasta) though it is probably close to impossible to set it up on your own. PaaSTA is Yelp's internal Distributed System Infrastructure to run all services.

## Principles
#TODO https://paasta.readthedocs.io/en/latest/about/paasta_principles.html


## Tech blog
#TODO
https://engineeringblog.yelp.com/2015/11/introducing-paasta-an-open-platform-as-a-service.html



## SPARK
https://engineeringblog.yelp.com/2020/03/spark-on-paasta.html

## Tron
https://engineeringblog.yelp.com/2010/09/tron.html

Yelp internal scheduling 
[open-sourced repo](https://github.com/Yelp/Tron)


# Scale from 0 to 139 million users

[VP Engineering article](https://engineeringblog.yelp.com/2014/10/scaling-traffic-from-0-to-139-million-unique-visitors.html)


Yelp was born pre-AWS, so we had to operate our own data centers.