SELECT
    activity_date day, 
    COUNT(DISTINCT user_id) active_users
FROM
    Activity
WHERE
    DATE_SUB(DATE("2019-07-27"), INTERVAL 30 DAY) < activity_date 
    AND activity_date <= DATE("2019-07-27")
GROUP BY
    activity_date