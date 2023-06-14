-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: database_facturacionybonificacion-sicte
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `table_facture`
--

DROP TABLE IF EXISTS `table_facture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table_facture` (
  `ID_Table_Facture` int NOT NULL,
  `CODIGO` varchar(100) DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `ALIADO` varchar(50) DEFAULT NULL,
  `MOVIL` varchar(50) DEFAULT NULL,
  `NOMBRE` varchar(50) DEFAULT NULL,
  `CEDILA` int DEFAULT NULL,
  `ELITE` varchar(50) DEFAULT NULL,
  `CUENTA` int DEFAULT NULL,
  `T_USER` varchar(50) DEFAULT NULL,
  `IDORDEN_DE_TRABAJO` int DEFAULT NULL,
  `CODCIUDAD` varchar(50) DEFAULT NULL,
  `CODNODO` varchar(50) DEFAULT NULL,
  `AREA` int DEFAULT NULL,
  `CECO` varchar(50) DEFAULT NULL,
  `CLASE` varchar(50) DEFAULT NULL,
  `FACTURADO` int DEFAULT NULL,
  `CANTIDAD_ACTIVIDAD` int DEFAULT NULL,
  `COMUNIDAD` varchar(50) DEFAULT NULL,
  `MODULO` varchar(50) DEFAULT NULL,
  `CARPETA` varchar(50) DEFAULT NULL,
  `TIPO_TRABAJO` varchar(50) DEFAULT NULL,
  `SUBTIPO_TRABAJO` varchar(50) DEFAULT NULL,
  `FECHA_CIERRE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_Table_Facture`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_facture`
--

LOCK TABLES `table_facture` WRITE;
/*!40000 ALTER TABLE `table_facture` DISABLE KEYS */;
/*!40000 ALTER TABLE `table_facture` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-05 12:56:14
