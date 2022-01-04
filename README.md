< [GMIT Data Analytics](https://web.archive.org/web/20201029063153/https://www.gmit.ie/computer-science-and-applied-physics/higher-diploma-science-computing-data-analytics-ict) | [Home](https://github.com/SeanOhAileasa) | [README](https://github.com/SeanOhAileasa/drp-app-server/blob/main/README.md) >

[![GMIT](https://github.com/SeanOhAileasa/SeanOhAileasa/blob/master/rc/gmit.png?raw=true)](https://web.archive.org/web/20201029063153/https://www.gmit.ie/computer-science-and-applied-physics/higher-diploma-science-computing-data-analytics-ict)

## Data Representation, Winter 21/22
### Due: last commit on or before January 4th, 2022

Winter 21/22 assessment for the ``Data Representation`` module (5 Credits) of the ``Higher Diploma in Science in Computing (Data Analytics) (H.Dip)`` programme (75 Credits) at **Galway-Mayo Institute of Technology (GMIT)**.

## Learning Outcomes

Investigate and operate the protocols, standards and architectures used in representing data, focusing on interacting with data services across the internet. The objective is to get practical experience in developing applications that interact with such data.

The module introduces the various means of retrieving data from external sources (for example, CSO, weather servers, etc.). The module looks at the formats that data can come in (``XML``, ``JSON``, ``CSV``) and how to retrieve (through an API) and process that data using JavaScript and Python. In addition, present data to the outside world by creating an ``API`` (Application Programmer's Interface) using the ``Python`` module ``Flask``.

In practical terms, the module looks at:

i. two means of representing data (``XML`` and ``JSON``);

- ``XML`` (of which ``HTML`` is a version) is used for rendering webpages;

- ``JSON`` is the JavaScript Object Notation and is a much shorter means of representing data.

ii. how data is transferred across the internet:

- ``HTTP``;

- RESTful APIs are the standard means for interacting with programs around the web - mechanisms for performing basic CRUD operations across the internet.

iii. how to create a web application that will serve out data across the internet and to be able to consume that data either via a web page or a ``Python`` script.


## Instructions

Write a program that demonstrates the understand of creating and consuming ``RESTful APIs``—creating a Web application in ``Flask`` with a ``RESTful API`` and linking to one or more database tables. In addition, making web pages that can consume the ``API`` and perform ``CRUD`` operations on the data.

## Motivation

Initially, I proposed to complete an application with a focus on a Data Analytics problem. However, given the requirement to demonstrate an understanding of creating and consuming ``RESTful APIs``, instead focused on ensuring the module's overall learning outcomes are met and for future reference of the topics. In addition, I was also providing sample work to show prospective employers. The following ``Jupyter`` Notebooks each document my engagement of the module and are supplemented by additional research where appropriate: 

#### i. [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/SeanOhAileasa/drp-data-representation/blob/main/drp-data-representation.ipynb)] ``Core Topics`` Jupyter Notebook

#### ii. [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/SeanOhAileasa/adb-MySQL/blob/main/adb-MySQL.ipynb#datarep)] ``MySQL Topics`` Jupyter Notebook


#### iii. [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/SeanOhAileasa/drp-app-server/blob/main/drp-app-server.ipynb#Abstract)] ``Flask RESTful API`` Jupyter Notebook

While the implemented ``RESTful APIs`` mirrors the module course example, it is essential to note that the implemented ``Flask`` app-server is a standalone application and is separate from the course example. For example, instead of ``ISBN`` as a ``Primary Key``, implemented an autoincrementing ``ID``.

## Installation

- Requires ``Python`` to be loaded on your local machine. Recommend downloading and installing Anaconda.

https://www.anaconda.com/download/

- The software must be downloaded and run on a machine as follows:

	- Clone the repository with the following command:

	``git clone https://github.com/SeanOhAileasa/drp-app-server.git``

	- Change directory to the cloned ``drp-app-server``
	
	``cd drp-app-server\``

	- Create i the database; ii. with table ``book``; and iii populate with the top five New York Times Best Sellers (as of January 4th, 2022):

	``python db.py`` # run python command

## Run ``Flask`` App

There are two ways of starting a ``Flask`` app-server:

a.) run the ``Python`` server program (giving the server's name).

``python .\rc\server\serverDAO.py``

b.) use environmental variables to set what is run:

###### Linux

``export FLASK_APP=.\rc\server\serverDAO``

``export FLASK_ENV=development``


``flask run``

###### Windows

``set FLASK_APP=.\rc\server\serverDAO``

``set FLASK_ENV=development``

``echo %FLASK_APP%``

``flask run``

### Browser

``http://127.0.0.1:5000`` redirects to ``http://127.0.0.1:5000/index.html``

### Hosting

``https://seanohaileasa.pythonanywhere.com/`` redirects to ``https://seanohaileasa.pythonanywhere.com/index.html``

## Credits

``Andrew Beatty`` - Lecturer at ``GMIT`` - Excellent walk-throughs on topics, promoting self-learning's importance.

## Contact

``Associate Apprenticeship Programme Candidate`` in ``Cybersecurity`` and seeking a sponsor [[GitHub](https://github.com/SeanOhAileasa)].

## END