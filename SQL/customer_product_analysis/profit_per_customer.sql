WITH
profit_per_customer AS (
SELECT o.customerNumber,
	   SUM(od.quantityOrdered * (od.priceEach - p.buyPrice)) AS profit
  FROM orders AS o
  JOIN orderdetails AS od
    ON o.orderNumber = od.orderNumber
  JOIN products AS p
    ON od.productCode = p.productCode
 GROUP BY customerNumber
 )

SELECT c.contactLastName, c.contactFirstName, c.city, c.country,
	   ppc.profit
  FROM customers AS c
  JOIN profit_per_customer AS ppc
    ON ppc.customerNumber = c.customerNumber
 ORDER BY profit DESC
 LIMIT 5;