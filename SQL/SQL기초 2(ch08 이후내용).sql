CREATE TABLE user(
	user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(50) NOT NULL,
	address VARCHAR(100)
);

INSERT INTO user(username, address) 
VALUES ('A', '서울'),
			 ('B', '대전'),
			 ('C', '경기도'),
		   ('D', NULL),
			 ('E', NULL),
			 ('F', '서울'),
			 ('G', '경기도'),
			 ('H', '대구'),
			 ('I', '부산'),
			 ('J', '전주'),
			 ('K', '광주');
             
             
SELECT address, ISNULL(address) FROM user;
SELECT username, IFNULL(address, '주소없음') FROM user;

SELECT 
	address, 
    IF(address ='경기도' , '수도권', '지방')
FROM user;

SELECT 
	address, 
    IF(address ='경기도' OR address ='서울', '수도권', '지방')
FROM user;

SELECT 
	address, 
    IF(address ='경기도' OR address ='서울', '수도권',
    IF(address ='대전', '충청권', 
    IF(address ='부산' OR address ='대구', '경상권',
    IF(address ='전주' OR address ='광주', '전라권', 
    IF(address = NULL, '주소없음', '1')))))
FROM user;

SELECT
	address,
    CASE
		WHEN address = "경기도" OR address = "서울" THEN "수도권"
        WHEN address = "대전" THEN "충청권"
        WHEN address = "부산" OR address = "대구" THEN "경상권"
        ELSE "전라권"
	END AS KR_AREA
FROM user;

SELECT
	stock_quantity,
    CASE
		WHEN stock_quantity >= 50 THEN '제고많음'
		WHEN stock_quantity >= 30 THEN '제고중간'
		ELSE '재고없음'
	END AS quantity_level
FROM books;

-- 두 차이를 느껴라
SELECT DISTINCT author_lname FROM books;
SELECT DISTINCT author_lname, title FROM books;

SELECT * FROM books;
SELECT * FROM books LIMIT 4;




