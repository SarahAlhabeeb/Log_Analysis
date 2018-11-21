#!/usr/bin/env python3

import psycopg2

conn = psycopg2.connect(database="news")
cursor = conn.cursor()

# Query 1

print("Question 1: What are the most popular three articles of all time?\n")
firstQ = """
         SELECT articlesTitle,
               views
         FROM popularArticles
         LIMIT 3;
         """

cursor.execute(firstQ)
results = cursor.fetchall()

# Printing 1st query's results
for title, views in results:
        print("\"{}\" -- {} views".format(title, views))

# Query 2

print("\nQuestion 3: Who are the most popular article authors of all time?\n")

secondQ = """
          SELECT authors.name,
          SUM(views) AS logs
          FROM authors
          INNER JOIN popularArticles ON authors.id = popularArticles.authorsID
          GROUP BY authors.name
          ORDER BY logs DESC;
          """
cursor.execute(secondQ)
results = cursor.fetchall()

# Printing 2nd query's results
for author, views in results:
        print("{} -- {} views".format(author, views))

# Query 3

print("\nQuestion 3: On which days did more than '1%' of requests "
      "lead to errors?\n")

thirdQ = """
         SELECT Date, round((CAST(Errors AS decimal) / Total) *100, 2)
                AS RESULT
         FROM requests
         WHERE round((CAST(Errors AS decimal)/ Total)* 100, 2) > 1.00
         GROUP BY Date, RESULT
         ORDER BY Date;
         """
cursor.execute(thirdQ)
results = cursor.fetchall()

# Printing 3rd query's results
for date, percent in results:
        print("{} -- {} errors".format(date, percent))
cursor.close()
conn.close()
