select
  date_trunc(first_order_at, month) date_month,
  count(*) as new_customers
 
from {{ ref('customers') }}
 
group by 1