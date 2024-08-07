SELECT 
    name, bonus 
FROM 
    Employee E
LEFT JOIN
    Bonus B
ON
    E.empId = B.empId
WHERE 
    bonus IS NULL or bonus < 1000;