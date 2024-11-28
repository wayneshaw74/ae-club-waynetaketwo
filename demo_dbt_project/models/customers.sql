{{  config(
    materialized ='table'
) }}

select 
  customers.id,
  customers.name,
  customers.email,
  min(orders.created_at) AS first_order_at,
  count(distinct orders.id) AS number_of_orders,
  sum(orders.total) as total_order_value
from `analytics-engineers-club.coffee_shop.orders` orders
inner join `analytics-engineers-club.coffee_shop.customers` customers on customers.id = orders.customer_id
group by 1,2,3
order by first_order_at 
