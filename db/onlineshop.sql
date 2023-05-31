-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2022 at 08:21 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `onlineshop`
--

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

CREATE TABLE `brand` (
  `bid` int(11) NOT NULL,
  `brand` varchar(100) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'Active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `brand`
--

INSERT INTO `brand` (`bid`, `brand`, `status`) VALUES
(1, 'HM', 'Active'),
(3, 'LP', 'Active'),
(4, 'RT', 'Active'),
(5, 'DFGH', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `card`
--

CREATE TABLE `card` (
  `cardid` int(11) NOT NULL,
  `cid` int(11) DEFAULT NULL,
  `cardnum` varchar(20) DEFAULT NULL,
  `cardname` varchar(20) DEFAULT NULL,
  `expmonth` varchar(20) DEFAULT NULL,
  `expyear` varchar(20) DEFAULT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `card`
--

INSERT INTO `card` (`cardid`, `cid`, `cardnum`, `cardname`, `expmonth`, `expyear`, `status`) VALUES
(1, 1, '1111 1111 1111 1111', 'AK', '09', '21', 'Inactive'),
(2, 1, '7777 7777 7777 7777', 'DJ', '02', '21', 'Active'),
(3, 1, '8888 8888 8888 8888', 'AK', '02', '21', 'Active'),
(4, 1, '5555 5555 5555 5555', 'GHJK', '02', '21', 'Active'),
(5, 1, '9876543212345678', 'ABC', '02', '25', 'Active'),
(6, 1, '4444444444444444', 'Ak', '02', '25', 'Active'),
(7, 3, '9999999999999999', 'SA', '01', '28', 'Active'),
(8, 4, '9999999999999999', 'sa', '01', '28', 'Active'),
(9, 5, '9999999999999999', 'JB', '03', '28', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cartid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `total_amount` bigint(20) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`cartid`, `cid`, `total_amount`, `status`) VALUES
(13, 1, 31578, 'Purchased'),
(14, 1, 1800, 'Purchased'),
(15, 1, 154, 'Purchased'),
(16, 1, 75, 'Purchased'),
(17, 1, 6300, 'Purchased'),
(18, 1, 3600, 'Purchased'),
(19, 1, 0, 'Purchased'),
(20, 1, 2800, 'Purchased'),
(21, 1, 546, 'Purchased'),
(22, 1, 9250, 'Purchased'),
(23, 1, 0, 'Purchased'),
(24, 1, 3700, 'Purchased'),
(25, 1, 0, 'Purchased'),
(26, 1, 0, 'Purchased'),
(27, 1, 2340, 'Purchased'),
(28, 1, 720, 'Purchased'),
(29, 1, 770, 'Purchased'),
(30, 1, 0, 'Purchased'),
(31, 1, 100, 'Purchased'),
(32, 1, 0, 'Purchased'),
(33, 1, 330, 'Purchased'),
(34, 3, 0, 'Purchased'),
(35, 4, 0, 'Purchased'),
(36, 5, 0, 'Purchased'),
(37, 1, 0, 'Purchased'),
(38, 1, 0, 'In cart');

-- --------------------------------------------------------

--
-- Table structure for table `cartchild`
--

CREATE TABLE `cartchild` (
  `cartchid` int(11) NOT NULL,
  `cartid` int(11) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `qty` bigint(20) DEFAULT NULL,
  `price` bigint(20) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cartchild`
--

INSERT INTO `cartchild` (`cartchid`, `cartid`, `pid`, `qty`, `price`, `status`) VALUES
(25, 13, 2, 9, 693, 'Purchased'),
(28, 13, 3, 7, 3885, 'Purchased'),
(31, 13, 4, 30, 27000, 'Purchased'),
(33, 14, 4, 2, 1800, 'Purchased'),
(35, 15, 2, 2, 154, 'Purchased'),
(41, 16, 7, 3, 75, 'Purchased'),
(42, 17, 4, 7, 6300, 'Purchased'),
(44, 18, 4, 4, 3600, 'Purchased'),
(45, 19, 2, 13, 650, 'Purchased'),
(46, 20, 4, 3, 2700, 'Purchased'),
(47, 20, 7, 4, 100, 'Purchased'),
(48, 21, 6, 6, 396, 'Purchased'),
(49, 21, 2, 3, 150, 'Purchased'),
(50, 22, 2, 5, 250, 'Purchased'),
(51, 22, 4, 10, 9000, 'Purchased'),
(52, 23, 4, 4, 3600, 'Purchased'),
(53, 24, 4, 4, 3600, 'Purchased'),
(55, 25, 4, 4, 3600, 'Purchased'),
(56, 26, 9, 3, 360, 'Purchased'),
(57, 27, 4, 9, 1980, 'Purchased'),
(58, 27, 2, 4, 800, 'Purchased'),
(59, 28, 11, 3, 360, 'Purchased'),
(60, 28, 9, 5, 600, 'Purchased'),
(61, 29, 4, 8, 880, 'Purchased'),
(62, 30, 3, 4, 480, 'Purchased'),
(64, 31, 2, 5, 100, 'Purchased'),
(65, 32, 9, 2, 240, 'Purchased'),
(67, 33, 2, 4, 80, 'Purchased'),
(68, 33, 14, 2, 250, 'Purchased'),
(69, 34, 15, 4, 840, 'Purchased'),
(70, 35, 16, 3, 360, 'Purchased'),
(71, 36, 15, 4, 840, 'Purchased'),
(72, 37, 15, 3, 630, 'Purchased'),
(73, 38, 2, 3, 360, 'In cart');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `catid` int(11) NOT NULL,
  `category` varchar(100) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'Active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`catid`, `category`, `status`) VALUES
(1, 'ST', 'Active'),
(2, 'Normal', 'Active'),
(7, 'KGB', 'Active'),
(8, 'HJK', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `cid` int(11) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `house` varchar(100) NOT NULL,
  `street` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`cid`, `fname`, `lname`, `house`, `street`, `district`, `pincode`, `contact`, `email`) VALUES
(1, 'Akhil', 'V', 'VI', 'VV', 'Thrissur', '680570', '9090909090', 'ak@mail.com'),
(3, 'Swapna', 'Abraham', 'SA House', 'Aluva', 'EKM', '678678', '7897897899', 'sa@mail.com'),
(4, 'Megha', 'Raj', 'MA House', 'Aluva', 'EKM', '678678', '8998789878', 'mr@mail.com'),
(5, 'Jisna', 'Benny', 'JB house', 'Aluva', 'EKM', '678678', '9879879879', 'jb@mail.com'),
(6, 'Aji', 'A', 'Aji House', 'Aluva', 'EKM', '678678', '8888888888', 'aji@mail.com');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `logid` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `usertype` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`logid`, `username`, `password`, `usertype`, `status`) VALUES
(1, 'admin@gmail.com', 'admin', 'admin', '1'),
(2, 'ak@mail.com', 'Ak@12345', 'customer', '1'),
(3, 'vis@mail.com', '12345', 'staff', '1'),
(5, 'puma@mail.com', 'Puma@123', 'vendor', '1'),
(6, 'sa@mail.com', 'Sa@12345', 'customer', '1'),
(7, 'so@mail.com', 'So@12345', 'staff', '1'),
(8, 'mr@mail.com', 'Mr@12345', 'customer', '1'),
(9, 'jb@mail.com', 'Jb@12345', 'customer', '1'),
(10, 'az@mail.com', 'Az@12345', 'staff', '1'),
(11, 'aji@mail.com', 'Aji@12345', 'customer', '1');

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `orderid` int(11) NOT NULL,
  `cartid` int(11) DEFAULT NULL,
  `orderdate` date DEFAULT NULL,
  `orderstatus` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`orderid`, `cartid`, `orderdate`, `orderstatus`) VALUES
(1, 13, '2022-03-04', 'Purchased'),
(2, 13, '2022-03-05', 'Purchased'),
(3, 14, '2022-03-06', 'Purchased'),
(4, 15, '2022-03-09', 'Purchased'),
(5, 16, '2022-03-15', 'Purchased'),
(6, 17, '2022-03-16', 'Purchased'),
(7, 18, '2022-03-16', 'Purchased'),
(8, 19, '2022-03-16', 'Purchased'),
(9, 20, '2022-03-21', 'Purchased'),
(10, 21, '2022-03-23', 'Purchased'),
(11, 10, '2022-04-02', 'Purchased'),
(12, 22, '2022-04-02', 'Cancled'),
(13, 23, '2022-04-02', 'Purchased'),
(14, 24, '2022-04-04', 'Cancelled'),
(15, 25, '2022-04-04', 'Delevered'),
(16, 26, '2022-04-07', 'Cancelled'),
(17, 27, '2022-04-07', 'Delevered'),
(18, 28, '2022-04-10', 'Delevered'),
(19, 29, '2022-04-12', 'Delevered'),
(20, 30, '2022-04-12', 'Delevered'),
(21, 31, '2022-04-21', 'Delevered'),
(22, 32, '2022-04-26', 'Cancelled'),
(23, 33, '2022-04-28', 'Delevered'),
(24, 34, '2022-05-10', 'Delevered'),
(25, 35, '2022-05-10', 'Delevered'),
(26, 36, '2022-05-11', 'Delevered'),
(27, 37, '2022-05-12', 'Delevered');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `payid` int(11) NOT NULL,
  `cardid` bigint(20) DEFAULT NULL,
  `orderid` int(11) DEFAULT NULL,
  `paydate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`payid`, `cardid`, `orderid`, `paydate`) VALUES
(1, 2, 2, '2022-03-05'),
(2, 3, 3, '2022-03-06'),
(3, 4, 4, '2022-03-09'),
(4, 3, 5, '2022-03-15'),
(5, 4, 6, '2022-03-16'),
(6, 2, 7, '2022-03-16'),
(7, 5, 8, '2022-03-16'),
(8, 4, 9, '2022-03-21'),
(9, 4, 10, '2022-03-23'),
(10, 2, 11, '2022-04-02'),
(11, 2, 12, '2022-04-02'),
(12, 2, 13, '2022-04-02'),
(13, 2, 14, '2022-04-04'),
(14, 2, 15, '2022-04-04'),
(15, 2, 16, '2022-04-07'),
(16, 2, 17, '2022-04-07'),
(17, 3, 18, '2022-04-10'),
(18, 1, 19, '2022-04-12'),
(19, 1, 20, '2022-04-12'),
(20, 3, 21, '2022-04-21'),
(21, 6, 22, '2022-04-26'),
(22, 5, 23, '2022-04-28'),
(23, 7, 24, '2022-05-10'),
(24, 8, 25, '2022-05-10'),
(25, 9, 26, '2022-05-11'),
(26, 2, 27, '2022-05-12');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `pid` int(11) NOT NULL,
  `subid` int(11) NOT NULL,
  `bid` int(11) NOT NULL,
  `product` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `rate` int(11) NOT NULL,
  `img` varchar(100) NOT NULL,
  `stock` bigint(20) DEFAULT 0,
  `status` varchar(20) DEFAULT 'Active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`pid`, `subid`, `bid`, `product`, `description`, `rate`, `img`, `stock`, `status`) VALUES
(2, 4, 3, 'LKJ', 'LKJ DESC', 120, '/media/AVENGERS%20TIMELINE_ZTM7m5B.jpg', 1387, 'Active'),
(3, 2, 1, 'NBKK', 'NBK DESC', 220, '/media/download.png', 2509, 'Active'),
(4, 2, 1, 'PPP', 'PP DESC', 110, '/media/5f4a7f73d78a2.png', 72, 'Active'),
(6, 4, 1, 'DJ', 'ddD jjJ', 66, '/media/5f4a803aa8560_uveZsDq.png', 0, 'Active'),
(7, 4, 1, 'LKJHGF', 'LKJHGFGHJKL:', 25, '/media/pngwing.com%20(63)_U7jdA9p.png', 396, 'Active'),
(8, 5, 4, 'GI', 'ASD', 0, '/media/is%20light%20blue.jpg', 0, 'Active'),
(9, 2, 1, 'JHBh', 'kjsachuba', 120, '/media/bull.jpg', 195, 'Active'),
(10, 3, 1, 'KKK', 'kjbhj', 0, '/media/pexels-pixabay-159806.jpg', 0, 'Active'),
(11, 2, 1, 'jhhjg', 'mn jbhj', 120, '/media/download.jpg', 997, 'Active'),
(12, 2, 1, 'ZX', 'Zzz Xxx', 0, '/media/pexels-josh-sorenson-976866.jpg', 0, 'Active'),
(13, 3, 3, 'LKL', 'incadh iasc', 0, '/media/hanna-morris-Eu_jjK6Z67Q-unsplash%20(1)%20(2).jpg', 0, 'Active'),
(14, 2, 1, 'ZXC', 'ZZ XX CC', 125, '/media/WhatsApp%20Image%202022-04-19%20at%2012.04.45%20PM.jpeg', 298, 'Active'),
(15, 7, 5, 'THM', 'hbjh', 210, '/media/pexels-gabriel-peter-719396.jpg', 89, 'Active'),
(16, 8, 1, 'PPPP', 'jxshub', 120, '/media/pexels-pixabay-416528.jpg', 17, 'Active'),
(17, 3, 1, 'JKL', 'cjahj cahjsbh', 0, '/media/pexels-gabriel-peter-719396.jpg', 0, 'Active'),
(18, 2, 3, 'fgh', 'jhvgh', 0, '/media/pexels-gabriel-peter-719396.jpg', 0, 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `purchase_child`
--

CREATE TABLE `purchase_child` (
  `pc_id` int(11) NOT NULL,
  `pm_id` int(11) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `qty` bigint(20) DEFAULT NULL,
  `rate` bigint(20) DEFAULT NULL,
  `cost_price` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `purchase_child`
--

INSERT INTO `purchase_child` (`pc_id`, `pm_id`, `pid`, `qty`, `rate`, `cost_price`) VALUES
(12, 6, 3, 23, 57500, 2500),
(13, 6, 2, 12, 40800, 3400),
(14, 8, 4, 5, 25000, 5000),
(15, 10, 4, 29, 130500, 4500),
(16, 31, 2, 78, 6006, 77),
(17, 32, 5, 8, 528, 66),
(18, 32, 5, 8, 528, 66),
(21, 34, 6, 6, 396, 66),
(22, 44, 3, 12, 660, 55),
(23, 44, 2, 40, 1360, 34),
(24, 49, 3, 200, 160000, 800),
(25, 53, 7, 400, 8000, 20),
(26, 53, 3, 46, 2668, 58),
(27, 66, 3, 24, 384, 16),
(28, 67, 9, 200, 20000, 100),
(29, 67, 4, 10, 2000, 200),
(30, 70, 3, 100, 10000, 100),
(31, 70, 2, 100, 19000, 190),
(32, 73, 11, 1000, 100000, 100),
(33, 74, 2, 1000, 12000, 12),
(34, 75, 4, 28, 2800, 100),
(35, 83, 3, 0, 0, 0),
(36, 83, 3, 2000, 400000, 200),
(37, 89, 14, 300, 36000, 120),
(38, 90, 15, 100, 20000, 200),
(39, 91, 16, 20, 2000, 100),
(40, 92, 2, 100, 10000, 100);

-- --------------------------------------------------------

--
-- Table structure for table `purchase_master`
--

CREATE TABLE `purchase_master` (
  `pm_id` int(11) NOT NULL,
  `sid` int(11) DEFAULT 0,
  `vid` int(11) DEFAULT NULL,
  `purchase_date` date DEFAULT NULL,
  `total_amount` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `purchase_master`
--

INSERT INTO `purchase_master` (`pm_id`, `sid`, `vid`, `purchase_date`, `total_amount`) VALUES
(6, 0, 1, '2022-02-24', 98300),
(8, 1, 1, '2022-02-24', 25000),
(10, 0, 1, '2022-02-24', 130500),
(34, 0, 1, '2022-03-02', 396),
(35, 0, 1, '2022-03-05', 0),
(36, 0, 1, '2022-03-06', 0),
(37, 0, 0, '2022-03-06', 0),
(38, 0, 0, '2022-03-06', 0),
(39, 0, 1, '2022-03-07', 0),
(40, 0, 0, '2022-03-07', 0),
(41, 0, 0, '2022-03-08', 0),
(42, 0, 0, '2022-03-08', 0),
(43, 0, 0, '2022-03-08', 0),
(44, 0, 1, '2022-03-09', 2020),
(45, 0, 1, '2022-03-09', 0),
(46, 0, 1, '2022-03-11', 0),
(47, 0, 1, '2022-03-11', 0),
(48, 0, 1, '2022-03-14', 0),
(49, 1, 1, '2022-03-14', 160000),
(50, 0, 1, '2022-03-15', 0),
(51, 0, 1, '2022-03-15', 0),
(52, 0, 0, '2022-03-15', 0),
(53, 1, 1, '2022-03-15', 10668),
(54, 0, 0, '2022-03-15', 0),
(55, 0, 1, '2022-03-16', 0),
(56, 0, 1, '2022-03-16', 0),
(57, 0, 2, '2022-03-16', 0),
(58, 0, 2, '2022-03-16', 0),
(59, 0, 1, '2022-03-21', 0),
(60, 0, 2, '2022-03-22', 0),
(61, 0, 2, '2022-03-23', 0),
(62, 0, 1, '2022-03-28', 0),
(63, 0, 4, '2022-03-31', 0),
(64, 0, 0, '2022-03-31', 0),
(65, 0, 0, '2022-03-31', 0),
(66, 0, 5, '2022-04-04', 384),
(67, 0, 5, '2022-04-07', 22000),
(68, 0, 2, '2022-04-07', 0),
(69, 0, 0, '2022-04-07', 0),
(70, 0, 1, '2022-04-07', 29000),
(71, 0, 1, '2022-04-08', 0),
(72, 0, 1, '2022-04-09', 0),
(73, 0, 5, '2022-04-10', 100000),
(74, 0, 2, '2022-04-11', 12000),
(75, 1, 4, '2022-04-11', 2800),
(76, 0, 1, '2022-04-12', 0),
(77, 0, 1, '2022-04-12', 0),
(78, 0, 1, '2022-04-12', 0),
(79, 0, 1, '2022-04-12', 0),
(80, 0, 1, '2022-04-12', 0),
(81, 0, 5, '2022-04-20', 0),
(82, 0, 2, '2022-04-21', 0),
(83, 0, 5, '2022-04-26', 400000),
(84, 0, 1, '2022-04-26', 0),
(85, 0, 2, '2022-04-26', 0),
(86, 0, 1, '2022-04-26', 0),
(87, 0, 1, '2022-04-27', 0),
(88, 0, 2, '2022-04-27', 0),
(89, 0, 5, '2022-04-28', 36000),
(90, 0, 4, '2022-05-10', 20000),
(91, 0, 5, '2022-05-10', 2000),
(92, 0, 4, '2022-05-11', 10000),
(93, 0, 1, '2022-05-16', 0);

-- --------------------------------------------------------

--
-- Table structure for table `regsession`
--

CREATE TABLE `regsession` (
  `rsid` int(11) NOT NULL,
  `uid` int(11) DEFAULT NULL,
  `utype` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `regsession`
--

INSERT INTO `regsession` (`rsid`, `uid`, `utype`, `date`) VALUES
(1, 1, 'customer', '2022-02-02'),
(2, 3, 'customer', '2022-03-17'),
(3, 4, 'customer', '2022-03-09'),
(4, 5, 'customer', '2022-03-25'),
(5, 1, 'staff', '2022-01-26'),
(6, 2, 'staff', '2022-01-27'),
(7, 3, 'staff', '2022-01-31'),
(8, 6, 'customer', '2022-05-14');

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `revid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `rdate` datetime NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `rating` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`revid`, `cid`, `pid`, `rdate`, `feedback`, `rating`) VALUES
(0, 1, 2, '2022-02-18 23:03:02', 'Nice', 5);

-- --------------------------------------------------------

--
-- Table structure for table `staffs`
--

CREATE TABLE `staffs` (
  `sid` int(11) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `house` varchar(100) NOT NULL,
  `street` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `status` varchar(100) DEFAULT 'Active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staffs`
--

INSERT INTO `staffs` (`sid`, `fname`, `lname`, `house`, `street`, `district`, `pincode`, `contact`, `email`, `status`) VALUES
(1, 'Vis', 'CC', 'Chen', 'Chendra', 'Thrissur', '678786', '9898989800', 'vis@mail.com', 'Active'),
(2, 'SA', 'One', 'SO ', 'Aluva', 'EKM', '678678', '6789678999', 'so@mail.com', 'Active'),
(3, 'Abc', 'Zxc', 'jjj', 'jjj', 'jjj', '678678', '8908989000', 'az@mail.com', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `subcategory`
--

CREATE TABLE `subcategory` (
  `subid` int(11) NOT NULL,
  `catid` int(11) DEFAULT NULL,
  `subcategory` varchar(100) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'Active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subcategory`
--

INSERT INTO `subcategory` (`subid`, `catid`, `subcategory`, `status`) VALUES
(2, 1, 'abc', 'Active'),
(3, 1, 'efg', 'Active'),
(4, 2, 'KEF', 'Active'),
(5, 2, 'QWE', 'Active'),
(6, 1, 'KEF', 'Active'),
(7, 7, 'GHJ', 'Active'),
(8, 8, 'HJ', 'Active'),
(9, 8, 'jhg', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `vendor`
--

CREATE TABLE `vendor` (
  `vid` int(11) NOT NULL,
  `sName` varchar(100) NOT NULL,
  `fName` varchar(100) NOT NULL,
  `lName` varchar(100) NOT NULL,
  `street` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `status` varchar(20) DEFAULT 'Active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendor`
--

INSERT INTO `vendor` (`vid`, `sName`, `fName`, `lName`, `street`, `district`, `pincode`, `contact`, `email`, `status`) VALUES
(1, 'Diloooooooooooooooo', 'Dil', 'D', 'Kaii', 'Thrissur', '678876', '8989898989', 'dil@mail.com', 'Active'),
(2, 'VOO...', 'Vennn', 'Onennnn', 'Alu', 'EKM', '678876', '9879870000', 'vo@mail.com', 'Active'),
(4, 'JK S', 'J', 'K', 'SS', 'TSR', '890098', '6767676767', 'jk@mail.com', 'Active'),
(5, 'JW S', 'J', 'W', 'SS', 'TSR', '678678', '7878787878', 'jw@mail.com', 'Active'),
(6, 'Puma', 'Ok', 'AY', 'kk', 'Eranakulam', '678678', '9999999999', 'puma@mail.com', 'Active');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`bid`);

--
-- Indexes for table `card`
--
ALTER TABLE `card`
  ADD PRIMARY KEY (`cardid`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cartid`),
  ADD KEY `rid` (`cid`),
  ADD KEY `pid` (`total_amount`);

--
-- Indexes for table `cartchild`
--
ALTER TABLE `cartchild`
  ADD PRIMARY KEY (`cartchid`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`catid`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`logid`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`orderid`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`payid`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`pid`),
  ADD KEY `subid` (`subid`,`bid`);

--
-- Indexes for table `purchase_child`
--
ALTER TABLE `purchase_child`
  ADD PRIMARY KEY (`pc_id`);

--
-- Indexes for table `purchase_master`
--
ALTER TABLE `purchase_master`
  ADD PRIMARY KEY (`pm_id`);

--
-- Indexes for table `regsession`
--
ALTER TABLE `regsession`
  ADD PRIMARY KEY (`rsid`);

--
-- Indexes for table `staffs`
--
ALTER TABLE `staffs`
  ADD PRIMARY KEY (`sid`);

--
-- Indexes for table `subcategory`
--
ALTER TABLE `subcategory`
  ADD PRIMARY KEY (`subid`);

--
-- Indexes for table `vendor`
--
ALTER TABLE `vendor`
  ADD PRIMARY KEY (`vid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `brand`
--
ALTER TABLE `brand`
  MODIFY `bid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `card`
--
ALTER TABLE `card`
  MODIFY `cardid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `cartid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `cartchild`
--
ALTER TABLE `cartchild`
  MODIFY `cartchid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `catid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `logid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `orderid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `payid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `purchase_child`
--
ALTER TABLE `purchase_child`
  MODIFY `pc_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `purchase_master`
--
ALTER TABLE `purchase_master`
  MODIFY `pm_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT for table `regsession`
--
ALTER TABLE `regsession`
  MODIFY `rsid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `staffs`
--
ALTER TABLE `staffs`
  MODIFY `sid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `subcategory`
--
ALTER TABLE `subcategory`
  MODIFY `subid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `vendor`
--
ALTER TABLE `vendor`
  MODIFY `vid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
