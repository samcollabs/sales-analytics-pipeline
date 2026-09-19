select
    date_trunc('day', invoice_date) as sale_date,
    count(distinct invoice_number) as number_of_orders,
    sum(case when is_return = false then quantity * unit_price else 0 end) as gross_revenue,
    sum(case when is_return = true then quantity * unit_price else 0 end) as returns_value,
    sum(quantity * unit_price) as net_revenue
from {{ ref('stg_sales') }}
group by date_trunc('day', invoice_date)
order by sale_date