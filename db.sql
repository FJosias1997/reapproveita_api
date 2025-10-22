-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (x86_64)
--
-- Host: 127.0.0.1    Database: reapproveita_db
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `categoria_produtos`
--

DROP TABLE IF EXISTS `categoria_produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria_produtos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria_produtos`
--

LOCK TABLES `categoria_produtos` WRITE;
/*!40000 ALTER TABLE `categoria_produtos` DISABLE KEYS */;
INSERT INTO `categoria_produtos` VALUES (1,'Frutas'),(2,'Bebidas'),(3,'Conservas'),(4,'Macarrão'),(5,'Verduras'),(6,'Legumes'),(7,'Diversos');
/*!40000 ALTER TABLE `categoria_produtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos`
--

DROP TABLE IF EXISTS `produtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `codigo` int DEFAULT NULL,
  `supermercado_id` int DEFAULT NULL,
  `categoria_id` int DEFAULT NULL,
  `preco` decimal(7,2) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `descricao_produto` varchar(10000) DEFAULT NULL,
  `image_url` text,
  PRIMARY KEY (`id`),
  KEY `supermercado_id` (`supermercado_id`),
  KEY `categoria_id` (`categoria_id`),
  CONSTRAINT `produtos_ibfk_1` FOREIGN KEY (`supermercado_id`) REFERENCES `supermercados` (`id`),
  CONSTRAINT `produtos_ibfk_2` FOREIGN KEY (`categoria_id`) REFERENCES `categoria_produtos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos`
--

LOCK TABLES `produtos` WRITE;
/*!40000 ALTER TABLE `produtos` DISABLE KEYS */;
INSERT INTO `produtos` VALUES (1,102030,1,1,10.00,'Banana Prata','Contém 12 bananas no cacho','https://drive.google.com/uc?export=view&id=11tZpJ51rZJL7c6ckjqIp2saiz5-7JH1-'),(2,202020,2,1,6.99,'1kg de Maracujá','Contém 1kg de Maracujá','https://drive.google.com/uc?export=view&id=16sYDOI7hyJTrc31HrF70QHnqc-BXoIXf'),(3,303030,3,1,8.50,'Peras Sortidas','Contém várias peras','https://drive.google.com/uc?export=view&id=1EVkNLEwhT93xFdkmHqSUU5eyqRtFo8Gi'),(4,404040,4,1,10.00,'1L Açaí','1lt de Açaí','https://drive.google.com/uc?export=view&id=1liq9uU-w2GIP4lsHczGPZF_4j6D20XMu'),(5,881001,2,2,6.99,'Refrigerante Coca-Cola 2L','Garrafa PET de Coca-Cola sabor Original 2 litros.','https://demo11.webbvendas.com.br/_core/_uploads/148/2024/03/1156310324if58icfghg.jpg'),(6,881002,4,3,4.29,'Milho Verde Quero 170g','Lata de milho verde em conserva, peso drenado 170g.','https://destro.fbitsstatic.net/img/p/milho-verde-quero-lata-170g-71296/257832-1.jpg?w=500&h=500&v=202501231555&qs=ignore'),(7,881003,1,4,9.50,'Macarrão Espaguete Barilla 500g','Macarrão de sêmola grano duro, n.5.','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQljbuBvRLsCqAaFvRRz59-Ikde6udYmygw0w&s'),(8,881004,3,5,3.99,'Alface Crespa (Unidade)','Alface crespa fresca, higienizada, 1 unidade.','https://shizenorganicos.com.br/wp-content/uploads/2020/12/alface_crespa-removebg-preview.png'),(9,881005,2,6,4.75,'Cenoura (Aprox. 500g)','Cenouras frescas, aproximadamente 500g.','https://cdn.awsli.com.br/300x300/2283/2283132/produto/273214079/bffac282bd2d4c0bd7d9ae4bfb1c21c8-mg2d7de0qz.jpeg'),(10,881006,1,7,16.90,'Feijão Carioca','1kg de Feijão Carioca','https://essareceitafunciona.com.br/wp-content/uploads/2024/04/Receita-de-feijao-carioca-Essa-Receita-Funciona-5-500x500.jpg'),(11,881007,4,2,13.99,'Suco de Laranja Prats 900ml','Suco de laranja 100% natural, sem adição de açúcar.','https://saborecia.com.br/wp-content/uploads/2020/06/prats.jpg'),(12,881008,3,6,5.99,'Batata Inglesa 1kg','Batata inglesa lavada, pacote 1kg.','https://www.confianca.com.br/ccstore/v1/images/?source=/file/v6837510435172723105/products/1144782.1.jpg&height=940&width=940'),(13,881009,1,3,11.50,'Atum Sólido Gomes da Costa 170g','Atum sólido ao natural em lata, 170g.','https://mercantilnovaera.vtexassets.com/arquivos/ids/195675/Atum-Solido-ao-Natural-GOMES-DA-COSTA-Lata-120g.jpg?v=637798417077500000'),(14,881010,4,7,22.90,'Arroz Prato Fino 5kg','Arroz agulhinha tipo 1, pacote 5kg.','https://d3gdr9n5lqb5z7.cloudfront.net/fotos/1262.jpg');
/*!40000 ALTER TABLE `produtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supermercados`
--

DROP TABLE IF EXISTS `supermercados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supermercados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) DEFAULT NULL,
  `image_url` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supermercados`
--

LOCK TABLES `supermercados` WRITE;
/*!40000 ALTER TABLE `supermercados` DISABLE KEYS */;
INSERT INTO `supermercados` VALUES (1,'Assai Atacadista','https://drive.google.com/uc?export=view&id=1DqTnafcaGXRWi2MD4q4m0-aDUU7O6xHe'),(2,'Atacadão','https://drive.google.com/uc?export=view&id=1AHtdMIAZ-pOvk8X8NB_j_xT2Z_i08Vj7'),(3,'Atacadista','https://drive.google.com/uc?export=view&id=1dCHuf6LAbbmAGJD3aLBsR3XPAyRYySsg'),(4,'Mix Mateus','https://drive.google.com/uc?export=view&id=1w8sFebJasFYqrt2usNn-2tTUVju56qhq');
/*!40000 ALTER TABLE `supermercados` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-22 16:32:09
