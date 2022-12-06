# course-project-group-17 : Weekly Schedule
Introduction:
The weekly schedule is a planner in which the user can input to-do activites and have their day scheduled. The Schedule maximizes someones break to work ratio in order to create days with the least stress.
Architecture:
The Scheduler is broken up into two pieces; the backend using Django and the frontend using React.js. When a User inputs their activities, a Json response is sent to the backend, where two models are created, an Event model representing the recieved information and a Finalized model that takes the database created by Event and sorts it into a planner. The Finalized database is then serialized into Jsons and sent to the frontend, where the website refreshes add displays the sorted itinerary.
Installment and Use Instructions:
1) Copy the Git repository into your prefered coding environment. Then cd into the course-project-group17/src/
2) Then enter "pip3 install -r requirements.txt" into the terminal. If An error occurs and pip3 is not installed, follow the prompts to install it.
3) To create your virtual Environment, run "python -m venv Scheduler_env" and activate it using source ./logrocket_env/bin/activate.
4) Then cd back into the root folder and cd into the weekly-calendar-react.
5) Run npm install, which will install the dependencies of the frontend
6) Use Instructions: On the frontend run npm start and on the backend run python3 manage.py run server and open React at http://localhost:300
7) Then simply add tasks using the "Add Task" Button and watch your schedule unfold.
