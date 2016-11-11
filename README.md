#Flask Blog

Utilizes the Flask framework to provide the basis for any list type web application. The demonstration 
provided is setup as blog in which users can add posts and tag them with the appropriate category. This could really 
be used for any list type of application, such as: tutorials, products, reviews etc.<br /><br />
Live Demo: http://flask-blog.chaddmyers.com/<br />
<br />

##To Run:</b><br />
    1. Install python
    2. Install necessary requirements (list will be here)
    3. run application.py

##Api Routes

A quick list of available JSON endpoints are listed below. These can be used to extend this 
to any platform that can make http requests.

http://localhost:5000/Item/ - GET /{ model }/  <br />
http://localhost:5000/Item/1 - GET /{ model }/{ id }  <br />
http://localhost:5000/Category/ - GET /{ model }/  <br />
http://localhost:5000/Category/Item/ - GET /{ model }/{ model } <br />

