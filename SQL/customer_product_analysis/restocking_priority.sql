WITH 
prdct_perf_table AS (
SELECT SUM(quantityOrdered * priceEach) AS product_performance 
  FROM orderdetails AS od
 GROUP BY productCode
 ORDER BY product_performance DESC
 LIMIT 100
)

SELECT p.productCode, p.productName, p.productLine,
       ROUND(SUM(od.quantityOrdered) * 1.0 / p.quantityInStock, 2) AS stock_index,
       ROUND(SUM(quantityOrdered * priceEach), 2) AS product_performance,
       ROUND((LOG(ROUND(SUM(od.quantityOrdered) * 1.0 / p.quantityInStock, 2))*0.3) + (LOG(SUM(quantityOrdered * priceEach))*0.7), 2) AS priority
  FROM products AS p
  JOIN orderdetails AS od
    ON od.productCode = p.productCode
 GROUP BY p.productCode
HAVING product_performance IN (SELECT product_performance FROM prdct_perf_table)
 ORDER BY priority DESC
 LIMIT 10;
