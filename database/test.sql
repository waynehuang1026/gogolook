CREATE DATABASE test;

use test;

CREATE TABLE `task` (
    `id` int NOT NULL AUTO_INCREMENT,
    `name` text NOT NULL,
    `status` smallint DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB AUTO_INCREMENT = 70 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;