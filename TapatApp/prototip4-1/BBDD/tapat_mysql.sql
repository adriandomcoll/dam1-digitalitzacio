-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 18-12-2024 a las 19:42:43
-- Versión del servidor: 8.0.40-0ubuntu0.22.04.1
-- Versión de PHP: 8.1.2-1ubuntu2.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `Child` (
  `id` int NOT NULL AUTO_INCREMENT,
  `child_name` varchar(50) NOT NULL,
  `sleep_average` int NOT NULL,
  `treatment_id` int NOT NULL,
  `time` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `treatment_id` (`treatment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Child` (`id`, `child_name`, `sleep_average`, `treatment_id`, `time`) VALUES
(1, 'Carol Child', 8, 1, 6),
(2, 'Jaco Child', 10, 2, 6);

CREATE TABLE `RelationUserChild` (
  `user_id` int NOT NULL,
  `child_id` int NOT NULL,
  `rol_id` int NOT NULL,
  PRIMARY KEY (`user_id`,`child_id`,`rol_id`),
  KEY `user_id` (`user_id`),
  KEY `child_id` (`child_id`),
  KEY `rol_id` (`rol_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `RelationUserChild` (`user_id`, `child_id`, `rol_id`) VALUES
(1, 1, 1),
(1, 1, 2),
(2, 2, 1),
(2, 2, 2);

CREATE TABLE `Rol` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type_rol` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Rol` (`id`, `type_rol`) VALUES
(1, 'Admin'),
(2, 'Tutor Mare Pare'),
(3, 'Cuidador'),
(4, 'Seguiment');

CREATE TABLE `Status` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Status` (`id`, `name`) VALUES
(1, 'sleep'),
(2, 'awake'),
(3, 'yes_eyepatch'),
(4, 'no_eyepatch');

CREATE TABLE `Tap` (
  `id` int NOT NULL AUTO_INCREMENT,
  `child_id` int NOT NULL,
  `status_id` int NOT NULL,
  `user_id` int NOT NULL,
  `init` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `status_id` (`status_id`),
  KEY `child_id` (`child_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Treatment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Treatment` (`id`, `name`) VALUES
(1, 'Hour'),
(2, 'percentage');

CREATE TABLE `User` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `token` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `User` (`id`, `username`, `password`, `email`) VALUES
(1, 'mare', 'mare', 'prova@gmail.com'),
(2, 'pare', 'pare', 'prova2@gmail.com');

ALTER TABLE `Child`
  ADD CONSTRAINT `Child_ibfk_1` FOREIGN KEY (`treatment_id`) REFERENCES `Treatment` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `RelationUserChild`
  ADD CONSTRAINT `RelationUserChild_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `RelationUserChild_ibfk_2` FOREIGN KEY (`child_id`) REFERENCES `Child` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `RelationUserChild_ibfk_3` FOREIGN KEY (`rol_id`) REFERENCES `Rol` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Tap`
  ADD CONSTRAINT `Tap_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `Status` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Tap_ibfk_2` FOREIGN KEY (`child_id`) REFERENCES `Child` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Tap_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

COMMIT;