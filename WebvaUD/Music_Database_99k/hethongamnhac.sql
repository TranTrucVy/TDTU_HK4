-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 08, 2021 lúc 01:18 PM
-- Phiên bản máy phục vụ: 10.4.18-MariaDB
-- Phiên bản PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `hethongamnhac`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nhac`
--

CREATE TABLE `nhac` (
  `id` int(11) NOT NULL,
  `tenbaihat` varchar(100) COLLATE utf8_vietnamese_ci NOT NULL,
  `sangtac` varchar(100) COLLATE utf8_vietnamese_ci NOT NULL,
  `trinhbai` varchar(100) COLLATE utf8_vietnamese_ci NOT NULL,
  `nguoidang` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `thoigiandang` varchar(11) COLLATE utf8_vietnamese_ci NOT NULL,
  `hinhanh` text COLLATE utf8_vietnamese_ci NOT NULL,
  `luotxem` int(11) NOT NULL DEFAULT 0,
  `theloainhac` int(11) NOT NULL,
  `quocgia` int(11) NOT NULL,
  `linknhac` text COLLATE utf8_vietnamese_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `nhac`
--

INSERT INTO `nhac` (`id`, `tenbaihat`, `sangtac`, `trinhbai`, `nguoidang`, `thoigiandang`, `hinhanh`, `luotxem`, `theloainhac`, `quocgia`, `linknhac`) VALUES
(7, 'Khi Em Lớn', 'Hoàng Dung', 'Orega', 'nhung', '05/05/2021', 'https://photo-resize-zmp3.zadn.vn/w240_r1x1_jpeg/cover/c/4/3/a/c43a3f7cc98ee9c62401edb8fb999b74.jpg', 19, 1, 0, 'khiemlon.mp3'),
(8, 'Khi Người Lớn Cô Đơn', 'Phạm Hồng Phúc', 'Phạm Hồng Phúc', 'nhung', '05/04/2021', 'https://i1.sndcdn.com/artworks-000171730820-tc1pek-t500x500.jpg', 36, 1, 0, 'khinguoiloncodon.mp3'),
(9, 'Khi Tình Yêu Đủ Lớn', 'Hoàng Thùy Linh', 'RTeex', 'nhung', '05/05/2021', 'https://data.chiasenhac.com/data/cover/133/132503.jpg', 56, 2, 0, 'khitinhyeudulon.mp3'),
(10, 'Cô Đọc Vương', 'Hoàng Vương', 'Hoàng Vương', 'nhung', '05/05/2021', 'https://i.ytimg.com/vi/s2SFxLbpC5M/maxresdefault.jpg', 9, 4, 0, 'codocvuong.mp3'),
(11, 'Con Đường Tắt Nào', 'Toddy Quốc Trung', 'Toddy Quốc Trung', 'nhung', '7/5/2021', 'https://ledominhthao.com/wp-content/uploads/2020/12/12875447-casual-4am-walks-2.jpg', 19, 6, 0, 'conduongtatnao.mp3'),
(12, 'Đom Đóm', 'Jack', 'Jack', 'nhung', '08/05/2021', 'https://photo-resize-zmp3.zadn.vn/w600_r300x169_jpeg/thumb_video/8/0/1/c/801c0a9f296fd140a40f94ba3eae5e35.jpg', 1, 1, 0, 'domdom.mp3');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `quocgia`
--

CREATE TABLE `quocgia` (
  `id` int(11) NOT NULL,
  `tenquocgia` varchar(200) COLLATE utf8_vietnamese_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `quocgia`
--

INSERT INTO `quocgia` (`id`, `tenquocgia`) VALUES
(0, 'Việt Nam');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `taikhoan`
--

CREATE TABLE `taikhoan` (
  `taikhoan` varchar(20) COLLATE utf8_vietnamese_ci NOT NULL,
  `matkhau` varchar(50) COLLATE utf8_vietnamese_ci NOT NULL,
  `hoten` varchar(100) COLLATE utf8_vietnamese_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `taikhoan`
--

INSERT INTO `taikhoan` (`taikhoan`, `matkhau`, `hoten`) VALUES
('nhung', '123456', 'Nhung');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `theloainhac`
--

CREATE TABLE `theloainhac` (
  `id` int(11) NOT NULL,
  `tentheloai` varchar(200) COLLATE utf8_vietnamese_ci NOT NULL,
  `hinhanh` text COLLATE utf8_vietnamese_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_vietnamese_ci;

--
-- Đang đổ dữ liệu cho bảng `theloainhac`
--

INSERT INTO `theloainhac` (`id`, `tentheloai`, `hinhanh`) VALUES
(1, 'EDM', 'https://photo-resize-zmp3.zadn.vn/w320_r1x1_jpeg/cover/c/5/f/c/c5fc615c43215c6b72676f42767855ee.jpg'),
(2, 'Nhạc Âu', 'https://photo-resize-zmp3.zadn.vn/w320_r1x1_jpeg/cover/e/9/f/6/e9f6c74d1651a3dcf0be456822f1eefd.jpg'),
(3, 'Nhàn Hàn Quốc', 'https://photo-resize-zmp3.zadn.vn/w320_r1x1_jpeg/cover/2/d/d/0/2dd000bcd585f01edd235c0c3f21c2f9.jpg'),
(4, 'Trữ Tình', 'https://photo-resize-zmp3.zadn.vn/w320_r1x1_jpeg/cover/6/1/0/f/610f6b9b6d694034c23e4ef48e4ad7b8.jpg'),
(6, 'Rap', 'https://photo-resize-zmp3.zadn.vn/w320_r1x1_jpeg/cover/1/8/8/e/188e45098127c7f75cc4b715bf01bcd6.jpg');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `nhac`
--
ALTER TABLE `nhac`
  ADD PRIMARY KEY (`id`),
  ADD KEY `quocgia` (`quocgia`),
  ADD KEY `theloainhac` (`theloainhac`),
  ADD KEY `nguoidang` (`nguoidang`);

--
-- Chỉ mục cho bảng `quocgia`
--
ALTER TABLE `quocgia`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `taikhoan`
--
ALTER TABLE `taikhoan`
  ADD PRIMARY KEY (`taikhoan`);

--
-- Chỉ mục cho bảng `theloainhac`
--
ALTER TABLE `theloainhac`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `nhac`
--
ALTER TABLE `nhac`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT cho bảng `theloainhac`
--
ALTER TABLE `theloainhac`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `nhac`
--
ALTER TABLE `nhac`
  ADD CONSTRAINT `nhac_ibfk_1` FOREIGN KEY (`theloainhac`) REFERENCES `theloainhac` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `nhac_ibfk_2` FOREIGN KEY (`quocgia`) REFERENCES `quocgia` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `nhac_ibfk_3` FOREIGN KEY (`nguoidang`) REFERENCES `taikhoan` (`taikhoan`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
