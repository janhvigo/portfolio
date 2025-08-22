USE airbnb;

-- 1. Which neighborhoods generate the most revenue?
SELECT 
    neighbourhood,
    SUM(price * number_of_reviews) AS total_revenue
FROM 
    listings
GROUP BY 
    neighbourhood
ORDER BY 
    total_revenue DESC;


-- 2. What are the cheapest listings with good review counts?
SELECT 
    name, 
    neighbourhood, 
    price
FROM 
    listings
WHERE 
    price < 50 AND number_of_reviews > 10
ORDER BY 
    price ASC;

-- 3. What is the average price per room type?
SELECT 
    room_type,
    MIN(price) AS min_price,
    AVG(price) AS avg_price,
    MAX(price) AS max_price
FROM 
    listings
GROUP BY 
    room_type;

-- 4. Which listings received the most reviews overall?
SELECT 
    l.id, 
    l.name, 
    COUNT(r.date) AS total_reviews
FROM 
    listings l
JOIN 
    reviews r ON l.id = r.listing_id
GROUP BY 
    l.id, l.name
ORDER BY 
    total_reviews DESC
LIMIT 10;

-- 5. What is the cumulative number of reviews per listing by month? (Window function)
SELECT 
    listing_id,
    DATE_FORMAT(date, '%Y-%m') AS month,
    COUNT(*) OVER (
        PARTITION BY listing_id 
        ORDER BY date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_reviews
FROM 
    reviews;

-- 6. Classify listings into value categories using CASE
SELECT 
    name, 
    neighbourhood, 
    price, 
    number_of_reviews,
    CASE
        WHEN price < 50 AND number_of_reviews > 100 THEN 'Top Budget Pick'
        WHEN price BETWEEN 50 AND 100 AND number_of_reviews > 50 THEN 'Best Mid-Range'
        ELSE 'Niche or Premium'
    END AS category
FROM 
    listings;

-- 7. Which neighborhoods had the most reviews in 2025? 
WITH last_year_reviews AS (
    SELECT 
        listing_id, 
        date
    FROM 
        reviews
    WHERE 
        date >= '2025-01-01'
)
SELECT 
    l.neighbourhood, 
    COUNT(*) AS review_count
FROM 
    last_year_reviews r
JOIN 
    listings l ON r.listing_id = l.id
GROUP BY 
    l.neighbourhood
ORDER BY 
    review_count DESC
LIMIT 10;
