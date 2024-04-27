## Description workshop_3

For this workshop number 3 we wanted to implement an application of a vehicle catalog, as in workshop 1 and 2, however, in this case some modifications were made so that there is a user interaction with the vehicle catalog through an interface, doing this in a way that can optimize memory and flexibility in the application using structural patterns.

The following requirements were taken into account to achieve our purpose
* Application is still consuming a lot of memory, so you must reduce it as much as
possible.
* An authentication system is needed, so you must create a simple login system where
you could register users and authenticate them.
* You should differentiate two types of users: Admin and User. Admins could create,
update, and delete vehicles, while Users could only see and search the vehicles.
* You should log all the actions made by the users, so you could track both the changes
made in the vehicles and searches performed.
* Separate your project in different subsystems, and a made a simple interface to interact
with them.
* In addition, you must create a monitoring system to check the memory consumption
and time execution of the searches in the application, and save stats in a performance_log file.
* To increase performance, you should implement a cache system to store the last five
search results over vehicles.
* Verify if you could add encapsulation to increase the security of the application.
You must deliver a technical report where a Class Diagram of your solution is provided, also all related updated additional documentation; here it is recommended to think
in components, define a diagram por each component where connections with other components will be absolutely clear. Also, you must write about technical concerns and decisions
you make to create the architecture you are proposing; this includes SOLID implementation
analysis of your model, coupling, cohesion, and other software engineering principles.
