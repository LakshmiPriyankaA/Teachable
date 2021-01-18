CREATE DATABASE neighborhood;
GO
USE neighborhood
create table neighboring_node(
			 nn_id INT PRIMARY KEY IDENTITY (1, 1),
			 size INT NOT NULL,
			 x_crdnt INT,
			 y_crdnt INT,
			 i INT,
			 m INT NOT NULL,
			 topology Varchar(20) NOT NULL)
GO
INSERT INTO neighboring_node(size, x_crdnt, y_crdnt, i, m, topology)
VALUES('3','2','2',NULL,'1','SQUARE'),('6','3','3',NULL,'2','CROSS'),('9',NULL,NULL,'29','3','DIAMOND')
GO

