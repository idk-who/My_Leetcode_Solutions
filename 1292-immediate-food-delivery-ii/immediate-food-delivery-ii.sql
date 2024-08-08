SELECT 
    ROUND(
        SUM(IF(D1.mi_od=D1.cp_dd, 1, 0))*100
        /COUNT(D1.mi_od),
        2
    ) immediate_percentage
FROM
    (
        SELECT
            MIN(order_date) mi_od, MIN(customer_pref_delivery_date) cp_dd
        FROM
            Delivery
        GROUP BY
            customer_id
    ) D1;
