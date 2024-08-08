SELECT
    product_id,
    year first_year,
    quantity,
    price
FROM
    Sales S
WHERE
    (product_id, year)
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

