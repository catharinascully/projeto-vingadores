CREATE DATABASE  IF NOT EXISTS `vingadores` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `vingadores`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: vingadores
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `chip_gps`
--

DROP TABLE IF EXISTS `chip_gps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chip_gps` (
  `id_chip_gps` int NOT NULL AUTO_INCREMENT,
  `localizacao_atual` varchar(255) DEFAULT NULL,
  `ultima_localizacao` varchar(255) DEFAULT NULL,
  `id_tornozeleira` int NOT NULL,
  PRIMARY KEY (`id_chip_gps`),
  KEY `chip_tornozeleira_idx` (`id_tornozeleira`),
  CONSTRAINT `chip_tornozeleira` FOREIGN KEY (`id_tornozeleira`) REFERENCES `tornozeleira` (`id_tornozeleira`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chip_gps`
--

LOCK TABLES `chip_gps` WRITE;
/*!40000 ALTER TABLE `chip_gps` DISABLE KEYS */;
/*!40000 ALTER TABLE `chip_gps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `convocacao`
--

DROP TABLE IF EXISTS `convocacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `convocacao` (
  `id_convocacao` int NOT NULL AUTO_INCREMENT,
  `motivo` longtext NOT NULL,
  `data_convocacao` date NOT NULL,
  `data_comparecimento` date DEFAULT NULL,
  `status` enum('Pendente','Comparecido','Ausente') NOT NULL,
  `heroi_id` int NOT NULL,
  PRIMARY KEY (`id_convocacao`),
  KEY `heroi_id_idx` (`heroi_id`),
  CONSTRAINT `heroi_id` FOREIGN KEY (`heroi_id`) REFERENCES `heroi` (`heroi_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `convocacao`
--

LOCK TABLES `convocacao` WRITE;
/*!40000 ALTER TABLE `convocacao` DISABLE KEYS */;
INSERT INTO `convocacao` VALUES (5,'Missão secreta','2024-12-06','2024-10-10','Comparecido',9);
/*!40000 ALTER TABLE `convocacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `heroi`
--

DROP TABLE IF EXISTS `heroi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heroi` (
  `heroi_id` int NOT NULL AUTO_INCREMENT,
  `nome_heroi` varchar(45) DEFAULT NULL,
  `nome_real` varchar(45) DEFAULT NULL,
  `categoria` enum('Humano','Meta-Humano','Alienigena','Deidade') DEFAULT NULL,
  `poderes` varchar(255) DEFAULT NULL,
  `poder_principal` varchar(45) DEFAULT NULL,
  `fraquezas` varchar(255) DEFAULT NULL,
  `nivel_forca` bigint DEFAULT NULL,
  PRIMARY KEY (`heroi_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heroi`
--

LOCK TABLES `heroi` WRITE;
/*!40000 ALTER TABLE `heroi` DISABLE KEYS */;
INSERT INTO `heroi` VALUES (9,'Homem Aranha','Peter Parker','Meta-Humano','Teias, sentido aranha, agilidade','Sentido aranha','Danos físicos',4000),(10,'Pantera Negra ','T\'Challa','Meta-Humano','Agilidade, força sobre humana','Armadura','Pneumoultramicroscopicosilicovulcanoconiose',3000);
/*!40000 ALTER TABLE `heroi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mandado_de_prisao`
--

DROP TABLE IF EXISTS `mandado_de_prisao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mandado_de_prisao` (
  `id_mandado` int NOT NULL AUTO_INCREMENT,
  `heroi_id_mandado` int NOT NULL,
  `motivo_mandado` longtext NOT NULL,
  `status` enum('Ativo','Cumprido','Cancelado') NOT NULL,
  `data_emissao` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_mandado`),
  KEY `heroi_id_mandato_idx` (`heroi_id_mandado`),
  CONSTRAINT `heroi_id_mandato` FOREIGN KEY (`heroi_id_mandado`) REFERENCES `heroi` (`heroi_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mandado_de_prisao`
--

LOCK TABLES `mandado_de_prisao` WRITE;
/*!40000 ALTER TABLE `mandado_de_prisao` DISABLE KEYS */;
/*!40000 ALTER TABLE `mandado_de_prisao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tornozeleira`
--

DROP TABLE IF EXISTS `tornozeleira`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tornozeleira` (
  `id_tornozeleira` int NOT NULL AUTO_INCREMENT,
  `status` enum('Ativo','Inativo') NOT NULL,
  `data_ativacao` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data_desativacao` date DEFAULT NULL,
  `id_heroi` int NOT NULL,
  PRIMARY KEY (`id_tornozeleira`),
  KEY `tornozeleira_heroi_idx` (`id_heroi`),
  CONSTRAINT `tornozeleira_heroi` FOREIGN KEY (`id_heroi`) REFERENCES `heroi` (`heroi_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tornozeleira`
--

LOCK TABLES `tornozeleira` WRITE;
/*!40000 ALTER TABLE `tornozeleira` DISABLE KEYS */;
/*!40000 ALTER TABLE `tornozeleira` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'vingadores'
--

--
-- Dumping routines for database 'vingadores'
--
/*!50003 DROP PROCEDURE IF EXISTS `apagar_dados_heroi` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `apagar_dados_heroi`(
	 IN p_id_heroi INT 
)
BEGIN
	declare p_id_tornozeleira  INT;
	declare p_id_heroi_mandado INT;
    select id_tornozeleira into  p_id_tornozeleira from tornozeleira where id_heroi = p_id_heroi;
    delete from chip_gps where id_tornozeleira = p_id_tornozeleira;
    delete from tornozeleira where id_heroi = p_id_heroi;
    delete from convocacao where heroi_id = p_id_heroi;
    select heroi_id_mandado into p_id_heroi_mandado from mandado_de_prisao where heroi_id_mandado = p_id_heroi;
    delete from mandado_de_prisao where heroi_id_mandado = p_id_heroi;
    delete from heroi where heroi_id = p_id_heroi;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-06 14:33:15
