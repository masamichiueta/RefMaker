SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `refmaker` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ;
USE `refmaker` ;

-- -----------------------------------------------------
-- Table `refmaker`.`bibtype`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `refmaker`.`bibtype` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `refmaker`.`user`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `refmaker`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `email` VARCHAR(255) NOT NULL ,
  `password` VARCHAR(255) NOT NULL ,
  `active` TINYINT(1) NULL ,
  `confirmed_at` DATETIME NULL ,
  `name` VARCHAR(45) NULL DEFAULT 'username' ,
  `icon_path` VARCHAR(45) NULL DEFAULT 'img/default.png' ,
  `last_login_at` DATETIME NULL ,
  `current_login_at` DATETIME NULL ,
  `last_login_ip` VARCHAR(100) NULL ,
  `current_login_ip` VARCHAR(100) NULL ,
  `login_count` INT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `refmaker`.`bibtex`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `refmaker`.`bibtex` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `created_by` INT NOT NULL ,
  `bibtype_id` INT NOT NULL ,
  `address` VARCHAR(255) NULL ,
  `annote` VARCHAR(255) NULL ,
  `author` VARCHAR(255) NULL ,
  `booktitle` VARCHAR(255) NULL ,
  `chapter` VARCHAR(10) NULL ,
  `crossref` VARCHAR(45) NULL ,
  `edition` VARCHAR(45) NULL ,
  `editor` VARCHAR(255) NULL ,
  `howpublished` VARCHAR(45) NULL ,
  `institution` VARCHAR(45) NULL ,
  `journal` VARCHAR(45) NULL ,
  `key` VARCHAR(45) NULL ,
  `month` VARCHAR(10) NULL ,
  `note` VARCHAR(255) NULL ,
  `number` VARCHAR(10) NULL ,
  `organization` VARCHAR(45) NULL ,
  `pages` VARCHAR(45) NULL ,
  `publisher` VARCHAR(45) NULL ,
  `school` VARCHAR(45) NULL ,
  `series` VARCHAR(45) NULL ,
  `title` VARCHAR(255) NULL ,
  `type` VARCHAR(45) NULL ,
  `volume` VARCHAR(10) NULL ,
  `year` VARCHAR(10) NULL ,
  `yomi` VARCHAR(45) NULL ,
  `file_path` VARCHAR(45) NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_bibtex_type` (`bibtype_id` ASC) ,
  INDEX `fk_bib_tex_user` (`created_by` ASC) ,
  CONSTRAINT `fk_bibtex_type`
    FOREIGN KEY (`bibtype_id` )
    REFERENCES `refmaker`.`bibtype` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_bib_tex_user`
    FOREIGN KEY (`created_by` )
    REFERENCES `refmaker`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `refmaker`.`must_item`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `refmaker`.`must_item` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `type_id` INT NOT NULL ,
  `item_name` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `uq_type_id_item_name` (`type_id` ASC, `item_name` ASC) ,
  INDEX `fk_must_item_type` (`type_id` ASC) ,
  CONSTRAINT `fk_must_item_type`
    FOREIGN KEY (`type_id` )
    REFERENCES `refmaker`.`bibtype` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `refmaker`.`role`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `refmaker`.`role` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(80) NOT NULL ,
  `description` VARCHAR(255) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `refmaker`.`roles_users`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `refmaker`.`roles_users` (
  `user_id` INT NOT NULL ,
  `role_id` INT NOT NULL ,
  INDEX `fk_roles_users_user` (`user_id` ASC) ,
  INDEX `fk_roles_users_role` (`role_id` ASC) ,
  CONSTRAINT `fk_roles_users_user`
    FOREIGN KEY (`user_id` )
    REFERENCES `refmaker`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_roles_users_role`
    FOREIGN KEY (`role_id` )
    REFERENCES `refmaker`.`role` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `refmaker`.`follow`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `refmaker`.`follow` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `who` INT NOT NULL ,
  `whom` INT NOT NULL ,
  UNIQUE INDEX `uq_who_whom` (`who` ASC, `whom` ASC) ,
  INDEX `fk_follow_who_user` (`who` ASC) ,
  INDEX `fk_follow_whom_user` (`whom` ASC) ,
  PRIMARY KEY (`id`) ,
  CONSTRAINT `fk_follow_who_user`
    FOREIGN KEY (`who` )
    REFERENCES `refmaker`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_follow_whom_user`
    FOREIGN KEY (`whom` )
    REFERENCES `refmaker`.`user` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
