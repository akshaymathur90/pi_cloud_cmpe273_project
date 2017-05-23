
<h1>Pi-Cloud</h1>

Pi Cloud is a Raspberry Pi based PaaS service that can add or remove the nodes in real-time without restarting the server.

<h2>Features Implemented:-</h2>

<h3>Controller:</h3>
1. Register the worker nodes.
2. Download the application to be installed from GitHub.
3. Install application dependancies on the worker node.
4. Launch the application on the node.
5. Route HTTP traffic to the application running on worker nodes.
6. Re-Deploying an existing application with latest source code from GitHub.
7. Publish controller details to Directory Services. 

<h3>Workers:</h3>
1. Identify the controlling node using Directory Service module implemented.
2. Registering themselves with the controller as available nodes.

<h3>Directory Services (Running on AWS):</h3>
1. Keep track of the controller node in the Pi-Cloud.
2. Provide controller node details to worker nodes.

<h2>Technologies Used:-</h2>
1. User Interface: AngularJS and HTML
2. Backend Server: Python Flask
3. Python Fabric library to connect to worker nodes.
4. HAProxy for dynamic HTTP Routing.
5. Sqlite3 Database.

<h2>Screenshots:-</h2>
To Deploy an App:
![alt text](/screenshots/Deploying%20an%20App.png?raw=true "Deployed Apps")
To view Deployed Apps:
![alt text](/screenshots/All%20Deployed%20Apps.png?raw=true "Deployed Apps")

<h2>Running this project:-</h2>
1. Clone the source code on a Raspberry Pi.
2. Create and activate a virtual environment.
3. Install the dependencies using pip install -r requirements.txt
4. python manage.py create_db
5. python manage.py db init
6. python manage.py db migrate
7. python manage.py runserver -h 0.0.0.0 -p 5000
8. Configure the Directory Service scripts on worker and controller respectively using crontab @reboot.
