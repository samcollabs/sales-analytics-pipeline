select
    "Invoice" as invoice_number,
    "StockCode" as stock_code,
    "Description" as description,
    "Quantity" as quantity,
    case when "Quantity" < 0 then true else false end as is_return,
    "InvoiceDate" as invoice_date,
    "Price" as unit_price,
    coalesce("Customer ID", -1) as customer_id,
    "Country" as country
from {{ source('raw', 'raw_sales') }}
where "Price" > 0