This Yoga class application is a dynamic website which reacts at realtime as well as it is a highly scalable application. This website is totally developed on tech stacks Django, Python, Html, Css, Bootstrap4, Javascript, sqlite3(Database). I have used ORM (Object Relationship Mapping) for database handling and DTL (Django Template Library) -and dynamic data handling in between backend and frontend. 

SignUp:
This application have feature of secure signup with django authentication. Signup has password validator and username, email, age validations which is calculated from difference of date of birth and present date so that people with age less than 18 or above 65 cannot register. Also a user cannot keep a password less than 8 characters. 

LogIn:
login is done using the safer auth library of django authentication. Each password is hashed into a string to protect user data from hacking. A user can login with their username and password. There is an Admin portal(to manage all the database). 

Payment:
User can select four slots and then confirm the payment by clicking pay now. After clicking pay now button user will be redirected to dashboard where date of user's last transaction, number of days left in his/her plan and the time slot user selected will be displayed. 

Number of days left in a plan are calculated by fetching the last transaction and comparing it with present date to get number of days passed which is subtracted from 30. 

If number of days after last transaction is more than 30 or there is no previous transaction then a pay button will be visible on dashboard otherwise other details will be shown on dashboard. This will prevent user from paying more than once in a month. The user can also choose to cancel payment.

Dashboard:
If user is not authenticated or visited for first time then signup and signin options will be shown to user.
If user is logged in then user's payment details and yoga slot information are shown. There is also a log out option in navbar menu. 

In addition to these various yoga asanas, benefits of yoga, various services and different time slots are also added in dashboard.

Some problem statements solved are... 
1. User won't be able to pay before his last plan gets over.
2. Users will be able to know there last transaction.
3. The days remaining in users subscription will also be shown on dashboard.
4. There slot details will also be updated on the dashboard.

To run this web application on your device:
You first need to have following softwares:- 
1)python with latest version 
2)pip with latest version 
3)Visual Studio with latest version 
4)All path should be added to system variables

Then:
 1)Go to the location where you want to install the software and make one folder. 
 2)After this, paste the application file in the same location. 
 3)Install all the packages mentioned in requirements.txt 
 4)Now lets create Admin superuser, run the command: 
 python manage.py createsuperuser 
 username=Lovebansal 
 email=Love@gmail.com 
 password=1234(won't be able to see typed characters.so don't worry.just type it) 
 confirm password=1234(won't be able to see typed characters.so don't worry.just type it) 
 weak password[Y/N]=Y 
 superuser will get created. 
 5)Now you can run your application. 
 6)Use the following command. python manage.py runserver go to google chrome and type in the url bar http://127.0.0.1:8000/ and the application will get executed successfully. 
 7)to visit admin site visit http://127.0.0.1:8000/admin
