CREATE DATABASE  IF NOT EXISTS `s1_sdgp_prod` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `s1_sdgp_prod`;
-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: 135.181.2.74    Database: s1_sdgp_prod
-- ------------------------------------------------------
-- Server version	5.5.5-10.6.23-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tenants`
--

DROP TABLE IF EXISTS `tenants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tenants` (
  `tenant_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `national_insurance` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `occupation` enum('Employed','Student','Part-Time','Unemployed') DEFAULT NULL,
  `references` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`tenant_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tenants`
--

LOCK TABLES `tenants` WRITE;
/*!40000 ALTER TABLE `tenants` DISABLE KEYS */;
INSERT INTO `tenants` VALUES (1,'Peter','Test','111','peter@gmail.com','1234','1','Employed',NULL),(3,'Peter','Test','123','peter2@gmail.com','','07777777','Employed',NULL),(4,'Max','Jones','1234556','max@gmail.com','123','0777772','Student',NULL),(5,'harry','potter','12345','harry@gmail.com','hedwig','07777','Employed',NULL),(22,'Max','Jones','123123','max','1234','31232131','Employed',NULL),(26,'wasdzfzf','esfesf','fesf','esf','esf','esf','Employed',NULL),(27,'awdfef','wdfaswed','waddaw','wdadwa','dwa','wadwad','Student',NULL),(29,'dwaddwa','awdw','dwad','dwadwa','dwadaw','dwadaw','Student',NULL),(30,'dwadwa','awd','dwada','wdada','dwadwa','waddwa','Student',NULL),(31,'mia','andaya','123456','1234@gmail.com','1234','077','Student',NULL),(32,'mia','andaya','1234567','123@hotmail.com','1234','077','Student',NULL),(33,'wadwa','wadwadd','wad','dwad','wad','dwadaw','Student',NULL),(34,'dwa','dwadaw','dwadwa','waddwa','dwdadwa','dwadwa','Student',NULL),(35,'lol','lol','458rut','weofnwr','irnpenv','34r3454','Student',NULL),(36,'s','sdas','s','s','s','s','Unemployed',NULL),(37,'dwaawd','dwa','wad','wad','wad','wad','Student',NULL),(38,'2fovindvn','odvnaen','dsvonadvn','0dfvkzjnd','zdbonad;b','3984ru340570','Student',NULL),(39,'wad','dwaAAAAA','wda','wd','wad','dwawad','Student',NULL),(40,'test','\'zdbnpzd\'n','svno','zdfbn','\'afbno','evrpin','Student',NULL),(41,'wefpjwf','aergatg','sgbn','stbart','sgb','atbr','Student',NULL),(42,'d','daw','adw','adw','adw','daw','Student',NULL),(43,'Testing','testing','11111111','testing@gmail.com','1234','111111111','Student',NULL),(44,'Testing 1','Test','1111','testing11@gmail.com','12344','1111','Student',NULL);
/*!40000 ALTER TABLE `tenants` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-01 14:47:15
