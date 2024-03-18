# ORB-CHALLENGE-DEFAULT

P.S. This project made for a company's job application challenge project! Not personal project! <br />

<br />
API ENDPOINTS :  <br />
- `POST /events` - Create a new event reminder. <br />
- `GET /events` - Retrieve all events. <br />
- `GET /events/{id}` - Retrieve details of a specific event. <br />
- `PUT /events/{id}` - Update a specific event. <br />
- `DELETE /events/{id}` - Delete a specific event. <br />
- `GET /events/upcoming` - Retrieve events happening in the next 24 hours. <br />
- `GET /events/category/{categoryName}` - Retrieve events by category. <br />

<br />
INSTALLATION AND SETUP <br />
Make sure to install all requirements, in order to do that; <br />
pip install -r requirements.txt (be sure you are in the right path in terminal) <br />
<br />
If you want to create your own .venv ; <br />
python -m venv venv <br />

<br />
After installing requirements we can start, <br />
python manage.py makemigrations <br />
(This command detects changes made to the model files in your project and creates a "migrations" file according to these changes. This file defines changes to the database schema but does not update the database, it just saves the changes made to the model.) <br />
<br />
python manage.py migrate (this command will do that) <br />
<br />
In order to run project, <br />
python manage.py runserver  (it will run local server and the project) <br />

<br /> <br /> <br />
NOTE : You can test the API by sending requests by using POSTMAN or with any other method, I'll use POSTMAN.
<br /> <br /> <br />

<br /> <br />
QUERY EXAMPLES&TEST : <br />

<br />
api/events/  (GET) : <br />

![image](https://github.com/JiyuuX/ORB-CHALLENGE-DEFAULT/assets/139239394/2d7aa7ef-4ce0-47fa-aae9-31ece2049183)

<br />
api/events/ (POST) : <br />

![image](https://github.com/JiyuuX/ORB-CHALLENGE-DEFAULT/assets/139239394/233b32a3-0e14-4bbf-b6ca-dfca41cc0aa9)

<br />
api/events/<event_id>/ (GET) : <br />

![image](https://github.com/JiyuuX/ORB-CHALLENGE-DEFAULT/assets/139239394/eb8b305a-d15e-4389-825c-8d64a92a588f)

<br />
api/event/catrgory/<category_name>/ (GET) : <br />

(1) ![image](https://github.com/JiyuuX/ORB-CHALLENGE-DEFAULT/assets/139239394/4e5e72a8-fab1-44c9-91af-c741b20f5b43) <br />

(2) <br /> ![image](https://github.com/JiyuuX/ORB-CHALLENGE-DEFAULT/assets/139239394/ed6ac840-38c7-4dea-8094-549a59939f52) <br />

<br />
api/events/<event_id>/ (DELETE) :  <br />

![image](https://github.com/JiyuuX/ORB-CHALLENGE-DEFAULT/assets/139239394/972164c1-5b34-44d9-8725-e950e400b61b)

<br />
api/events/<event_id>/ (PUT) : <br />

![image](https://github.com/JiyuuX/ORB-CHALLENGE-DEFAULT/assets/139239394/56f959ff-8a25-4ba9-a9be-bc402c4b5a41)

<br />
api/upcoming/ (GET) : <br />

![image](https://github.com/JiyuuX/ORB-CHALLENGE-DEFAULT/assets/139239394/e04c1dfa-63f0-403d-a361-99c478408791)


<br />
NOTE : <br />

 Default Challenge Project ended, its little bit much more improved version is at ("https://github.com/JiyuuX/ORB-CHALLENGE-IMPROVED") here!
 
