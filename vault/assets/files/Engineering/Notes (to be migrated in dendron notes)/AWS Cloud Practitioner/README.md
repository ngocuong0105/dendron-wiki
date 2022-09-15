## Aimed for the stars, ended up in the cloud

Reading material for AWS can be found [here](https://github.com/ngocuong0105/algorithms/tree/main/Readings/Engineering/AWS)
------------------------------------------------------------------------------

### Q&A session
Q1: Which design principles are enabled by the AWS Cloud to improve the operation of workloads? \
A1: - Remove single points of failure
    - Loose coupling
Loose coupling is an approach to interconnecting the components in a system or network so that those components, also called elements, depend on each other to the least extent practicable. Coupling refers to the degree of direct knowledge that
one element has of another.

------------------------------------------------------------------------------
Q2: What is a Job in AWS?\
A2 : A unit of work (such as a shell script, a Linux executable, or a Docker container image) that you submit to AWS Batch

Q3: What does AWS Batch do?
A3: AWS Batch helps you to run batch computing workloads of any scale. AWS Batch automatically provisions compute resources and optimizes the workload distribution based on the quantity and scale of the workloads.

------------------------------------------------------------------------------
Q4: What is IOPS?\
A4: Input outputs per second

Q5: What is EBS and where you can access it?\
A5: Elastic Block Storage. It is not an AWS service directly, it is part of AWS EC2 service (for creating a VM image) and EBS is one of the configurations you need to set up.

Q6: What are the 2 general types of EBS?\
A6: General Purpose SSD (simple), Provisioned IOPS SSD (complex for I/O-intensive database workloads)

------------------------------------------------------------------------------
Q7: What is agility in AWS?\
A7: Agility is the practice of “building in” the ability to change quickly and inexpensively.

Q8: How does the AWS cloud increase the speed and agility of execution for customers?\
A8: Fast provisioning of resources, scalable compute capacity.

------------------------------------------------------------------------------
A legacy application (legacy app) is a software program that is outdated or obsolete.\
Q9: A company is planning to move a number of legacy applications to the AWS Cloud. The solution must be COST-EFFECTIVE. What would you propose?\
A9: Re-host the application on Amazon EC2 instances that are RIGHT-SIZED (cheapest).


------------------------------------------------------------------------------
Q10: When running applications in the AWS Cloud, which common tasks can AWS manage on behalf of their customers?\
A10:


------------------------------------------------------------------------------
Q11: What is Amazon S3?
A11: It is a object storage built to store and retrieve any amount of data from anywhere. Amazon Simple Storage Service.

Q11: How much data can a company store in  Amazon S3 service?
A11: Virtually unlimited. Amazon S3 objects can range from 0 bytes to 5 TB, but the total amount of data is unlimited. Storage is not a problem anymore! Computing still is.



------------------------------------------------------------------------------
Q12: What is Amazon RDS?\
A12: Amazon Relational Database Storage.

------------------------------------------------------------------------------
Q13: What advantages does a database administrator obtain by using Amazon RDS?\
A13: Simplifies admin tasks (UDEMY stupid general answer).
RDS databases have auto scaling for storage (SSD) but for compute (CPU and RAM) it scales based on instance type(manual)
AWS RDS has built-in Multi-AZ feature. This feature creates a standby instance in another Availability Zone and asynchronously
 replicates it. In the event of failure of the primary database you can recover it.

------------------------------------------------------------------------------
Q14: What is SRE?\
A14: Site reliability engineers/engineering. Goal is to create scalable and highly reliable software systems. It is closely related to DevOps. Site reliability engineering include automation, system design, and improvements to system resilience

------------------------------------------------------------------------------
Q15: Which AWS Service provides with a managed version control system?\
A15: AWS CodeCommit hosts Git-based repos.

AWS CodePipeline is a continuous delivery service that automates release pipelines for code.

------------------------------------------------------------------------------
Q16: What is AWS Well-Architectured tool?\
A16: The AWS Well - Architected Tool helps you review the state of your workloads and compares them to the latest AWS architectural best practices.

5 best practices which are recommended:
- perform operations as code
- make frequent, small, reversible changes
- refine operations procedures frequently
- learn from all operational failures

------------------------------------------------------------------------------
Q17:Customers using AWS services must patch operating systems on which of the following services? (Amazon DynamoDB,
Amazon EC2, AWS Lambda, AWS Fargate)\
A17: Amazon EC2. It is a infrastructure as a service (IaaS). Underlying it you have a hardware and a virtual server handled
for you. However you must manage the operating system on the server and installing regular patches on the operating system.
Patches are small local updates/changes of a software. All other answers are serverless.

------------------------------------------------------------------------------
Q18: A user is planning to launch 3 EC2 instances behind a single Elastic Load Balancer. Want high availability.
How to achieve this?\
A18: Launch the instance across multiple Availability Zones in a single AWS region (ELB cannot work across regions!)

------------------------------------------------------------------------------
Q19: Which AWS feature you would use to provide root storage for Amazon EC2 instance?\
A19: Amazon Elastic Block Store(EBS).

------------------------------------------------------------------------------
Q20: What is Amazon SNS?\
A20:Amazon Simple Notification Service (Amazon SNS) is a web service that makes it easy to set up, operate, and
send notifications from the cloud to subscribers on your web app. End point is their url or email.

------------------------------------------------------------------------------
Q21: Amazon Virtual Private Cloud (VPC) can include multiple (AWS Regions, Internet gateway, Availability Zones,
Edge locations?)\
A21:

------------------------------------------------------------------------------
Q22: A company wants to refactor an app that does not scale well into the cloud and is refactoring it into a microservice
architecture. What vest practice of AWS Well-Architectured Framework does this plan relate to?\
A22: Implement loosely coupled services.

------------------------------------------------------------------------------

Distributed Denial of Service
DDoS Attack means "Distributed Denial-of-Service (DDoS) Attack" and it is a cybercrime in which the attacker floods a server with internet traffic to prevent users from accessing connected online services and sites.

Q23: What is one method do protect against DDoS attacks in the AWS Cloud? \
A23: Crete a firewall