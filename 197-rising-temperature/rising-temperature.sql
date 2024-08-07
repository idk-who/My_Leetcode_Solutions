SELECT 
    outer_query.id 
FROM 
    Weather outer_query
WHERE 
    outer_query.temperature > (
        SELECT 
            inner_query.temperature 
        FROM 
            Weather inner_query 
        WHERE DATEDIFF(inner_query.recordDate, outer_query.recordDate) = -1  
    );