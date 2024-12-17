with source_dbt_wstndp as (
    select * from {{ source('dbt_wstndp', 'montly_customers') }} as monthly_customers
)