# Github Push Issues #

 ### Issue Summary ###

On August 10th from 9:00am PST until August 10th 3:pm PST, Github.com wasn't
accepting my push request for the AirBnB_V2 project. At its peak, this issue
affected the single user (me) from being able to complete this portion of the
project in a respectable time frame. The root cause of the issue was Github.com
recognizing a repository that was linked to a different individual at
Holberton School.

### Timeline(all times Pacific Time) ###

* 9:00am PST-Proper completion of pushing a file to github is completed
* 9:05am PST-Issue detected after the Holberton School checker return red x's
* 9:10am PST-The user(Max Johnson) ensures that he has done the proper checks for the file
* 9:28am PST-Following the Github.com documentation for fixing push and pull request, the user doesn;t come up with a proper solution
* 9:32am PST-The user asks other members of The Holberton School to take a look at what is causing the issue
* 11:00am PST-More students try to trouble shoot the problem but nothing was resolved
* 1:00pm PST-The cause of the problem was found by Holberton School Guillame Salva
* 1:05pm PST-The issue was Github referring to the original Airbnb repository of John coleman
* 3:00pm PST-Guillame Salva fixed the issue by creating a entire new repo

### Root cause ###

At 1:00PM PST, a configuration change was made via Guillame Salva. The change specified
that the current repo of user1 (Max Johnson) was linked to the repo of user2 (John coleman).
Since the AirBnB project code base is linked to user2 and user1 originally collaborated
with user2 at the beginning of the AirBnB project, Github didn't recognize the files
eventhough they were pushed to user1's repository.

### Resolution ###

At 3:00pm PST, a new repository was made and properly configured to be recognized by
The Holberton School's checker.

Markup : ### Corrective and Preventative Measures ###

* Create a new repository to avoid this issue
* Make sure the user properly knows how to use Github
* If a user spends more than two hours on a problem then they need\n talk to upper management.
* Document all of the issues so you have a proper record for future use

Max Johnson
[Twitter](https://twitter.com/MBJohnson31)