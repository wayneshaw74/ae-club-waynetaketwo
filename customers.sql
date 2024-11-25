SELECT 
  c.id,
  c.name,
  c.email,
  min(o.created_at) AS first_order_at,
  COUNT (DISTINCT o.id) AS number_of_orders
FROM 
  `analytics-engineers-club.coffee_shop.orders` o
INNER JOIN
  `analytics-engineers-club.coffee_shop.customers` c
ON
  c.id = o.customer_id
Group BY 1,2,3
ORDER BY first_order_at 
LIMIT 5