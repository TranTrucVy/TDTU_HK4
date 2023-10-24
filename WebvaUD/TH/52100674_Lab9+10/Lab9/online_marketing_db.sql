-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Phiên bản PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `online_marketing_db`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `bill`
--

CREATE TABLE `bill` (
  `stt` varchar(10) NOT NULL,
  `pro_name` varchar(100) NOT NULL,
  `quantity` varchar(50) NOT NULL,
  `price` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `cart`
--

CREATE TABLE `cart` (
  `stt` varchar(10) NOT NULL,
  `image` varchar(200) NOT NULL,
  `pro_name` varchar(100) NOT NULL,
  `price` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `note` varchar(30) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `category`
--

INSERT INTO `category` (`id`, `name`, `note`) VALUES
(1, 'Apple', ''),
(2, 'Samsung', ''),
(3, 'Oppo', ''),
(4, 'Google', ''),
(5, 'Nokia', '');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `customer`
--

CREATE TABLE `customer` (
  `cust_id` varchar(10) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `customer`
--

INSERT INTO `customer` (`cust_id`, `username`, `password`, `email`) VALUES
('KH0001', 'a', '123456', 'a@gmail.com');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `price` int(11) NOT NULL,
  `description` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `vote` int(11) NOT NULL,
  `image` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `product`
--

INSERT INTO `product` (`id`, `name`, `price`, `description`, `vote`, `image`, `type`) VALUES
(1, 'iPhone 7', 10990000, 'This is iPhone 7', 4, 'images/iphone-7-plus-128gb-de-400x460.png', 1),
(2, 'Samsung Galaxy J3', 8490000, 'This is Samsung Galaxy J3', 3, 'images/samsung-galaxy-j3-2017-2-400x460-1.png', 2),
(3, 'Samsung Galaxy J5', 5490000, 'This is Samsung Galaxy J5', 4, 'images/samsung-galaxy-j3-2017-2-400x460.png', 2),
(4, 'Samsung Galaxy J7', 3490000, 'This is Samsung Galaxy J7', 2, 'images/samsung-galaxy-j7-plus-1-400x460.png', 2),
(5, 'Samsung Galaxy Note 5', 6990000, 'This is Samsung Galaxy Note 5', 2, 'images/samsung-galaxy-note-5-2-400x460.png', 2),
(6, 'iPhone 6S', 8500000, 'This is iPhone 6S', 5, 'images/iphone-6s-128gb-hong-1-400x450.png', 1),
(7, 'Oppo F3 Plus', 2500000, 'This is Oppo F3 Plus', 5, 'images/oppo-f3-plus-1-1-400x460.png', 3),
(8, 'Oppo A7', 12500000, 'This is Oppo A7', 3, 'images/oppo-a71-400x460.png', 3),
(9, 'Google Redmi 4X', 10500000, 'This is Google Redmi 4X', 3, 'images/xiaomi-redmi-4x-400-400x460.png', 4),
(10, 'Google Mi A1', 7500000, 'This is Google Mi A1', 3, 'images/xiaomi-mi-a12-400x460.png', 4),
(11, 'Nokia 8', 6300000, 'This is Nokia 8', 3, 'images/nokia-8-1-400x460.png', 5),
(12, 'Nokia 3', 4300000, 'This is Nokia 3', 3, 'images/nokia-3-2-400x460.png', 5);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`stt`);

--
-- Chỉ mục cho bảng `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`stt`);

--
-- Chỉ mục cho bảng `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cust_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Chỉ mục cho bảng `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
