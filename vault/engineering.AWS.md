---
id: poc9vlh4u5k814ql4zlyuxw
title: AWS
desc: ''
updated: 1761560594386
created: 1668960751907
---



AWS Certified Practitioner Course
------------------------------------------------------------------------------------

How do websistes work?
Client (your computer)- ---- Network ------- Server (data base system)

Network = routes packets(data from the server) 

Clients and Servers have IP address to find each other

Server send to Client (for client perspestive they get response from server)

What is a server? Server contains:
- CPU (computetion), 
- RAM (temporary memory), 
- Storage data (permanent memory),
- Database (structured data)
- Network (routers, switch, DNS server)

Router forwads pachets between computers in the network
Switch knows where to send these packets in the server.

The cloud gives you all these things above ON DEMAND (scalable).
No need for big servers in data centers and on prem.

3. What is Cloud Computing?

Cloud Computing is the on-demand delivery of servers which do the things in prev note.

Allows you to choose the right TYPE and SIZE of computing you need. 
Access to these resources Instantly.

AWS owns and maintains the network-connected HARDWARE. You use only the web application.

Cloud Types/Models
- private cloud (cloud service used by a single organization)
- public cloud (service delivered over the Internet)
- hybrid cloud

Problems solved by the cloud:
- time flexibility (instant resource access)
- cost-effective (pay as you go)
- scalability (no need buy servers and maintain them)
- elasticity (scale out and scale in when needed)
- availability and fault-tolerance (build across indepenedent data centers)
- agility - rapidly develop, test and launch software

Managing servers see page 4 picture!:

On prem - care about EVERYTHING

Cloud computing service types:
- Infrastructure as a Service (IaaS) - - care about OS, Runtime,Middleware, Data, Application
- Platform as a Service (PaaS) - care about Data, Applications
- Software as a Service (SaaS) - just use it

Examples:
- IaaS -> Amazon EC2 instance (Virtual machine on AWS)
- PaaS -> Heroku, (Elastic Beanstalk on AWS)
- SaaS -> (Zoom, Dropbox, Gmail, Rekognition on AWS)

AWS services can be any of the cloud computing types.

Pricing on the cloud:
- pay for compute time
- pay for amount of data stored on the cloud
- pay for data transfer out of the cloud


4. AWS overview

Global infrastructure:
- AWS Regions
- AWS Availability zones
- AWS Data Centers
- AWS Edge Locations/Points of presence

AWS Region e.g eu-west-2
A region is a cluster of data centers
Use AWS region close to you to have low latency

AWS services are region scoped! The same service ran in different regions runs it 2 times

How to choose AWS region?
- compliance (data govenrnance and legal requirements)
- proximity (low latency)
- available services in region
- pricing in region

AWS zones are SUBSET of AWS regions. AWS zone = AWS availability zone is one or more discrete data centers with their own power, networking and connectivity

Shared responsibility Model
Customer is responsible for the security IN the cloud
AWS is responsible for the security OF the cloud

5. IAM = Identity and Access Management global service

Provides access control across all of AWS.
With IAM you can specify who can access which services and resources.

IAM policies you manage permissions to other people.
Access is denied by default and is granted only if you specify Allow.

Root account is created by default when you register in AWS.
Should NOT be shared or used when developing applications.

How users access AWS:
- AWS Management Console (screen on the web app - protected by password + MFA(optional))
- AWS CLI (protected by access keys)
- AWS SDK (for code protected by access keys)

Access keys are like passsowrds generated through the AWS Console (screen on the web app)


An IAM user group is a collection of IAM users. 
User groups let you specify permissions for multiple users.

E.g. For a group called Admins  any user in that user group automatically has Admins group permissions

An IAM role is an IAM identity that you can create in your account that has specific permissions. 
IAM role vs IAM groups
Short answer for googlers: you can't assign role to user but can assign group to user.
    group is a bunch of users with the same policies
    role is a preset of policies for service(s)

Best practices:
- dont use root account except for AWS account setup
- One physical user = One AWS user
- assign users t groups and assign permissions to groups
- never share IAM users and access keys
- Audit permissions of you account with the IAM credentials report


6. Amazon EC2 = Amazon Elastic Compute Cloud = Virtual machine

Amazon EC2 is a service allowing you to:
- rent virtual machines (EC2 instances)
- storing data on virtual drives (EBS = elastic block storage)
- distribution across machines (ELB = elastic load balancing)
- scaliing services using auto-scaling group (ASG)

AWS EC2 is about renting compute/memory on demand (basically what AWS is about).
