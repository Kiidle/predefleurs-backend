# PreDeFleurs

## In a Nutshell
The web application developed by Kiidle for "predefleurs" is an extensive and professional product that supports the entire operation of the business. The system is extremely user-friendly and offers different roles with varying permissions to ensure that each employee and customers can do precisely what they need to. The warning system is another useful feature that helps keep all users on the same page, and the account profile system enables each user to modify and update their account information.</br></br>
The financial management module is an essential part of the application, allowing users to track all financial transactions and manage the business's income and expenses. The reservation and pre-ordering system is easy to use and provides a fast and efficient way for customers to order flower arrangements and gifts.</br></br>
The application also offers an internal communication system that allows employees to communicate directly with each other, ensuring that everyone is on the same page. Additionally, the application has a robust management system that enables users to manage business information and access the data they need to perform their tasks efficiently.</br></br>
The forum feature is available for both employees and customers, allowing for open communication and engagement. Additionally, the warning system is present for both employees and customers, and any abusive behavior or language on the forum can result in warnings for the offender.</br></br>
It is also worth noting that the financial management feature is only accessible to specific authorized personnel, ensuring the data's confidentiality and security.</br></br>
Overall, the web application for "predefleurs" is a comprehensive and valuable investment for anyone looking to improve their gift and flower shop's operation. Its user-friendly features and comprehensive management system make it a professional and powerful solution for managing the business effectively.</br></br>

## Technologies
### Django
"Feeder" was developed using the Django technology. Django is a popular web framework that is widely used for building high-quality web applications quickly and efficiently. It provides a powerful and secure infrastructure for developing complex applications, and it is known for its scalability and flexibility. With Django, developers can easily create web applications with clean and maintainable code, making it a popular choice for building web applications. The use of Django in the development of "Feeder" ensures that the app is reliable, secure, and easy to maintain.

## Setup

### PIP
1. First, check if pip is already installed on your system by typing the following command in your terminal or command prompt: ```pip --version```. If pip is already installed, this command willl display the version number. If not, you will see an error message.
2. If pip is not already installed, you can download the installation script from the official website. Open our web browser and navigate to the following URL: ```https://bootstrap.pypa.io/get-pip.py```
3. Once the script has download, navigate to the directory where the script was downloading using your terminal or command prompt. For example, if the script was downloaded to your Downloads folder, you would navigate to that directory by typing the following command: ```cd /Downloads```.
4. Once you are using Python 3, you may need to use the command "python3" instead of "python".
5. After running this command, pip should be installed on your system. You can verify this by running the following command: ```pip --version```. If pip is installed correctly, this command should display the version number.

You have now installed pup on your system. You can use pup to install Python packages and manage dependencies for your projects.

### Pyenv
1. First you need to make surte that you have pip installed. To do this, open the command line and type "pip". If pip is not installed, you will need to install it first.
2. Install pyenv by typing the following command in the command line: ```curl https://pyenv.run | bash```. This will download the pyenv installation script and install it. If you are using a different operating system than Linux, please consult pyenv's official documentation for instructions on your operation system.
3. Once pyenv is installed, you can install the desired version of Python. To do this, type the folllowing command in the command line: ```pyenv install 3.x```. This will install Python 3.x on your system.
4. Additional info: Since feeder-backend works on Python version 3.x. Virtual Environment (venv) is already set up in this project. Just use the following command: ```source venv/bin/activate```
5. To make sure that you are using the correct Python version, you can type the following command: ````python --version```. If everything is set up correctly, this should display the correct version of python.

That's it! You have now installed the correct Python version. To exit the virtual environment, you can run the deactivate command in the command line.

### Django
1. Make sure you have Python 3.x installed. If not, please follow the previous guide on how to install Python 3.x.
2. Open the command prompt or terminal.
3. Type the command ```pip install Django``` and press Enter.
4. Wait for the installation to complete. The installation process should automatically install all necessary dependencies.
5. Check that Django was installed correctly by typing the command "django-admin --version" in the command prompt or terminal. If Django was installed, the current version of Django should be displayed.

Congratulations! You have successfully installed Django on your computer. You are now ready to create and develop a new Django web application.

### Project
#### Clone using SSH
1. Open your command prompt or terminal.
2. Generate an SSH key by typing the command "ssh-keygen -t rsa" and following the prompts.
3. Log in to your GitHub account and navigate to the project you want to clone.
4. Click on the "Clone or download" button and select "Use SSH" in the top right corner of the pop-up.
5. Copy the SSH URL provided.
6. In the command prompt or terminal, navigate to the directory where you want to clone the project.
7. Type the command ```git clone git@github.com:Kiidle/predefleurs-backend.git``` and press Enter.
8. Wait for the project to be cloned.

#### Clone using HTTPS
1. Open your command prompt or terminal.
2. Log in to your GitHub account and navigate to the project you want to clone.
3. Click on the "Clone or download" button and select "Use HTTPS" in the top right corner of the pop-up.
4. Copy the HTTPS URL provided.
5. In the command prompt or terminal, navigate to the directory where you want to clone the project.
6. Type the command ```git clone https://github.com/Kiidle/predefleurs-backend.git``` and press Enter.
7. Wait for the project to be cloned.

#### Run
1. Open your command prompt or terminal.
2. Navigate to the directory where the cloned project is located using the "cd" command.
3. Once you are in the project's directory, you should see a file called "manage.py". This file is responsible for managing the Django project.
4. Type the command ```python manage.py runserver``` and press Enter.
5. Wait for the server to start up.
6. Once the server is up and running, open your web browser and type "http://localhost:8000" in the address bar.
7. If everything was set up correctly, you should see the project.
