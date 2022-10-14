-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Recetas_practica_examen
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Recetas_practica_examen
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Recetas_practica_examen` DEFAULT CHARACTER SET utf8 ;
USE `Recetas_practica_examen` ;

-- -----------------------------------------------------
-- Table `Recetas_practica_examen`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Recetas_practica_examen`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_time` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Recetas_practica_examen`.`recipes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Recetas_practica_examen`.`recipes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `description` TEXT NULL,
  `instructioms` TEXT NULL,
  `date_made` DATE NULL,
  `under_30` TINYINT(1) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recipes_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_recipes_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `Recetas_practica_examen`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
