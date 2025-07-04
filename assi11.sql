-- Q1) What is the total amount each customer spent at the restaurant?
SELECT CUSTOMER_ID, SUM(M.PRICE) AS TOTAL_AMOUNT FROM
SALES S JOIN MENU M ON M.PRODUCT_ID = S.PRODUCT_ID GROUP BY
CUSTOMER_ID;

-- Q2) How many days has each customer visited the restaurant?
SELECT CUSTOMER_ID, COUNT(DISTINCT ORDER_DATE) FROM SALES
GROUP BY CUSTOMER_ID;

-- Q3) What was the first item from the menu purchased by each customer?
SELECT S.CUSTOMER_ID, M.PRODUCT_NAME FROM MENU M JOIN
SALES S ON M.PRODUCT_ID = S.PRODUCT_ID WHERE (S.CUSTOMER_ID,
S.ORDER_DATE) IN (SELECT CUSTOMER_ID, MIN(ORDER_DATE) FROM SALES
GROUP BY CUSTOMER_ID);

-- Q4) What is the most purchased item on the menu and how many times was it
-- purchased by all customers?
 SELECT S.CUSTOMER_ID, M.PRODUCT_NAME, COUNT(*) AS
TIMES_PURCHASED
FROM SALES S JOIN MENU M ON S.PRODUCT_ID = M.PRODUCT_ID
WHERE S.PRODUCT_ID = (SELECT PRODUCT_ID
 FROM (
 SELECT PRODUCT_ID, COUNT(*) AS TOTAL_COUNT
 FROM SALES
 GROUP BY PRODUCT_ID)
WHERE TOTAL_COUNT = (
 SELECT MAX(TOTAL_COUNT)
  FROM (
  SELECT PRODUCT_ID, COUNT(*) AS TOTAL_COUNT
  FROM SALES
  GROUP BY PRODUCT_ID
  )
  )
  )
 GROUP BY S.CUSTOMER_ID, M.PRODUCT_NAME;

-- Q5Which item was the most popular for each customer

SELECT s.customer_id, m.product_name, COUNT(*) AS total_count
  FROM sales s
  JOIN menu m ON s.product_id = m.product_id
  GROUP BY s.customer_id, s.product_id
  HAVING COUNT(*) = (
  SELECT MAX(cnt) FROM (
  SELECT COUNT(*) AS cnt
  FROM sales
  WHERE customer_id = s.customer_id
  GROUP BY product_id
  ) AS counts
  );

-- Q6Which item was purchased first by the customer after they became a member?
SELECT
  s.customer_id,
  s.order_date,
  m.product_name
  FROM sales s
  JOIN members mem
  ON s.customer_id = mem.customer_id
  JOIN menu m
  ON s.product_id = m.product_id
  WHERE s.order_date = (
  SELECT MIN(order_date)
  FROM sales
  WHERE customer_id = s.customer_id
  AND order_date >= mem.join_date
  )
  ;
-- Q7) Which item was purchased just before the customer became a member?
SELECT
  s.customer_id,
  s.order_date,mem.join_date,
  m.product_name
  FROM sales s
  JOIN members mem
  ON s.customer_id = mem.customer_id
  JOIN menu m
  ON s.product_id = m.product_id
  WHERE s.order_date = (
  SELECT MAX(order_date)
  FROM sales
  WHERE customer_id = s.customer_id
  AND order_date < mem.join_date
  )
  ;

-- Q8) What is the total items and amount spent for each member before they became a
-- member?
SELECT
 s.customer_id,
 COUNT(*) AS total_items_before_membership,
 SUM(m.price) AS total_amount_spent_before_membership
 FROM sales s
 JOIN menu m
 ON s.product_id = m.product_id
 JOIN members mem
 ON s.customer_id = mem.customer_id
 WHERE s.order_date < mem.join_date
 GROUP BY s.customer_id;

--  Q9) If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many
-- points would each customer have?
SELECT
  s.customer_id,
  SUM(
  CASE
  WHEN m.product_name = 'sushi' THEN m.price * 20
  ELSE m.price * 10
  END
  ) AS total_points
  FROM sales s
  JOIN menu m ON s.product_id = m.product_id
  GROUP BY s.customer_id;

-- Q10) In the first week after a customer joins the program (including their join date)
-- they earn 2x points on all items, not just sushi - how many points do customer A and B
-- have at the end of January?
SELECT 
    c.customer_id,
    SUM(
        CASE 
            -- If in first week after join (inclusive)
            WHEN t.order_date BETWEEN c.join_date AND DATE_ADD(c.join_date, INTERVAL 6 DAY) THEN amount_spent * 10 * 2
            -- If it's sushi (but outside first week)
            WHEN t.item = 'sushi' THEN amount_spent * 10 * 2
            -- Regular case
            ELSE amount_spent * 10
        END
    ) AS total_points
FROM CUSTOMERS c
JOIN TRANSACTIONS t ON c.customer_id = t.customer_id
WHERE t.order_date BETWEEN '2023-01-01' AND '2023-01-31'
  AND c.customer_id IN ('A', 'B')
GROUP BY c.customer_id;
