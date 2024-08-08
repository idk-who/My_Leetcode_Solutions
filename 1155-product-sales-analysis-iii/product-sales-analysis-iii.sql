SELECT
    P.product_id,
    S.year first_year,
    S.quantity,
    S.price
FROM
    Product P
JOIN
    Sales S
ON
    P.product_id = S.product_id
WHERE
    (P.product_id, year)
IN
    (
        SELECT
            P.product_id,
            MIN(year) first_year
        FROM
            Product P
        JOIN
            Sales S
        ON
            P.product_id = S.product_id
        GROUP BY
            P.product_id
    );

