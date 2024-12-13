-- phpMyAdmin SQL Dump
-- version 3.4.9
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tempo de Geração: 10/12/2024 às 17h46min
-- Versão do Servidor: 5.5.20
-- Versão do PHP: 5.3.9

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Banco de Dados: `metalurgica`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `mensagem`
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
-- Estrutura da tabela `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `codigo` INT NOT NULL AUTO_INCREMENT, -- ID do usuário
  `nome` VARCHAR(100) NOT NULL,
  `cpf` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(20) NOT NULL,
  `login` VARCHAR(50) NOT NULL,
  `senha` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`codigo`) -- Definir 'codigo' como chave primária
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Extraindo dados da tabela `usuario`
--

INSERT INTO `usuario` (`codigo`, `nome`, `cpf`, `email`, `telefone`, `login`, `senha`) VALUES
(4, 'erik de freitas', '145.670.799-06', 'erikdefreitas5@gmail.com', '(48) 99122-5312', 'erik', '123'),
(5, 'gilson de freitas', '645.638.639-04', 'gilferacos@hotmail.com', '(48) 99984-5183', 'dido', 'dido'),
(6, 'pedro venicio', '123.456.789-10', 'pvviadao@gmail.com', '(48) 58899-4521', 'pv', '123'),
(7, 'eduardo samuel', '123.456.789-11', 'duducorinthians@gmail.com', '(48) 58899-4785', 'dudu', '123');

-- --------------------------------------------------------
--
-- Estrutura da tabela `produto`
CREATE TABLE IF NOT EXISTS `produto` (
  `codigo` INT NOT NULL AUTO_INCREMENT, -- ID do produto
  `usuario_id` INT NOT NULL, -- Referencia o ID do usuário
  `tipo` VARCHAR(50) NOT NULL,
  `peso` FLOAT(10, 2) NOT NULL,
  `espessura` FLOAT(10, 2) NOT NULL,
  `preco` DECIMAL(10, 2) NULL,
  `status` VARCHAR(20) DEFAULT 'Pendente',
  `data_criacao` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`codigo`),
  FOREIGN KEY (`usuario_id`) REFERENCES `usuario`(`codigo`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



--
-- Estrutura da tabela `vendedor`
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
