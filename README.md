# Log Analysis Project
#### Full Stack Web Developer Nano-Degree

### Overview
>This project is about building an internal reporting tool for a site, that will use information from the site's database to discover what kind of articles the site's readers like by answering the following questions:
>- What are the most popular three articles of all time?
>- Who are the most popular article authors of all time?
>- On which days did more than '1%' of requests lead to errors?

### Database
The database used in this project is newsdata.sql, provided by Udacity, which contains newspaper articles, authors, as well as the web server log for the site. 

### Requirements
* [Python3](https://www.python.org/)
* [Psycopg2 v2.7.5](http://initd.org/psycopg/download/)
* [PostgreSQL v9.5.14](https://www.postgresql.org/download/)
* [Vagrant v2.2.0](https://www.vagrantup.com/downloads.html) 
* [VirtualBox v5.1.38](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [FSND virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)
* [News Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### Setup
##### 1. Start with Software Installation
Once you get the above software installed, follow the following instructions:
```
cd vagrant
vagrant up
vagrant ssh
cd /vagrant
mkdir log-analysis-pr
```

\- For this project, all the work will be on your Linux machine, so always make sure you logged in by using the following commands:
`vagrant up`, then `vagrant ssh`, then `cd /vagrant`.
Note: Files in the VM's `/vagrant` directory are shared with the `vagrant` folder on your computer. But other data inside the VM is not.

##### 2. Download and Load the Data
  - Move the `newsdata.sql` to your project folder `log-analysis-project`
  - Load the data from the `newsdata.sql` by using the following command: Note that we are
using PostgreSQL for this project:
    ```
    psql -d news -f newsdata.sql
    ```
  - Once you have the data loaded into your database, connect to your database using:
    ```
    psql -d news
    ```
    
### Views
* PopularArticles view created for executing the first two queries:
```
        CREATE OR REPLACE VIEW popularArticles AS
        SELECT articles.title AS articlesTitle,
        articles.author AS authorsID,
        COUNT(log.id) AS views
        FROM articles
        LEFT JOIN log ON '/article/' || articles.slug = log.path
        GROUP BY authorsID,
        articlesTitle,
        log.path
        ORDER BY views DESC;
```

* Requests view created for executing the third query:

```
<<<<<<< HEAD
           CREATE OR REPLACE VIEW requests AS
           SELECT TO_CHAR(TIME, 'MON DD,YYYY') AS Date,
                   Count(*) AS Total,
                   SUM (CASE
                            WHEN status != '200 OK' THEN 1
                            ELSE 0
                        END) AS Errors
           FROM log
           GROUP BY Date
           ORDER BY Date;                                                       
```

Note: I provided an SQL script <create_views.sql> that contains the CREATE VIEW statements.
You can import that script to the "news" database directly from the command line by typing:
```
psql -d news -f create_views.sql
```

#### How to run:
  Run the python script <logs.py> from the vagrant directory inside the virtual machine, using:
  ```
    $ python3 logs.py
  ```
  
||||||| merged common ancestors
"CREATE VIEW requests as
               SELECT TO_CHAR(time,'MON DD,YYYY') as Date, Count(*) as Total,
               Sum (CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END) as Errors
               FROM log
               GROUP BY Date
               ORDER BY Date;                                                        
```
=======
CREATE VIEW requests as
               SELECT TO_CHAR(time,'MON DD,YYYY') as Date, Count(*) as Total,
               Sum (CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END) as Errors
               FROM log
               GROUP BY Date
               ORDER BY Date;                                                        
```
>>>>>>> 2e6f62a11fbcb1c6fc274b51ad0e1925f5f2511a
