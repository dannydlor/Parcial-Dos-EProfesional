-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: calendario
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `espacioacd`
--

DROP TABLE IF EXISTS `espacioacd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `espacioacd` (
  `idespacioacd` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `semestre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idespacioacd`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `espacioacd`
--

LOCK TABLES `espacioacd` WRITE;
/*!40000 ALTER TABLE `espacioacd` DISABLE KEYS */;
INSERT INTO `espacioacd` VALUES (1,'matematicas','semestre-8'),(2,'programacion-1','semestre-9');
/*!40000 ALTER TABLE `espacioacd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estudiantes`
--

DROP TABLE IF EXISTS `estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiantes` (
  `idestudent` int NOT NULL AUTO_INCREMENT,
  `identificacion` varchar(45) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `celular` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `semestre` varchar(45) DEFAULT NULL,
  `idespacioacd` int NOT NULL,
  PRIMARY KEY (`idestudent`,`idespacioacd`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiantes`
--

LOCK TABLES `estudiantes` WRITE;
/*!40000 ALTER TABLE `estudiantes` DISABLE KEYS */;
INSERT INTO `estudiantes` VALUES (1,'1124862267','edinson ','meneses','3106658317','edinson@gmai.com','semestre-4',1),(2,'1124862267','calros ','jurado','3123456785','calros@gamil.com','semestre-4',1),(3,'1123769877','ana','perez','3223343433','eana@gmail.com','semestre-6',2),(6,'','Jairo','Ortiz','3123456856','ortiz@gamil.com','Semestre IV',2),(7,'11234567983','Jonier','Perez','3123456856','eidf@gamilc.om','Semestre IX',1),(8,'11234567983','Jonier','Perez','3123456856','eidf@gamilc.om','Semestre IX',1);
/*!40000 ALTER TABLE `estudiantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sesion_estudiantes`
--

DROP TABLE IF EXISTS `sesion_estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sesion_estudiantes` (
  `idsesion_estudiantes` int NOT NULL AUTO_INCREMENT,
  `idsesion` int NOT NULL,
  `idestudiante` int NOT NULL,
  `asistencia` tinyint DEFAULT NULL,
  PRIMARY KEY (`idsesion_estudiantes`,`idsesion`,`idestudiante`),
  KEY `fk_sesion_idx` (`idsesion`),
  KEY `fk_estudiante_idx` (`idestudiante`),
  CONSTRAINT `fk_estudiante` FOREIGN KEY (`idestudiante`) REFERENCES `estudiantes` (`idestudent`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_sesion` FOREIGN KEY (`idsesion`) REFERENCES `sesiones` (`idsesiones`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sesion_estudiantes`
--

LOCK TABLES `sesion_estudiantes` WRITE;
/*!40000 ALTER TABLE `sesion_estudiantes` DISABLE KEYS */;
/*!40000 ALTER TABLE `sesion_estudiantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sesiones`
--

DROP TABLE IF EXISTS `sesiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sesiones` (
  `idsesiones` int NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `hora_inicio` varchar(20) NOT NULL,
  `hora_final` varchar(45) NOT NULL,
  `asignatura` varchar(45) NOT NULL,
  PRIMARY KEY (`idsesiones`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sesiones`
--

LOCK TABLES `sesiones` WRITE;
/*!40000 ALTER TABLE `sesiones` DISABLE KEYS */;
INSERT INTO `sesiones` VALUES (19,'2020-04-28','9:45','10:45','matematicas'),(20,'2021-04-07','18:30','21:45','matematicas');
/*!40000 ALTER TABLE `sesiones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-28 16:44:19
