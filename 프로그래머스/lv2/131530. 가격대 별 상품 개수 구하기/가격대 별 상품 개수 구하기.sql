# -- 코드를 입력하세요
# SELECT1
# 2
# 3
# 4
# 5
# SELECT (PRICE-PRICE%10000) AS PRICE_GROUP, COUNT(*) AS PRODUCTS
# FROM PRODUCT 
# GROUP BY PRICE_GROUP
# ORDER BY PRICE_GROUP
# ;

SELECT (PRICE-PRICE%10000) AS PRICE_GROUP,count(*) as products
FROM PRODUCT 
GROUP BY PRICE_GROUP
order by price_group asc