import psycopg2

conn = psycopg2.connect(database="news")
cursor = conn.cursor()

# Creating (PopularArticles) view to be used in the first two queries

popularArticles = "CREATE VIEW popularArticles as " \
        "SELECT articles.title as articlesTitle, articles.author as authorsID, COUNT(log.id) as views " \
        "FROM articles LEFT JOIN log on '/article/' || articles.slug = log.path " \
        "GROUP BY authorsID, articlesTitle, log.path order by views desc;"
cursor.execute(popularArticles)

# Query 1

print("Question 1: What are the most popular three articles of all time?\n")
firstQ = "SELECT articlesTitle, views " \
         "FROM popularArticles " \
         "limit 3;"
cursor.execute(firstQ)
results = cursor.fetchall()

# Printing 1st query's results
for row in results:
    print("\"", row[0], "\"", " -- ", row[1], " views")

# Query 2

print("\nQuestion 3: Who are the most popular article authors of all time?\n")
secondQ = "SELECT authors.name, SUM(views) as logs " \
          "FROM authors INNER JOIN popularArticles on authors.id = popularArticles.authorsID " \
          "GROUP BY authors.name order by logs desc;"

cursor.execute(secondQ)
results = cursor.fetchall()

# Printing 2nd query's results
for row in results:
    print(row[0], "--", row[1], " views")

# Query 3

print("\nQuestion 3: On which days did more than '1%' of requests lead to errors?\n")

# Creating (requests) view to be used in the third query
requests = "CREATE VIEW requests as "\
               "SELECT TO_CHAR(time,'MON DD,YYYY') as Date, Count(*) as Total, "\
               "Sum (CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END) as Errors "\
               "FROM log "\
               "GROUP BY Date "\
               "ORDER BY Date;"
cursor.execute(requests)

thirdQ = "SELECT Date, " \
         "round((CAST(Errors AS decimal) / Total) *100, 2) AS Result " \
         "FROM requests " \
         "WHERE round((CAST(Errors AS decimal)/ Total)* 100,2) > 1.00 " \
         "GROUP BY Date, Result " \
         "ORDER BY Date;"
cursor.execute(thirdQ)
results = cursor.fetchall()

# Printing 3rd query's results
for row in results:
    print(row[0], "--", row[1], "% errors")

cursor.close()
conn.close()