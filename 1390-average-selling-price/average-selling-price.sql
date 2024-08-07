SELECT
    P.product_id, 
    IFNULL(
        ROUND(
            SUM(U.units * P.price)/SUM(U.units),
            2
        ),
        0
    ) average_price
FROM
    Prices P
LEFT JOIN
    UnitsSold U
ON
    P.product_id = U.product_id
    AND U.purchase_date >= P.start_date 
    AND U.purchase_date <= P.end_date
GROUP BY
    P.product_id;