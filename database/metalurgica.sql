-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Dec 17, 2024 at 03:08 AM
-- Server version: 5.5.16
-- PHP Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `metalurgica`
--

-- --------------------------------------------------------

--
-- Table structure for table `mensagem`
--

CREATE TABLE IF NOT EXISTS `mensagem` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `mensagem` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `produto`
--

CREATE TABLE IF NOT EXISTS `produto` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `peso` float(10,2) NOT NULL,
  `espessura` float(10,2) NOT NULL,
  `preco` decimal(10,2) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'Pendente',
  `data_criacao` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`codigo`),
  KEY `usuario_id` (`usuario_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `produto`
--

INSERT INTO `produto` (`codigo`, `usuario_id`, `tipo`, `peso`, `espessura`, `preco`, `status`, `data_criacao`) VALUES
(3, 4, 'ferro', 50.00, 5.00, '500.00', 'aprovado', '2024-12-14 00:28:28'),
(4, 4, 'aço inoxidável', 90.00, 3.00, '69.00', 'negado', '2024-12-14 00:34:12'),
(5, 4, 'alumínio', 85.00, 12.00, '600.00', 'aprovado', '2024-12-14 01:16:41'),
(6, 4, 'ferro', 64.00, 8.00, '30.00', 'negado', '2024-12-14 18:54:02'),
(7, 5, 'cobre', 90.00, 3.00, '630.00', 'aprovado', '2024-12-16 21:43:40'),
(8, 8, 'alumínio', 47.00, 2.00, '750.00', 'negado', '2024-12-16 21:47:19'),
(9, 4, 'aço inoxidável', 45.00, 3.00, '320.00', 'aprovado', '2024-12-17 01:49:54');

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `codigo` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `login` varchar(50) NOT NULL,
  `senha` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`codigo`, `nome`, `cpf`, `email`, `telefone`, `login`, `senha`) VALUES
(4, 'erik de freitas', '145.670.799-06', 'erikdefreitas5@gmail.com', '(48) 99122-5312', 'erik', '123'),
(5, 'gilson de freitas', '645.638.639-04', 'gilferacos@hotmail.com', '(48) 99984-5183', 'dido', 'dido'),
(6, 'pedro venicio', '123.456.789-10', 'pvviadao@gmail.com', '(48) 58899-4521', 'pv', '123'),
(7, 'eduardo samuel', '123.456.789-11', 'duducorinthians@gmail.com', '(48) 58899-4785', 'dudu', '123'),
(8, 'joao pedro', '123.456.789-10', 'joao@gmail.com', '(48) 99122-5312', 'joao', '123');

-- --------------------------------------------------------

--
-- Table structure for table `vendedor`
--

CREATE TABLE IF NOT EXISTS `vendedor` (
  `codigo` int(5) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `cpf` varchar(50) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `login` varchar(50) NOT NULL,
  `senha` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `vendedor`
--

INSERT INTO `vendedor` (`codigo`, `nome`, `email`, `cpf`, `telefone`, `login`, `senha`) VALUES
(1, 'adm', 'admin@gmail.com', '123.456.789-10', '(48) 99122-5312', 'adm', 'adm');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `produto`
--
ALTER TABLE `produto`
  ADD CONSTRAINT `produto_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`codigo`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
