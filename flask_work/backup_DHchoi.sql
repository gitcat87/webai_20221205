-- --------------------------------------------------------
-- 호스트:                          192.168.0.80
-- 서버 버전:                        8.0.32 - MySQL Community Server - GPL
-- 서버 OS:                        Linux
-- HeidiSQL 버전:                  12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- DHchoi 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `DHchoi` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `DHchoi`;

-- 테이블 DHchoi.book 구조 내보내기
CREATE TABLE IF NOT EXISTS `book` (
  `idx` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `desc` text,
  `cata` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 DHchoi.book:~5 rows (대략적) 내보내기
INSERT INTO `book` (`idx`, `title`, `desc`, `cata`) VALUES
	(1, '', '씨에스에스', 'css_sprites1.png'),
	(2, '', '123', 'jackpot.jpg'),
	(6, 'JAVAProgramming', 'JAVA공부할수 있는데', 'aa.png'),
	(7, 'JAVAProgramming', 'JAVA공부할수 있는데', 'aa.png'),
	(9, 'djfuqek', 'djfudnj', 'pot.jpg');

-- 테이블 DHchoi.files 구조 내보내기
CREATE TABLE IF NOT EXISTS `files` (
  `idx` int NOT NULL AUTO_INCREMENT,
  `ko` varchar(255) DEFAULT NULL,
  `en` varchar(255) DEFAULT NULL,
  `filename` varchar(20) DEFAULT NULL,
  `regdate` datetime DEFAULT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 DHchoi.files:~4 rows (대략적) 내보내기
INSERT INTO `files` (`idx`, `ko`, `en`, `filename`, `regdate`) VALUES
	(7, '한국말', '영어말', 'MeganHernandez', '2023-01-12 05:39:46'),
	(9, '한국말', '영어말', 'KevinMarshall', '2023-01-12 05:40:27'),
	(10, '한국말', '영어말', 'ReginaTaylor', '2023-01-12 05:54:48'),
	(11, '한국말', '영어말', 'MoniqueAlvarado', '2023-01-12 05:54:55');

-- 테이블 DHchoi.freeboard 구조 내보내기
CREATE TABLE IF NOT EXISTS `freeboard` (
  `idx` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `content` text,
  `writer` varchar(50) DEFAULT NULL,
  `hits` int DEFAULT '0',
  `regdate` datetime DEFAULT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 DHchoi.freeboard:~13 rows (대략적) 내보내기
INSERT INTO `freeboard` (`idx`, `title`, `content`, `writer`, `hits`, `regdate`) VALUES
	(1, 'ㅏㅏㅏㅏ', 'ㅏㅏㅏㅏ', 'ㅏㅏㅏㅏ', 0, '2023-01-27 05:20:34'),
	(2, 'aaa', 'bbb', 'ccc', 0, '2023-01-27 05:21:15'),
	(5, '테스트', '테스1ㄴㅇㅇㅇㅇ', '테스슷', 0, '2023-01-30 05:35:48'),
	(6, 'aaa', 'bbb', 'ccc', 0, '2023-01-30 05:43:57'),
	(7, 'aaa', 'bbb', 'ccc', 0, '2023-01-30 06:11:58'),
	(8, 'aaa', 'bbb', 'ccc', 0, '2023-01-30 06:21:10'),
	(9, 'aaa', 'bbb', 'ccc', 0, '2023-01-31 05:06:29'),
	(10, 'aaa', 'bbb', 'ccc', 0, '2023-02-01 06:09:23'),
	(11, 'aaa', 'bbb', 'ccc', 0, '2023-02-01 06:09:29'),
	(12, 'aaa', 'bbb', 'ccc', 0, '2023-02-01 06:09:36'),
	(13, 'aaa', 'bbb', 'ccc', 0, '2023-02-01 06:09:44'),
	(14, '고쳤습니당', '매우 어렵습니다', '하하하', 0, '2023-02-01 06:26:37'),
	(15, 'ㅇㄹㄹㄴㅇㄹㅇㄴ', 'ㄴㅇㄹㄴㅇㄹㄴㅇㅇㄹㄴㄴㄷ', 'ㄴㄷㄹㄴㄷㄹ', 0, '2023-02-01 06:27:04');

-- 테이블 DHchoi.TB_A 구조 내보내기
CREATE TABLE IF NOT EXISTS `TB_A` (
  `aaa` int DEFAULT NULL,
  `bbb` int DEFAULT NULL,
  `ccc` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 DHchoi.TB_A:~9 rows (대략적) 내보내기
INSERT INTO `TB_A` (`aaa`, `bbb`, `ccc`) VALUES
	(10, 20, '내용'),
	(10, 20, '내용'),
	(10, 20, '내용'),
	(300, 100, '내용내용내용'),
	(10, 20, '내용'),
	(99, 2354, '글자입니다'),
	(11, 22, '33'),
	(12, 24, '24'),
	(100, 100, '100'),
	(100, 100, '100');

-- 테이블 DHchoi.test1 구조 내보내기
CREATE TABLE IF NOT EXISTS `test1` (
  `aa` varchar(20) DEFAULT NULL,
  `bb` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 DHchoi.test1:~2 rows (대략적) 내보내기
INSERT INTO `test1` (`aa`, `bb`) VALUES
	('선생님', '잘생겼네요'),
	('재미가', '없네요');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
