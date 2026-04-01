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
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifications` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `tenant_id` int(11) DEFAULT NULL,
  `type` enum('Urgent','Reminder') NOT NULL,
  `message` longtext NOT NULL,
  `is_read` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `location_id` int(11) DEFAULT NULL,
  `subject` longtext DEFAULT NULL,
  PRIMARY KEY (`notification_id`),
  KEY `location_id` (`location_id`),
  KEY `tenant_id` (`tenant_id`),
  CONSTRAINT `notifications_ibfk_1` FOREIGN KEY (`tenant_id`) REFERENCES `tenants` (`tenant_id`),
  CONSTRAINT `notifications_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `locations` (`location_id`),
  CONSTRAINT `notifications_ibfk_3` FOREIGN KEY (`tenant_id`) REFERENCES `tenants` (`tenant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
INSERT INTO `notifications` VALUES (1,5,'Urgent','The water in the building will be shut off on 06/11/2026 between 9:00 and 14:00 due to planned maintenance, apologies for any inconvinience.',1,'2026-10-10 09:05:00',NULL,'Water Maintenance 06/11/2026'),(2,5,'Urgent','We detected a water leak reported near your unit. Maintenance may need access within 24 hours. Please contact the office immediately.',1,'2026-03-22 23:06:33',NULL,'Urgent: Maintenance Access Required'),(3,5,'Reminder','Your lease renewal offer is now available. Please review and respond by the end of the month.',1,'2026-03-22 23:06:33',NULL,'Lease Renewal Notice'),(4,5,'Reminder','This is a friendly reminder that your parking permit expires in 7 days. Renew it to avoid towing penalties.',1,'2026-03-22 23:06:33',NULL,'Parking Permit Expiration'),(5,5,'Urgent','A package has been held at the leasing office for more than 5 days. Please pick it up as soon as possible.',1,'2026-03-22 23:06:33',NULL,'Package Pickup Required'),(6,NULL,'Reminder','Pest control services will be conducted on Friday between 9 AM and 12 PM. Please ensure pets are secured.',1,'2026-03-22 23:13:46',1,'Scheduled Pest Control'),(7,NULL,'Urgent','Water will be shut off for the entire building tomorrow from 10 AM to 2 PM due to emergency repairs.',1,'2026-03-22 23:13:46',1,'Urgent: Water Shutdown Notice'),(8,NULL,'Reminder','The pool area will be closed this weekend for routine cleaning and maintenance.',1,'2026-03-22 23:13:46',1,'Pool Maintenance Notice'),(9,NULL,'Reminder','Join us for the community BBQ this Saturday at 3 PM in the courtyard. All residents are welcome!',1,'2026-03-22 23:13:46',1,'Community BBQ Event'),(10,NULL,'Urgent','Severe weather alert: Please secure balcony items and avoid unnecessary travel until conditions improve.',1,'2026-03-22 23:13:46',1,'Severe Weather Advisory'),(11,NULL,'Urgent','There will be a building wide fire alarm test on 04/04/2026 at 10am. If it rings for more than 10 minutes, assume a real fire and proceed to the fire assembly points.',1,'2026-04-01 05:50:34',1,'Fire Alarm Test'),(13,1,'Urgent','test',1,'2026-04-01 06:02:25',NULL,'test'),(14,NULL,'Urgent','The wifi is out please do not worry we are in the process of fixing it.',0,'2026-04-01 11:32:23',1,'Wifi outage'),(15,NULL,'Urgent','The wifi is out again please use the availble hotspots',0,'2026-04-01 12:00:49',1,'Wifi Outage');
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-01 14:47:07
