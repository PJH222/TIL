CREATE DATABASE analyze_db;

create table analyze_db.TB_POPLTN_DATA
(
    ADMINIST_ZONE             text   null,
    TOT_POPLTN_CO             bigint null,
    AGE_SCTN_POPLTN_CO        bigint null,
    POPLTN_CO_0_9             bigint null,
    POPLTN_CO_10_19           bigint null,
    POPLTN_CO_20_29           bigint null,
    POPLTN_CO_30_39           bigint null,
    POPLTN_CO_40_49           bigint null,
    POPLTN_CO_50_59           bigint null,
    POPLTN_CO_60_69           bigint null,
    POPLTN_CO_70_79           bigint null,
    POPLTN_CO_80_89           bigint null,
    POPLTN_CO_90_99           bigint null,
    POPLTN_CO_100             bigint null,
    MALE_TOT_POPLTN_CO        bigint null,
    MALE_AGE_SCTN_POPLTN_CO   bigint null,
    MALE_POPLTN_CO_0_9        bigint null,
    MALE_POPLTN_CO_10_19      bigint null,
    MALE_POPLTN_CO_20_29      bigint null,
    MALE_POPLTN_CO_30_39      bigint null,
    MALE_POPLTN_CO_40_49      bigint null,
    MALE_POPLTN_CO_50_59      bigint null,
    MALE_POPLTN_CO_60_69      bigint null,
    MALE_POPLTN_CO_70_79      bigint null,
    MALE_POPLTN_CO_80_89      bigint null,
    MALE_POPLTN_CO_90_99      bigint null,
    MALE_POPLTN_CO_100        bigint null,
    FEMALE_TOT_POPLTN_CO      bigint null,
    FEMALE_AGE_SCTN_POPLTN_CO bigint null,
    FEMALE_POPLTN_CO_0_9      bigint null,
    FEMALE_POPLTN_CO_10_19    bigint null,
    FEMALE_POPLTN_CO_20_29    bigint null,
    FEMALE_POPLTN_CO_30_39    bigint null,
    FEMALE_POPLTN_CO_40_49    bigint null,
    FEMALE_POPLTN_CO_50_59    bigint null,
    FEMALE_POPLTN_CO_60_69    bigint null,
    FEMALE_POPLTN_CO_70_79    bigint null,
    FEMALE_POPLTN_CO_80_89    bigint null,
    FEMALE_POPLTN_CO_90_99    bigint null,
    FEMALE_POPLTN_CO_100      bigint null
);

USE analyze_db;

create table analyze_db.TB_PBTRNSP_DATA
(
    DE                          text   null,
    HO_LN                       text   null,
    STATN_NO                    bigint null,
    STATN_NM                    text   null,
    FROM_04_HOUR_TO_05_HOUR_TK  bigint null,
    FROM_04_HOUR_TO_05_HOUR_GFF bigint null,
    FROM_05_HOUR_TO_06_HOUR_TK  bigint null,
    FROM_05_HOUR_TO_06_HOUR_GFF bigint null,
    FROM_06_HOUR_TO_07_HOUR_TK  bigint null,
    FROM_06_HOUR_TO_07_HOUR_GFF bigint null,
    FROM_07_HOUR_TO_08_HOUR_TK  bigint null,
    FROM_07_HOUR_TO_08_HOUR_GFF bigint null,
    FROM_08_HOUR_TO_09_HOUR_TK  bigint null,
    FROM_08_HOUR_TO_09_HOUR_GFF bigint null,
    FROM_09_HOUR_TO_10_HOUR_TK  bigint null,
    FROM_09_HOUR_TO_10_HOUR_GFF bigint null,
    FROM_10_HOUR_TO_11_HOUR_TK  bigint null,
    FROM_10_HOUR_TO_11_HOUR_GFF bigint null,
    FROM_11_HOUR_TO_12_HOUR_TK  bigint null,
    FROM_11_HOUR_TO_12_HOUR_GFF bigint null,
    FROM_12_HOUR_TO_13_HOUR_TK  bigint null,
    FROM_12_HOUR_TO_13_HOUR_GFF bigint null,
    FROM_13_HOUR_TO_14_HOUR_TK  bigint null,
    FROM_13_HOUR_TO_14_HOUR_GFF bigint null,
    FROM_14_HOUR_TO_15_HOUR_TK  bigint null,
    FROM_14_HOUR_TO_15_HOUR_GFF bigint null,
    FROM_15_HOUR_TO_16_HOUR_TK  bigint null,
    FROM_15_HOUR_TO_16_HOUR_GFF bigint null,
    FROM_16_HOUR_TO_17_HOUR_TK  bigint null,
    FROM_16_HOUR_TO_17_HOUR_GFF bigint null,
    FROM_17_HOUR_TO_18_HOUR_TK  bigint null,
    FROM_17_HOUR_TO_18_HOUR_GFF bigint null,
    FROM_18_HOUR_TO_19_HOUR_TK  bigint null,
    FROM_18_HOUR_TO_19_HOUR_GFF bigint null,
    FROM_19_HOUR_TO_20_HOUR_TK  bigint null,
    FROM_19_HOUR_TO_20_HOUR_GFF bigint null,
    FROM_20_HOUR_TO_21_HOUR_TK  bigint null,
    FROM_20_HOUR_TO_21_HOUR_GFF bigint null,
    FROM_21_HOUR_TO_22_HOUR_TK  bigint null,
    FROM_21_HOUR_TO_22_HOUR_GFF bigint null,
    FROM_22_HOUR_TO_23_HOUR_TK  bigint null,
    FROM_22_HOUR_TO_23_HOUR_GFF bigint null,
    FROM_23_HOUR_TO_24_HOUR_TK  bigint null,
    FROM_23_HOUR_TO_24_HOUR_GFF bigint null,
    FROM_24_HOUR_TO_01_HOUR_TK  bigint null,
    FROM_24_HOUR_TO_01_HOUR_GFF bigint null,
    FROM_01_HOUR_TO_02_HOUR_TK  bigint null,
    FROM_01_HOUR_TO_02_HOUR_GFF bigint null,
    FROM_02_HOUR_TO_03_HOUR_TK  bigint null,
    FROM_02_HOUR_TO_03_HOUR_GFF bigint null,
    FROM_03_HOUR_TO_04_HOUR_TK  bigint null,
    FROM_03_HOUR_TO_04_HOUR_GFF bigint null,
    WORK_DT                     text   null
);

-- 확인용
USE analyze_db;
DESC TB_POPLTN_DATA;
DESC TB_PBTRNSP_DATA;

SELECT * FROM TB_POPLTN_DATA;
SELECT * FROM TB_PBTRNSP_DATA;
-- 보기 좋은 데이터, 분석하기 좋은 데이터
-- 컬럼에 집계의 기준이 들어있는 경우, 집계가 불가능하다!
-- ex) 나이대 별 등 ~~ 별이라는 기준이 컬럼에 있는 경우에는 불가능하다

-- 집계가 가능한 형태로 데이터를 바꿔 보겠다!
create table analyze_db.TB_POPLTN
(
    ADMINIST_ZONE_NO varchar(10)  not null,
    ADMINIST_ZONE_NM varchar(150) null,
    STD_MT           varchar(6)   not null,
    POPLTN_SE_CD     varchar(1)   not null,
    AGRDE_SE_CD      varchar(3)   not null,
    POPLTN_CNT       int          null,
    primary key (ADMINIST_ZONE_NO, STD_MT, POPLTN_SE_CD, AGRDE_SE_CD)
);

INSERT INTO TB_POPLTN
SELECT A.ADMINIST_ZONE_NO, A.ADMINIST_ZONE_NM, A.STD_MT
     , CASE WHEN LVL1 = 1 THEN 'M' WHEN LVL1 = 2 THEN 'F' WHEN LVL1 = 3 THEN 'T' END AS POPLTN_SE_CD
     , CASE WHEN LVL2 = 1  THEN '000' WHEN LVL2 = 2  THEN '010' WHEN LVL2 = 3  THEN '020'
            WHEN LVL2 = 4  THEN '030' WHEN LVL2 = 5  THEN '040' WHEN LVL2 = 6  THEN '050'
            WHEN LVL2 = 7  THEN '060' WHEN LVL2 = 8  THEN '070' WHEN LVL2 = 9  THEN '080'
            WHEN LVL2 = 10 THEN '090' WHEN LVL2 = 11 THEN '100'
       END AS AGRDE_SE_CD
     , CASE WHEN LVL1 = 1 AND LVL2 = 1  THEN MALE_POPLTN_CO_0_9     WHEN LVL1 = 1 AND LVL2 = 2  THEN MALE_POPLTN_CO_10_19
            WHEN LVL1 = 1 AND LVL2 = 3  THEN MALE_POPLTN_CO_20_29   WHEN LVL1 = 1 AND LVL2 = 4  THEN MALE_POPLTN_CO_30_39
            WHEN LVL1 = 1 AND LVL2 = 5  THEN MALE_POPLTN_CO_40_49   WHEN LVL1 = 1 AND LVL2 = 6  THEN MALE_POPLTN_CO_50_59
            WHEN LVL1 = 1 AND LVL2 = 7  THEN MALE_POPLTN_CO_60_69   WHEN LVL1 = 1 AND LVL2 = 8  THEN MALE_POPLTN_CO_70_79
            WHEN LVL1 = 1 AND LVL2 = 9  THEN MALE_POPLTN_CO_80_89   WHEN LVL1 = 1 AND LVL2 = 10 THEN MALE_POPLTN_CO_90_99
            WHEN LVL1 = 1 AND LVL2 = 11 THEN MALE_POPLTN_CO_100     WHEN LVL1 = 2 AND LVL2 = 1  THEN FEMALE_POPLTN_CO_0_9
            WHEN LVL1 = 2 AND LVL2 = 2  THEN FEMALE_POPLTN_CO_10_19 WHEN LVL1 = 2 AND LVL2 = 3  THEN FEMALE_POPLTN_CO_20_29
            WHEN LVL1 = 2 AND LVL2 = 4  THEN FEMALE_POPLTN_CO_30_39 WHEN LVL1 = 2 AND LVL2 = 5  THEN FEMALE_POPLTN_CO_40_49
            WHEN LVL1 = 2 AND LVL2 = 6  THEN FEMALE_POPLTN_CO_50_59 WHEN LVL1 = 2 AND LVL2 = 7  THEN FEMALE_POPLTN_CO_60_69
            WHEN LVL1 = 2 AND LVL2 = 8  THEN FEMALE_POPLTN_CO_70_79 WHEN LVL1 = 2 AND LVL2 = 9  THEN FEMALE_POPLTN_CO_80_89
            WHEN LVL1 = 2 AND LVL2 = 10 THEN FEMALE_POPLTN_CO_90_99 WHEN LVL1 = 2 AND LVL2 = 11 THEN FEMALE_POPLTN_CO_100
            WHEN LVL1 = 3 AND LVL2 = 1  THEN POPLTN_CO_0_9          WHEN LVL1 = 3 AND LVL2 = 2  THEN POPLTN_CO_10_19
            WHEN LVL1 = 3 AND LVL2 = 3  THEN POPLTN_CO_20_29        WHEN LVL1 = 3 AND LVL2 = 4  THEN POPLTN_CO_30_39
            WHEN LVL1 = 3 AND LVL2 = 5  THEN POPLTN_CO_40_49        WHEN LVL1 = 3 AND LVL2 = 6  THEN POPLTN_CO_50_59
            WHEN LVL1 = 3 AND LVL2 = 7  THEN POPLTN_CO_60_69        WHEN LVL1 = 3 AND LVL2 = 8  THEN POPLTN_CO_70_79
            WHEN LVL1 = 3 AND LVL2 = 9  THEN POPLTN_CO_80_89        WHEN LVL1 = 3 AND LVL2 = 10 THEN POPLTN_CO_90_99
            WHEN LVL1 = 3 AND LVL2 = 11 THEN POPLTN_CO_100 END AS POPLTN_CNT
  FROM
     (
      SELECT SUBSTR(ADMINIST_ZONE, INSTR(ADMINIST_ZONE, '(') + 1, 10) AS ADMINIST_ZONE_NO
           , SUBSTR(ADMINIST_ZONE, 1, INSTR(ADMINIST_ZONE, '(')-1) AS ADMINIST_ZONE_NM,
             '202304' AS STD_MT
           , MALE_POPLTN_CO_0_9    , MALE_POPLTN_CO_10_19  , MALE_POPLTN_CO_20_29
           , MALE_POPLTN_CO_30_39  , MALE_POPLTN_CO_40_49  , MALE_POPLTN_CO_50_59
           , MALE_POPLTN_CO_60_69  , MALE_POPLTN_CO_70_79  , MALE_POPLTN_CO_80_89  , MALE_POPLTN_CO_90_99  , MALE_POPLTN_CO_100
           , FEMALE_POPLTN_CO_0_9  , FEMALE_POPLTN_CO_10_19, FEMALE_POPLTN_CO_20_29
           , FEMALE_POPLTN_CO_30_39, FEMALE_POPLTN_CO_40_49, FEMALE_POPLTN_CO_50_59
           , FEMALE_POPLTN_CO_60_69, FEMALE_POPLTN_CO_70_79, FEMALE_POPLTN_CO_80_89, FEMALE_POPLTN_CO_90_99, FEMALE_POPLTN_CO_100
           , POPLTN_CO_0_9         , POPLTN_CO_10_19, POPLTN_CO_20_29
           , POPLTN_CO_30_39       , POPLTN_CO_40_49, POPLTN_CO_50_59
           , POPLTN_CO_60_69       , POPLTN_CO_70_79, POPLTN_CO_80_89, POPLTN_CO_90_99, POPLTN_CO_100
           , LVL1, LVL2
        FROM TB_POPLTN_DATA,
             (SELECT (tmp1.idx) AS LVL1 FROM (SELECT 1 as idx UNION SELECT 2 UNION SELECT 3) tmp1) LVL1,
             (SELECT (tmp2.idx) AS LVL2 FROM (SELECT 1 as idx UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9 UNION SELECT 10 UNION SELECT 11) tmp2) LVL2
     ) A ;

SELECT * FROM TB_POPLTN_DATA;     
SELECT * FROM TB_POPLTN;