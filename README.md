### Contents

- [Description](#specification)
- [How to install](#how-to-install)
- [Changing ports](#changing-ports)
- [Run the application](#run-the-application)

# Description

This App will display the output of the `ps` command, showing the running processes on your **UNIX** system.

The backend is written in Python using Django, where it executes a Bash script that saves the information to the database. The frontend is written in Javascript using React, which displays the data stored in the database in a table.

# How to install

#### Make sure sqlite is installed, it's needed for the application. Django also has to be run with Python 3.

First the repository has to be cloned

    git clone https://gitlab.com/daniel-ulises/ps_project.git
Navigate to the project where two folders will be seen, client and server. The next step is to install the dependencies for them.

In the root of the project is going to be a 'requirements.txt' file, which is going to be used to install the dependencies for the Django application. To do so, run the following

```bash
# ~$PROJECT_DIR/

pip -r requirements.txt

# or

python -m pip -r requirements.txt
```
After the dependencies for Django are installed, go into the client directory and install the dependencies using `yarn` or `npm`

```bash
# ~$PROJECT_DIR/client

# If you use yarn
yarn install

# If you use npm
npm install
```
One that thing that has to be done is to create the database and tables that are necessary for the application. Fortunately Django makes allows this to be done with one simple command.
From the **server** folder, execute this command

```bash
# ~$PROJECT_DIR/server

python manage.py migrate
```
This will create the sqlite database and the tables defined through models in the Django application.

# Changing ports

The default ports used from this application are 8000 and 3000. If these ports are already taken in your system, you can easily assign different ports.

To change the port for the React application, you can do so in the 'package.json' file, that's in the **client** folder.

```bash
# ~$PROJECT_DIR/client/package.json

"scripts": {
    "start": "PORT=3000 react-scripts start"
```
Changing this value will make the script run the application on the desirted port.

For Django, the port has to be passed in the command used to run the application. Change `$PORT` to the desired port, for example 5000.
This command has to be run inside the **server** folder.

```bash
# ~$PROJECT_DIR/server

python manage.py runserver PORT
```
If the Django port is changed, it has to be also changed in the 'package.json' file inside the **client** folder

```bash
# ~$PROJECT_DIR/client/package.json

"proxy": "http://127.0.0.1:8000",
```
This is a proxy set up to shorten the paths in the React application.

# Run the application

Once the dependencies are installed and the ports changed if needed, the application can be started. To do so, two commands have to be executed.

To run the django application, this command has to be executed inside the **server** folder.

```bash
# ~$PROJECT_DIR/server

python manage.py runserver
```
If no port is added, it will run on port 8000 by default.

For the React application the following command has to be executed inside the **client** folder.

```bash
# ~$PROJECT_DIR/client

# If using yarn
yarn start

# If using npm
npm run start
```
If the port is not changed, it will run on port 3000.

Additionally, there is a Bash script called **startserver.sh**, which will run both applications in the same terminal. Note that if this script is used the default ports will be used, 8000 and 3000, unless the script is manually changed.
