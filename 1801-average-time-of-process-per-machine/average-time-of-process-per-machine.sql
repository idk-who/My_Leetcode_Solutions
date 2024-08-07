SELECT 
    machine_id,
    ROUND(
        SUM(
            CASE
                WHEN activity_type = 'end' THEN timestamp
                WHEN activity_type = 'start' THEN -timestamp
            END
        )/(COUNT(*)/2),
        3
    )
     as processing_time
FROM
    Activity
GROUP BY
    machine_id;

-- FROM
--     Activity A1
-- JOIN
--     Activity A2
-- ON
--     A1.machine_id = A2.machine_id AND
--     A1.process_id = A2.process_id AND
