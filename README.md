# Loede Budget
This is the repository for my semester project, Loede Budget. I developed a django application and hosted it on an EC2 instance. The data that users input into the expense report is stored in an AWS RDS database (that took forever to set up and get working correctly).

# Installation and Running on an EC2 server
First create an EC2 server.<br>
Give your server a name, for me, I named it "CC2" for Cloud Computing 2 as it was the second attempt at getting it deployed.<br>
Select Ubuntu for the operating system.<br>
You can then leave most of the other things blank or default, I however created a new key pair and used that for my deployment.<br>
Once done, launch the instance.<br>
After the status checks and the other booting things, connect to your EC2 server.<br><br>
Once connected, run the following commands:<br>

`sudo apt update`<br>
This will make sure your Ubuntu server has everything it needs to get started.<br><br>
`clear`<br>
Just to make everything look nice.<br><br>
`git clone https://github.com/loedetyler/LoedeBudget.git`<br>
Clone this repository into the server.<br><br>
`cd LoedeBudget/loedebudget/`<br>
Navigate into the correct directory.<br><br>
`sudo apt install python3-pip -y`<br>
`sudo apt install python3-django -y`<br>
These will make sure you have pip and django installed.<br>
After this, we then move into a tmux terminal so it will keep the EC2 instance running.<br>
Side note: When trying to test a different app I just did python3 manage.py runserver on the EC2 instance itself and after a while of inactivity it shut down, tmux helped prevent that.<br><br>
`tmux`<br>
Enter the [tmux](https://github.com/tmux/tmux/wiki) terminal.<br><br>
`python3 manage.py createsuperuser`<br>
Create a superuser and fill out the requested information.<br><br>
`python3 manage.py runserver --insecure 0.0.0.0:8000`<br>
Run the server with the insecure flag to maintain the CSS.<br><br>
`CTRL + B, D`
To escape the tmux terminal.<br><br>

# Disclaimer
While all the logic came from me, I did occasionally get assistance from ChatGPT, W3Schools, and YouTube for some help understanding and implementing concepts.<br>
I am not the best with CSS so I did ask ChatGPT for a lot of help there BUT it was a lot of "how do I get this drop down to look like this" or "I want the background to be this way, can you help me" and I have it set to not immediately show me code and to guide me to places where I can find answers instead of being served answers on a silver platter.<br>

# Getting Started
After all this, navigate to the Public IP of your EC2 instance or if you were just going to use the one I have up, navigate to: http://18.205.26.214:8000/<br>
Have a look around, click the burger menu to navigate to the About page or back Home. Click the User icon in the top right to login or create an account.<br>
Once logged in or you create an account, it will redirect you back to the home page.<br>
From here, now that you are authenticated, you will see a new option in the burger menu!<br>
Click Expenses in that menu to take yourself to the Expense Tracker.<br>
Feel free to add expenses here! They are yours and only yours, you won't be able to see anyone else's.<br>
