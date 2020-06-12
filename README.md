# Tutorial API (Application Pogramming Interface)

![Tutorial](/media/images/1.jpg)

## Built By [Dan Kariuki](https://github.com/Buttonupd/) And Sheila Mmbukane (https://github.com/Mmbukane-shy6)

## Description
This a basic API development application, A CRUD positioned basic platform which generates api endpoints for a tutorial application. API has been developed using  Django framework. The user interface, which consumes the API has been developed using Angularjs.

## User Stories

Users would like to:
* Create a new tutorial item.
* Retrieve all tutorials items.
* Retrieve one tutorial item.
* Update tutorial item.
* Delete tutorial item
* Delete all tutorials
* Search for a tutorial item

## Admin Abilities

Admin should:
* Update the API
* Create new API endpoints


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| In DRF, provide username and password to generate ccess token | **Home page** | Save the token, both access and refresh |
| Open the Angular app | **Navigate to the directory** | ng serve|



## SetUp / Installation Requirements
### Prerequisites
* python3.7
* pip3
* virtualenv
* Requirements.txt
* Angularjs


### Cloning
* In your terminal:

        $ git clone https://github.com/Buttonupd/Tutorial
        $ cd Tutorial

## Running the Application
* Creating the virtual environment

        $ Virtualenv env(* 'env is the name of the enviroment')
        $ source env/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ ./manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ ./manage.py test Tutorial

## Technologies Used
* Python3.7
* Django Framework
* Postgresql Database
* Django Rest Framework
* Angular

## License

Copyright (c) 2020 Dan Kariuki

------------

