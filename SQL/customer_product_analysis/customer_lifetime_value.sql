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
 
 SELECT ROUND(AVG(profit),2) AS LTV
   FROM profit_per_customer AS ppc;