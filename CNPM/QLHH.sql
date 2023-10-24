USE master
GO
CREATE DATABASE QLHH
GO
USE QLHH
GO

CREATE TABLE HangHoa (
	MaHH INT IDENTITY(1,1) PRIMARY KEY, 
	TenHH NVARCHAR(50) NOT NULL,
	SoLuong INT NOT NULL,
	DonGia MONEY NOT NULL
);
GO

-- Tạo bảng Hoá đơn
CREATE TABLE HoaDon (
	MaHD INT IDENTITY(1,1) PRIMARY KEY,
	NgayLap DATE NOT NULL,
	TongTien MONEY NOT NULL
);
GO
-- Tạo bảng Chi tiết hoá đơn
CREATE TABLE ChiTietHoaDon (
	MaHD INT NOT NULL,
	MaHH INT NOT NULL,
	SoLuong INT NOT NULL,
	DonGia MONEY NOT NULL,
	PRIMARY KEY (MaHD, MaHH),
	FOREIGN KEY (MaHD) REFERENCES HoaDon(MaHD), 
	FOREIGN KEY (MaHH) REFERENCES HangHoa(MaHH) 
);
GO
INSERT INTO HangHoa (TenHH, SoLuong, DonGia)
VALUES ('Sách lập trình Python', 50, 250000),
		('Điện thoại Samsung Galaxy S21', 20, 20000000),
		('Laptop Dell XPS 13', 10, 35000000);
GO

-- Thêm dữ liệu vào bảng HoaDon
INSERT INTO HoaDon (NgayLap, TongTien)
VALUES ('2022-01-01', 12500000),
		('2022-01-02', 7500000);
GO
-- Thêm dữ liệu vào bảng ChiTietHoaDon
INSERT INTO ChiTietHoaDon (MaHD, MaHH, SoLuong, DonGia)
VALUES (1, 1, 5, 250000),
		(1, 2, 2, 20000000),
		(2, 1, 3, 250000),
		(2, 3, 1, 35000000);
GO