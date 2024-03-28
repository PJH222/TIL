create table analyze_db.TB_PBTRNSP
(
    STATN_NO        int         not null,
    STATN_NM        varchar(50) null,
    HO_LN           varchar(50) null,
    STD_MT          char(6)     not null,
    BEGIN_TIME      char(4)     not null,
    END_TIME        char(4)     not null,
    TKCAR_GFF_SE_CD char(2)     not null,
    NMPR_CNT        bigint      null,
    primary key (STATN_NO, STD_MT, BEGIN_TIME, END_TIME, TKCAR_GFF_SE_CD)
);

INSERT INTO TB_PBTRNSP (STATN_NO, STATN_NM, HO_LN, STD_MT, BEGIN_TIME, END_TIME, TKCAR_GFF_SE_CD, NMPR_CNT)
SELECT A.STATN_NO, A.STATN_NM, A.HO_LN, '202304' AS STD_MT
     , CASE WHEN A.LVL BETWEEN 1 AND 2 THEN '0400' WHEN A.LVL BETWEEN 3 AND 4 THEN '0500' WHEN A.LVL BETWEEN 5 AND 6 THEN '0600' WHEN A.LVL BETWEEN 7 AND 8 THEN '0700'
            WHEN A.LVL BETWEEN 9 AND 10 THEN '0800' WHEN A.LVL BETWEEN 11 AND 12 THEN '0900' WHEN A.LVL BETWEEN 13 AND 14 THEN '1000' WHEN A.LVL BETWEEN 15 AND 16 THEN '1100'
            WHEN A.LVL BETWEEN 17 AND 18 THEN '1200' WHEN A.LVL BETWEEN 19 AND 20 THEN '1300' WHEN A.LVL BETWEEN 21 AND 22 THEN '1400' WHEN A.LVL BETWEEN 23 AND 24 THEN '1500'
            WHEN A.LVL BETWEEN 25 AND 26 THEN '1600' WHEN A.LVL BETWEEN 27 AND 28 THEN '1700' WHEN A.LVL BETWEEN 29 AND 30 THEN '1800' WHEN A.LVL BETWEEN 31 AND 32 THEN '1900'
            WHEN A.LVL BETWEEN 33 AND 34 THEN '2000' WHEN A.LVL BETWEEN 35 AND 36 THEN '2100' WHEN A.LVL BETWEEN 37 AND 38 THEN '2200' WHEN A.LVL BETWEEN 39 AND 40 THEN '2300'
            WHEN A.LVL BETWEEN 41 AND 42 THEN '2400' WHEN A.LVL BETWEEN 43 AND 44 THEN '0100' WHEN A.LVL BETWEEN 45 AND 46 THEN '0200' WHEN A.LVL BETWEEN 47 AND 48 THEN '0300'
            ELSE '' END AS BEGIN_TIME
     , CASE WHEN A.LVL BETWEEN 1 AND 2 THEN '0500' WHEN A.LVL BETWEEN 3 AND 4 THEN '0600' WHEN A.LVL BETWEEN 5 AND 6 THEN '0700' WHEN A.LVL BETWEEN 7 AND 8 THEN '0800'
            WHEN A.LVL BETWEEN 9 AND 10 THEN '0900' WHEN A.LVL BETWEEN 11 AND 12 THEN '1000' WHEN A.LVL BETWEEN 13 AND 14 THEN '1100' WHEN A.LVL BETWEEN 15 AND 16 THEN '1200'
            WHEN A.LVL BETWEEN 17 AND 18 THEN '1300' WHEN A.LVL BETWEEN 19 AND 20 THEN '1400' WHEN A.LVL BETWEEN 21 AND 22 THEN '1500' WHEN A.LVL BETWEEN 23 AND 24 THEN '1600'
            WHEN A.LVL BETWEEN 25 AND 26 THEN '1700' WHEN A.LVL BETWEEN 27 AND 28 THEN '1800' WHEN A.LVL BETWEEN 29 AND 30 THEN '1900' WHEN A.LVL BETWEEN 31 AND 32 THEN '2000'
            WHEN A.LVL BETWEEN 33 AND 34 THEN '2100' WHEN A.LVL BETWEEN 35 AND 36 THEN '2200' WHEN A.LVL BETWEEN 37 AND 38 THEN '2300' WHEN A.LVL BETWEEN 39 AND 40 THEN '2400'
            WHEN A.LVL BETWEEN 41 AND 42 THEN '0100' WHEN A.LVL BETWEEN 43 AND 44 THEN '0200' WHEN A.LVL BETWEEN 45 AND 46 THEN '0300' WHEN A.LVL BETWEEN 47 AND 48 THEN '0400'
            ELSE '' END AS END_TIME
     , CASE WHEN MOD(A.LVL, 2) = 1 THEN 'TK'
            WHEN MOD(A.LVL, 2) = 0 THEN 'GF'
            ELSE '' END AS TKCAR_GFF_SE_CD
       , CASE WHEN A.LVL = 1  THEN FROM_04_HOUR_TO_05_HOUR_TK WHEN A.LVL = 2  THEN FROM_04_HOUR_TO_05_HOUR_GFF
            WHEN A.LVL = 3  THEN FROM_05_HOUR_TO_06_HOUR_TK WHEN A.LVL = 4  THEN FROM_05_HOUR_TO_06_HOUR_GFF
            WHEN A.LVL = 5  THEN FROM_06_HOUR_TO_07_HOUR_TK WHEN A.LVL = 6  THEN FROM_06_HOUR_TO_07_HOUR_GFF
            WHEN A.LVL = 7  THEN FROM_07_HOUR_TO_08_HOUR_TK WHEN A.LVL = 8  THEN FROM_07_HOUR_TO_08_HOUR_GFF
            WHEN A.LVL = 9  THEN FROM_08_HOUR_TO_09_HOUR_TK WHEN A.LVL = 10 THEN FROM_08_HOUR_TO_09_HOUR_GFF
            WHEN A.LVL = 11 THEN FROM_09_HOUR_TO_10_HOUR_TK WHEN A.LVL = 12 THEN FROM_09_HOUR_TO_10_HOUR_GFF
            WHEN A.LVL = 13 THEN FROM_10_HOUR_TO_11_HOUR_TK WHEN A.LVL = 14 THEN FROM_10_HOUR_TO_11_HOUR_GFF
            WHEN A.LVL = 15 THEN FROM_11_HOUR_TO_12_HOUR_TK WHEN A.LVL = 16 THEN FROM_11_HOUR_TO_12_HOUR_GFF
            WHEN A.LVL = 17 THEN FROM_12_HOUR_TO_13_HOUR_TK WHEN A.LVL = 18 THEN FROM_12_HOUR_TO_13_HOUR_GFF
            WHEN A.LVL = 19 THEN FROM_13_HOUR_TO_14_HOUR_TK WHEN A.LVL = 20 THEN FROM_13_HOUR_TO_14_HOUR_GFF
            WHEN A.LVL = 21 THEN FROM_14_HOUR_TO_15_HOUR_TK WHEN A.LVL = 22 THEN FROM_14_HOUR_TO_15_HOUR_GFF
            WHEN A.LVL = 23 THEN FROM_15_HOUR_TO_16_HOUR_TK WHEN A.LVL = 24 THEN FROM_15_HOUR_TO_16_HOUR_GFF
            WHEN A.LVL = 25 THEN FROM_16_HOUR_TO_17_HOUR_TK WHEN A.LVL = 26 THEN FROM_16_HOUR_TO_17_HOUR_GFF
            WHEN A.LVL = 27 THEN FROM_17_HOUR_TO_18_HOUR_TK WHEN A.LVL = 28 THEN FROM_17_HOUR_TO_18_HOUR_GFF
            WHEN A.LVL = 29 THEN FROM_18_HOUR_TO_19_HOUR_TK WHEN A.LVL = 30 THEN FROM_18_HOUR_TO_19_HOUR_GFF
            WHEN A.LVL = 31 THEN FROM_19_HOUR_TO_20_HOUR_TK WHEN A.LVL = 32 THEN FROM_19_HOUR_TO_20_HOUR_GFF
            WHEN A.LVL = 33 THEN FROM_20_HOUR_TO_21_HOUR_TK WHEN A.LVL = 34 THEN FROM_20_HOUR_TO_21_HOUR_GFF
            WHEN A.LVL = 35 THEN FROM_21_HOUR_TO_22_HOUR_TK WHEN A.LVL = 36 THEN FROM_21_HOUR_TO_22_HOUR_GFF
            WHEN A.LVL = 37 THEN FROM_22_HOUR_TO_23_HOUR_TK WHEN A.LVL = 38 THEN FROM_22_HOUR_TO_23_HOUR_GFF
            WHEN A.LVL = 39 THEN FROM_23_HOUR_TO_24_HOUR_TK WHEN A.LVL = 40 THEN FROM_23_HOUR_TO_24_HOUR_GFF
            WHEN A.LVL = 41 THEN FROM_24_HOUR_TO_01_HOUR_TK WHEN A.LVL = 42 THEN FROM_24_HOUR_TO_01_HOUR_GFF
            WHEN A.LVL = 43 THEN FROM_01_HOUR_TO_02_HOUR_TK WHEN A.LVL = 44 THEN FROM_01_HOUR_TO_02_HOUR_GFF
            WHEN A.LVL = 45 THEN FROM_02_HOUR_TO_03_HOUR_TK WHEN A.LVL = 46 THEN FROM_02_HOUR_TO_03_HOUR_GFF
            WHEN A.LVL = 47 THEN FROM_03_HOUR_TO_04_HOUR_TK WHEN A.LVL = 48 THEN FROM_03_HOUR_TO_04_HOUR_GFF
            ELSE 0 END AS NMPR_CNT
  FROM (
          SELECT A.*, B.LVL
            FROM TB_PBTRNSP_DATA A
            JOIN (SELECT 1 AS LVL UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6
                  UNION SELECT 7 UNION SELECT 8 UNION SELECT 9 UNION SELECT 10 UNION SELECT 11 UNION SELECT 12
                  UNION SELECT 13 UNION SELECT 14 UNION SELECT 15 UNION SELECT 16 UNION SELECT 17 UNION SELECT 18
                  UNION SELECT 19 UNION SELECT 20 UNION SELECT 21 UNION SELECT 22 UNION SELECT 23 UNION SELECT 24
                  UNION SELECT 25 UNION SELECT 26 UNION SELECT 27 UNION SELECT 28 UNION SELECT 29 UNION SELECT 30
                  UNION SELECT 31 UNION SELECT 32 UNION SELECT 33 UNION SELECT 34 UNION SELECT 35 UNION SELECT 36
                  UNION SELECT 37 UNION SELECT 38 UNION SELECT 39 UNION SELECT 40 UNION SELECT 41 UNION SELECT 42
                  UNION SELECT 43 UNION SELECT 44 UNION SELECT 45 UNION SELECT 46 UNION SELECT 47 UNION SELECT 48
                 ) B
     ) A
ORDER BY CAST(STATN_NO AS UNSIGNED), BEGIN_TIME, END_TIME;

SELECT *
FROM TB_PBTRNSP;

SELECT *
FROM TB_PBTRNSP_DATA;
-- TK 승차, GFF 하차, 

-- 역별 승차 / 하차 별로 인원수가 가장 많은 순으로 조회


WITH TMP1 AS (
	SELECT STATN_NO, 
		STATN_NM, 
		HO_LN,
		TKCAR_GFF_SE_CD, 
        SUM(NMPR_CNT) NMPR_CNT
	FROM TB_PBTRNSP
	WHERE NMPR_CNT > 0
	GROUP BY STATN_NO, STATN_NM, HO_LN, TKCAR_GFF_SE_CD
), TMP2 AS(
	SELECT STATN_NO, 
			STATN_NM, 
			HO_LN,
			IF(TKCAR_GFF_SE_CD = 'GF', NMPR_CNT , 0 ) AS GF,
			IF(TKCAR_GFF_SE_CD != 'GF', NMPR_CNT , 0 ) AS TK
	FROM TMP1
), TMP3 AS(
SELECT
	STATN_NO, 
	STATN_NM, 
    HO_LN,
	MAX(GF) GF , 
    MAX(TK) TK
FROM TMP2
GROUP BY STATN_NO, STATN_NM, HO_LN
)
SELECT 
	STATN_NO, 
	STATN_NM, 
    HO_LN,
    GF,
	TK
FROM TMP3
WHERE GF = (
		SELECT MAX(GF)
		FROM TMP3)
    OR TK = (
		SELECT MAX(TK)
        FROM TMP3)
	OR TK = (
		SELECT MIN(TK)
        FROM TMP3)
    OR GF = (
		SELECT MIN(GF)
		FROM TMP3)
;

-- 전체 데이터를 대상으로 승차 1등, 승차 꼴등, 하차 1등, 하차 꼴등 구하기
WITH TMP1 AS (
	SELECT STATN_NO, 
		STATN_NM, 
		HO_LN,
		TKCAR_GFF_SE_CD, 
        SUM(NMPR_CNT) NMPR_CNT
	FROM TB_PBTRNSP
	WHERE NMPR_CNT > 0
	GROUP BY STATN_NO, STATN_NM, HO_LN, TKCAR_GFF_SE_CD
), TMP2 AS(
	SELECT STATN_NO, 
			STATN_NM, 
			HO_LN,
			IF(TKCAR_GFF_SE_CD = 'GF', NMPR_CNT , 0 ) AS GF,
			IF(TKCAR_GFF_SE_CD != 'GF', NMPR_CNT , 0 ) AS TK
	FROM TMP1
), TMP3 AS(
SELECT
	STATN_NO, 
	STATN_NM, 
    HO_LN,
	MAX(GF) GF , 
    MAX(TK) TK
FROM TMP2
GROUP BY STATN_NO, STATN_NM, HO_LN
), TMP4 AS(
SELECT 
	STATN_NO, 
	STATN_NM, 
    HO_LN,
    GF,
	TK,
    RANK() OVER(ORDER BY TK) AS RANK_TK,
    RANK() OVER(ORDER BY GF) AS RANK_GF,
    RANK() OVER(ORDER BY TK DESC) AS RANK_TK_DESC,
    RANK() OVER(ORDER BY GF DESC) AS RANK_GF_DESC
FROM TMP3
)
SELECT STATN_NO, 
	STATN_NM, 
    HO_LN,
    GF,
	TK
FROM TMP4
WHERE RANK_TK = 1 OR RANK_GF = 1 OR RANK_TK_DESC = 1 OR RANK_GF_DESC = 1;

-- 출근 시간대 (07:00 ~ 08:00)애 허처 안유ㅗㄴ슈거 거정 많은 순으로 데이터 조회
WITH TMP1 AS (
	SELECT STATN_NO, 
		STATN_NM, 
		HO_LN,
		TKCAR_GFF_SE_CD, 
        SUM(NMPR_CNT) NMPR_CNT
	FROM TB_PBTRNSP
	WHERE NMPR_CNT > 0
	GROUP BY STATN_NO, STATN_NM, HO_LN, TKCAR_GFF_SE_CD
), TMP2 AS(
	SELECT STATN_NO, 
			STATN_NM, 
			HO_LN,
			IF(TKCAR_GFF_SE_CD = 'GF', NMPR_CNT , 0 ) AS GF,
			IF(TKCAR_GFF_SE_CD != 'GF', NMPR_CNT , 0 ) AS TK
	FROM TMP1
), TMP3 AS(
SELECT
	STATN_NO, 
	STATN_NM, 
    HO_LN,
	MAX(GF) GF , 
    MAX(TK) TK
FROM TMP2
GROUP BY STATN_NO, STATN_NM, HO_LN
)
SELECT 
	STATN_NO, 
	STATN_NM, 
    HO_LN,
    GF,
	TK,
    RANK() OVER(ORDER BY TK) AS RANK_TK,
    RANK() OVER(ORDER BY GF) AS RANK_GF,
    RANK() OVER(ORDER BY TK DESC) AS RANK_TK_DESC,
    RANK() OVER(ORDER BY GF DESC) AS RANK_GF_DESC
FROM TMP3
;

SELECT STATN_NO, STATN_NM, HO_LN, BEGIN_TIME, END_TIME, TKCAR_GFF_SE_CD, NMPR_CNT
FROM TB_PBTRNSP
WHERE BEGIN_TIME = 1800 AND END_TIME = 1900 AND TKCAR_GFF_SE_CD = 'TK'
ORDER BY NMPR_CNT DESC;

-- 2300 ~ 0400 사이 가장 많이 타는지 구하기
SELECT STATN_NO, STATN_NM, HO_LN, BEGIN_TIME, END_TIME, TKCAR_GFF_SE_CD, NMPR_CNT
FROM TB_PBTRNSP
WHERE (BEGIN_TIME,END_TIME) IN (('2300','2400'),
								('2400','0100'),
                                ('0100','0200'),
                                ('0200','0300'),
                                ('0300','0400')) 
	AND TKCAR_GFF_SE_CD = 'TK'
ORDER BY NMPR_CNT DESC;

