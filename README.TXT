Nathan Yee
nyee@csu.fullerton.edu
CPSC449-01
Project 3: Server-side Sessions 

This project includes a PDF of screenshots and their descriptions, python source code for sessions.py and dump.py, and this README.TXT file. An example of some screenshots show two different browsers running app.py on localhost:5000 with separate counts. The main focus of this project was running these applications and seeing how they can manipulate data such as cookies or key:value pairs. The file dump.py will be ran with the command $ python3 ./dump.py localhost:5100. This file will post key value pairs to the given URL and print in the terminal the key value pair using a get method. Foreman will be used to start both applications and another terminal is needed to run dump.py. 

# How to run this project ########################################################################################################
open one terminal and change directory to the counter folder. 
run the command $ foreman start

open another terminal and change directory to the folder containing dump.py
run the command $ python3 ./dump.py localhost:5100 

# dump.py ########################################################################################################################
First we need to import requests and sys. 
Then I created a url variable that will store the first argument from the command line which is supposed to be localhost:5100
This code stores all of the key value pairs in a variable as a dictionary.
We now create a sessions object using requests.post(url, json=var)
The sessions object just created has a method to show the status code. An exception is created to test if the status code is not 200.
We now create another sessions object using requests.get(url). This object contains data from the given url
We now use the .json() function on this object to convert the data to json. 
then we use .values() to get a list of the keys stored
A nested loop is created to loop through the list of keys and each value is extracted for a get request using requests.get(url + str(var) 
The json value of this object is then printed as a key value pair. 

# sessions.py ####################################################################################################################
This file just required us to override the set_key, get_key, and delete_key methods of the session store class. in the __init__ function, self.url = url was written to access the url from other functions. Set key is given two parameters. A key (session.sid) and a value (dict(session)). A post method is used to post the session id cookie and the value of the count to the url. 
The get_key function was written using a get method. .get(self.url + '/' + key) was used to get the key object.
the delete_key function is very simialr to the get_key function where the only change is .delete is used instead of .get.

# overview #######################################################################################################################
I was not able to get the counter working when foreman start was ran. I beleive there is a problem with the way I have implemented my set_key funciton in sessions.py. When I refresh the count app, A cookie is created and when dump.py is ran, I am able to see the cookie and the count (stored as an int) but the count will not increment. I have tried many solutions and ways of storing the value. I can see that it is passed in as a dict so the logical way to post the key value would be to use {key:value['count']} 

