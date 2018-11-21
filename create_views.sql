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