SELECT b.BOOK_ID AS BOOK_ID, A.AUTHOR_NAME AS AUTHOR_NAME,
TO_CHAR(b.PUBLISHED_DATE,'yyyy-mm-dd') AS PUBLISHED_DATE
FROM BOOK b 
join AUTHOR a
on b.AUTHOR_ID=a.AUTHOR_ID
where b.CATEGORY='경제'
ORDER BY b.PUBLISHED_DATE;

-- FROM TABLE B 
-- JOIN TABLE A 
-- ON B.C = A.C