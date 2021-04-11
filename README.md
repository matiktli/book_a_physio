# Book A Physio Project

## Info
Physiotherapist and Gyms booking system.  

## Dev Info
> Lets keep the price < 1$/month.  

Architecture: Serverless on AWS _(what a rhyme)_  
Tech-stack _fronted_: ?  
Tech-stack _backend_: Python, Flask, Peewee, Boto3.  
Infrastructure: AWS Lambda, API Gateway, RDS, SNS, SQS.  

## Details
### Backend

#### Lambdas
Most services are using REST API with Flask and MySQL on RDS.

* [User Service](https://github.com/matiktli/book_a_physio/tree/master/backend/lambdas/user_svc) - Managing Users, Registration, Login.
* [Gym Service](https://github.com/matiktli/book_a_physio/tree/master/backend/lambdas/gym_svc) - Managing Gyms.
* [Booking Service](https://github.com/matiktli/book_a_physio/tree/master/backend/lambdas/booking_svc) - Managing Bookings. :construction:


### UI
:construction: