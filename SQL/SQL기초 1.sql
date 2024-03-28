USE book_shop;

CREATE TABLE books 
	(
		book_id INT NOT NULL AUTO_INCREMENT,
		title VARCHAR(100),
		author_fname VARCHAR(100),
		author_lname VARCHAR(100),
		released_year INT,
		stock_quantity INT,
		pages INT,
		PRIMARY KEY(book_id)
	);

INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES
('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343);

SELECT * FROM books;

SELECT CONCAT('HELLO', ' ', 'MYSQL') AS concat_sample FROM DUAL;

SELECT CONCAT(author_fname,' ', author_lname) AS full_name FROM books;
-- 집가고 싶다아앙
SELECT CONCAT(title, '-', released_year) as title_year FROM books;

-- 둘차이를 비교해 보세요~~
SELECT CONCAT(title,'-', author_fname,'-', released_year) FROM books;
SELECT CONCAT_WS(' - ', title, author_fname, released_year) FROM books;

-- 원하는 순서의 글자를 뽑기, 둘 차이를 비교해보기
SELECT SUBSTRING('Hologram', 3);
SELECT SUBSTRING('Hologram', 3,3);

SELECT CONCAT(SUBSTRING(title, 1, 10), '...') AS SUMMARY_TITLE
FROM books;

-- 느낌표를 바꾸기
SELECT REPLACE('HELLO WORLD!', '!', '?');

-- 문자 치환하기
SELECT REPLACE('I LOVE YOU', 'LOVE', 'LIKE');

SELECT REPLACE(title, ' ', '_') FROM books;

-- 문자열의 길이를 정확하게 재기위해서는 CHAR_LENGTH를 사용해라
SELECT LENGTH("MINHO"), CHAR_LENGTH("MINHO");
SELECT LENGTH("민호"), CHAR_LENGTH("민호");

-- 여백 지우기, 각 세 가지 경우의 차이를 찾아봐라
SELECT TRIM("                   MINGO       ");
SELECT TRIM(LEADING ' ' FROM "                   MINGO       ");
-- "MINGO       "
SELECT TRIM(BOTH ' ' FROM "                   MINGO       ");
-- "MINGO"
SELECT TRIM(TRAILING ' ' FROM "                   MINGO       ");
-- "                   MINGO"
SELECT TRIM(BOTH ' #' FROM "                   MINGO       #");
-- "                   MINGO      "

