# SELECT A.FOOD_TYPE, A.REST_ID, A.REST_NAME, A.FAVORITES
# FROM REST_INFO AS A JOIN (
#     SELECT FOOD_TYPE, MAX(FAVORITES) AS FAVORITES
#     FROM REST_INFO
#     GROUP BY FOOD_TYPE
# ) AS B ON A.FOOD_TYPE = B.FOOD_TYPE
# WHERE A.FAVORITES = B.FAVORITES
# ORDER BY FOOD_TYPE DESC

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM (
    SELECT *, RANK() OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS RNK
    FROM REST_INFO
) AS R
WHERE RNK = 1
ORDER BY FOOD_TYPE DESC