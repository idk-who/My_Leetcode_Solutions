SELECT 
    id 
FROM 
    Weather outer_query
WHERE 
    temperature > (
        SELECT 
            inner_query.temperature 
        FROM 
            Weather inner_query 
        WHERE inner_query.recordDate = DATE_ADD(outer_query.recordDate, INTERVAL -1 DAY)    
    );