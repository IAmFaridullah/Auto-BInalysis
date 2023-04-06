-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: auto_binalysisdb
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `acquitted_datasets`
--

DROP TABLE IF EXISTS `acquitted_datasets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acquitted_datasets` (
  `Ds_Name` varchar(25) NOT NULL,
  `User` varchar(100) NOT NULL,
  `Ds_Path` varchar(55) NOT NULL,
  `Ds_Created` datetime NOT NULL,
  PRIMARY KEY (`Ds_Name`,`User`),
  UNIQUE KEY `Ds_Path` (`Ds_Path`),
  KEY `User` (`User`),
  CONSTRAINT `acquitted_datasets_ibfk_1` FOREIGN KEY (`User`) REFERENCES `client_details` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acquitted_datasets`
--

LOCK TABLES `acquitted_datasets` WRITE;
/*!40000 ALTER TABLE `acquitted_datasets` DISABLE KEYS */;
/*!40000 ALTER TABLE `acquitted_datasets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `Username` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `Admin_Name` varchar(100) NOT NULL,
  `Admin_Gender` varchar(6) NOT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES ('iamadmin','password123','Farid ullah','Male');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add client_details',7,'add_client_details'),(26,'Can change client_details',7,'change_client_details'),(27,'Can delete client_details',7,'delete_client_details'),(28,'Can view client_details',7,'view_client_details'),(29,'Can add admin',8,'add_admin'),(30,'Can change admin',8,'change_admin'),(31,'Can delete admin',8,'delete_admin'),(32,'Can view admin',8,'view_admin'),(33,'Can add chat',9,'add_chat'),(34,'Can change chat',9,'change_chat'),(35,'Can delete chat',9,'delete_chat'),(36,'Can view chat',9,'view_chat'),(37,'Can add trained model',10,'add_trainedmodel'),(38,'Can change trained model',10,'change_trainedmodel'),(39,'Can delete trained model',10,'delete_trainedmodel'),(40,'Can view trained model',10,'view_trainedmodel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$390000$lOIrYQ75kwhHIEwC3IHxSx$L7bkMZ9btdk7HrR6DU3J3Zhq9Sl4hK4FWSvLc524BqY=','2023-01-12 15:56:55.529597',1,'admin','','','admin@gmail.com',1,1,'2023-01-12 06:57:13.288343'),(2,'pbkdf2_sha256$390000$iKso6FME4NXdgdsyvyiAeh$nVvFPIR4xrkJmaa6zVocH1ewdFvekpKS1MovFha08/Y=',NULL,1,'AutoAdmin','','','autoadmin@gmail.com',1,1,'2023-01-12 08:34:25.609486');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_details`
--

DROP TABLE IF EXISTS `client_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client_details` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `Client_Type` varchar(255) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `Client_Gender` enum('Male','Female') NOT NULL,
  `Account_Name` varchar(100) NOT NULL,
  `org_name` varchar(100) NOT NULL,
  `org_city` varchar(100) NOT NULL,
  `org_country` varchar(100) NOT NULL,
  `Last_Login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL DEFAULT '0',
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `Username_UNIQUE` (`username`),
  UNIQUE KEY `Email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_details`
--

LOCK TABLES `client_details` WRITE;
/*!40000 ALTER TABLE `client_details` DISABLE KEYS */;
INSERT INTO `client_details` VALUES ('iamelliot','pbkdf2_sha256$390000$J7XmzDi1PLso5RwqLOliwD$hVktrevpEog+klrTj8rGZQ7ZAOUXbzEQPDOjqd1PLlU=',NULL,'elliot@db.com','Male','Elliot Alderson','Google','New york','pakistan',NULL,0,1),('iamfaridullah','pbkdf2_sha256$390000$2SilYJiPyzrDHSsObBDIow$ATGwGyHWDUbeRjQ5civs5pH4HeLrXXUMhMFGNBMdQZI=','','faridullahkhan645@gmail.com','Male','Faridullah khan','Google','New york','Usa','2023-03-14 19:02:07',0,1),('iammrrobot','pbkdf2_sha256$390000$ZEGJJX0YzFGnhLwy6QLOIf$0b2B5cy6GTeU+rlIS/EmNtvLSa+GuhsR3TQ08qNNVWQ=',NULL,'muzamil@db.com','Male','Muzammil khan','Google','New york','pakistan',NULL,0,1),('iammuzammil','pbkdf2_sha256$390000$vL6cJKWvqrCjedylUEVaHh$WVrYXTyakbF+R56D1ooozmBDEo+IefVyOF+/aYFJJAU=',NULL,'randommail@email.com','Male','Muzammil khan','eziline','rawalpindi','pakistan',NULL,0,1);
/*!40000 ALTER TABLE `client_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(10,'analysis','trainedmodel'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(8,'chatbot','admin'),(9,'chatbot','chat'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'userauthentication','client_details');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-01-08 08:16:21.006352'),(2,'auth','0001_initial','2023-01-08 08:16:23.356319'),(3,'admin','0001_initial','2023-01-08 08:16:23.492888'),(4,'admin','0002_logentry_remove_auto_add','2023-01-08 08:16:23.514711'),(5,'admin','0003_logentry_add_action_flag_choices','2023-01-08 08:16:23.521517'),(6,'contenttypes','0002_remove_content_type_name','2023-01-08 08:16:23.606137'),(7,'auth','0002_alter_permission_name_max_length','2023-01-08 08:16:23.623606'),(8,'auth','0003_alter_user_email_max_length','2023-01-08 08:16:23.642125'),(9,'auth','0004_alter_user_username_opts','2023-01-08 08:16:23.650102'),(10,'auth','0005_alter_user_last_login_null','2023-01-08 08:16:23.714726'),(11,'auth','0006_require_contenttypes_0002','2023-01-08 08:16:23.718022'),(12,'auth','0007_alter_validators_add_error_messages','2023-01-08 08:16:23.726190'),(13,'auth','0008_alter_user_username_max_length','2023-01-08 08:16:23.742737'),(14,'auth','0009_alter_user_last_name_max_length','2023-01-08 08:16:23.759687'),(15,'auth','0010_alter_group_name_max_length','2023-01-08 08:16:23.779609'),(16,'auth','0011_update_proxy_permissions','2023-01-08 08:16:23.786945'),(17,'auth','0012_alter_user_first_name_max_length','2023-01-08 08:16:23.805580'),(18,'sessions','0001_initial','2023-01-08 08:16:23.858678'),(19,'userauthentication','0001_initial','2023-01-08 08:49:43.700038'),(20,'userauthentication','0002_alter_signupform_table','2023-01-08 08:49:43.708844'),(21,'userauthentication','0003_rename_signupform_client_details','2023-01-08 08:49:43.711837'),(22,'userauthentication','0002_remove_client_details_age_remove_client_details_id_and_more','2023-03-12 17:56:55.878491'),(23,'userauthentication','0003_remove_client_details_age_remove_client_details_id_and_more','2023-03-12 18:00:14.970742'),(24,'userauthentication','0004_client_details_is_active','2023-03-12 20:57:01.034017'),(25,'userauthentication','0005_alter_client_details_table','2023-03-13 15:35:40.985159'),(26,'userauthentication','0006_alter_client_details_table','2023-03-14 17:27:26.312795'),(27,'userauthentication','0007_alter_client_details_table','2023-03-14 17:27:26.320792'),(28,'userauthentication','0008_alter_client_details_table','2023-03-14 18:23:52.760090'),(29,'chatbot','0001_initial','2023-03-15 21:34:34.276625'),(30,'chatbot','0002_alter_chat_table','2023-03-15 21:40:51.009180'),(31,'chatbot','0003_alter_chat_table','2023-03-15 21:40:51.039029'),(32,'chatbot','0004_alter_chat_table','2023-03-15 21:42:00.894612'),(33,'chatbot','0005_delete_chat','2023-03-15 21:55:33.258431'),(34,'chatbot','0006_chat','2023-03-15 21:56:22.366119'),(35,'chatbot','0007_alter_chat_admin_username','2023-03-15 22:02:54.107841'),(36,'chatbot','0008_alter_chat_admin_username_alter_chat_username','2023-03-18 20:24:52.938932'),(37,'chatbot','0009_alter_chat_admin_username','2023-03-18 20:24:52.947924'),(38,'userauthentication','0009_rename_username_client_details_username','2023-03-18 20:39:09.342989'),(39,'chatbot','0010_alter_chat_chat_id','2023-03-19 20:22:04.085953'),(40,'chatbot','0011_alter_chat_chat_id','2023-03-19 20:32:38.114244'),(41,'chatbot','0012_rename_cbot_ans_chat_message_and_more','2023-03-26 16:21:13.693286'),(42,'userauthentication','0010_rename_username_client_details_username','2023-03-26 16:21:13.782285'),(43,'chatbot','0013_alter_chat_reciever','2023-03-26 16:24:49.838000'),(44,'chatbot','0014_remove_chat_reciever_remove_chat_sender_and_more','2023-03-26 20:22:41.249464'),(45,'analysis','0001_initial','2023-04-06 08:39:15.290853');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preprocessed_datasets`
--

DROP TABLE IF EXISTS `preprocessed_datasets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `preprocessed_datasets` (
  `PDs_Name` varchar(25) NOT NULL,
  `User` varchar(100) NOT NULL,
  `PDs_Path` varchar(55) NOT NULL,
  `PDs_Created` datetime NOT NULL,
  PRIMARY KEY (`PDs_Name`,`User`),
  UNIQUE KEY `PDs_Path` (`PDs_Path`),
  KEY `User` (`User`),
  CONSTRAINT `preprocessed_datasets_ibfk_1` FOREIGN KEY (`PDs_Name`) REFERENCES `acquitted_datasets` (`Ds_Name`),
  CONSTRAINT `preprocessed_datasets_ibfk_2` FOREIGN KEY (`User`) REFERENCES `client_details` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preprocessed_datasets`
--

LOCK TABLES `preprocessed_datasets` WRITE;
/*!40000 ALTER TABLE `preprocessed_datasets` DISABLE KEYS */;
/*!40000 ALTER TABLE `preprocessed_datasets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trained_models`
--

DROP TABLE IF EXISTS `trained_models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trained_models` (
  `id` char(32) NOT NULL,
  `model_name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `model_path` varchar(255) NOT NULL,
  `model_for` varchar(255) NOT NULL,
  `accuracy` double NOT NULL,
  `rmse` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trained_models`
--

LOCK TABLES `trained_models` WRITE;
/*!40000 ALTER TABLE `trained_models` DISABLE KEYS */;
INSERT INTO `trained_models` VALUES ('114390bacda9429d93fcdfba1d3e0a2d','Member Churn.pkl','iamfaridullah','analysis\\trained-models\\user_iamfaridullah\\Member Churn.pkl','S1',0.7720797720797721,0.1),('51699a2792514770a422eda7ff8c0aa1','Member Card Analysis Data.pkl','iamfaridullah','analysis\\trained-models\\user_iamfaridullah\\Member Card Analysis Data.pkl','S1',0.91,0.1),('65bc08d7f93049cf89d2bc963247b239','Member Card Analysis Data.pkl','iamfaridullah','analysis\\trained-models\\user_iamfaridullah\\Member Card Analysis Data.pkl','S1',0.92,0.1);
/*!40000 ALTER TABLE `trained_models` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-06 22:17:26
