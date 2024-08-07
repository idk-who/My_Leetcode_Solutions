SELECT
    M.name
FROM
    Employee E
JOIN
    Employee M
ON
    E.managerId = M.id
GROUP BY
    E.managerId
HAVING
    COUNT(E.managerId) >= 5;