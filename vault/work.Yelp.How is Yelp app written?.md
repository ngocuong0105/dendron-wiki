---
id: 4vzvi1b96nq3mqii7jmjwpp
title: How is Yelp app written?
desc: ''
updated: 1677851010804
created: 1677849631052
---

Yelp has 2 main bodies of code - **services** and **yelp-main**. 


Yelp-main is the monolithic code base that represents the bulk of the existing (now legacy) Yelp app. It has existed since Yelp's inception and we are trying our best to separate functionality into services. This repo is not owned by any team. Teams own different parts of the repo. And we use **fork and pull model** [[engineering.git]]
services at Yelp are applications that provide a set of functionality via a well defined 
interface. All code development happens in the same repository. Developers share development work via git branches. This is described as the **shared repository model**. The master branch contains the latest stable changes.

**Move to Micro Services architecture**

Yelp has moved to Microservices architecture. Initially Yelp started with a monolith web application called “yelp-main”.

So when you visit yelp and start searching for any specific business or topic, you would hit their auto completion service as you type the search query. Then on searching, it would hit their backend service that would try to understand the query semantics and finds the suitable results matching the query. After the search results are displayed it is possible to select a specific business and order anything. This would result in hitting their payment service and also other services required for communicating to the partners.

As they broke the monolith “yelp-main”, the “yelp-main” become more of a frontend application, responsible for aggregating and rendering data from their growing number of backend services.


# Scale from 0 to 139 million users

[VP Engineering article](https://engineeringblog.yelp.com/2014/10/scaling-traffic-from-0-to-139-million-unique-visitors.html)