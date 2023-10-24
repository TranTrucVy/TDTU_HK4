USE [tempdb]
GO
DROP DATABASE IF EXISTS QLThuVien
GO
create database QLThuVien
GO
use QLThuVien
GO

-----
DROP TABLE IF EXISTS DOCGIA
GO
create table DOCGIA
(
	MaDocGia INT IDENTITY(1,1) PRIMARY KEY,
	TenDangNhap varchar(30),
	HoTen nvarchar(30),
	GioiTinh bit,
	NamSinh datetime,
	DiaChi nvarchar(100),
)
GO
DROP TABLE IF EXISTS SACH
GO
create table SACH
(
	MaSach INT IDENTITY(1,1) PRIMARY KEY,
	TenSach nvarchar(30),
	TacGia nvarchar(30),
	TheLoai nvarchar(30),
	NhaXuatBan nvarchar(30),
	GiaSach int,
	SoLuong int,
	TinhTrang nvarchar(30),
)
GO
DROP TABLE IF EXISTS PHIEUMUON
GO
create table PHIEUMUON
(
	MaPhieu INT IDENTITY(1,1) PRIMARY KEY,
	MaDocGia int,
	MaSach int,
	NgayMuon datetime,
	NgayPhaiTra datetime,
)
GO
DROP TABLE IF EXISTS PHIEUTRA
GO
create table PHIEUTRA
(
	MaPhieu INT IDENTITY(1,1) PRIMARY KEY,
	MaDocGia int,
	MaSach int,
	NgayTra datetime,
)
GO
DROP TABLE IF EXISTS ACCOUNT
GO
create table ACCOUNT
(
	MaDocGia INT IDENTITY(1,1) PRIMARY KEY,
	TenDangNhap varchar(30),
	MatKhau varchar(30),
	Quyen int,
)
GO

alter table PHIEUMUON add
	constraint FK_PHIEUMUON_DOCGIA foreign key (MaDocGia) references DOCGIA (MaDocGia),
	constraint FK_PHIEUMUON_SACH foreign key (MaSach) references SACH (MaSach)
GO
alter table PHIEUTRA add
	constraint FK_PHIEUTRA_DOCGIA foreign key (MaDocGia) references DOCGIA (MaDocGia),
	constraint FK_PHIEUTRA_SACH foreign key (MaSach) references SACH (MaSach)
GO
ALTER TABLE dbo.DOCGIA ADD
	CONSTRAINT FK_DOCGIA_ACCOUNT FOREIGN KEY (MaDocGia) REFERENCES dbo.ACCOUNT(MaDocGia)
GO

INSERT INTO ACCOUNT VALUES ('tranthiven', '123456', 0)
INSERT INTO ACCOUNT VALUES ('tranvana', '123456', 1)
INSERT INTO ACCOUNT VALUES ('nguyenthib', '123456', 1)
INSERT INTO ACCOUNT VALUES ('levanc', '123456', 1)
INSERT INTO ACCOUNT VALUES ('hothid', '123456', 1)

INSERT INTO DOCGIA VALUES ('tranthiven',N'TRẦN THỊ VẸN',0,2003,N'QUẬN 7')
INSERT INTO DOCGIA VALUES ('tranvana',N'TRẦN VĂN A',1,2000,N'QUẬN 1')
INSERT INTO DOCGIA VALUES ('nguyenthib',N'NGUYỄN THỊ B',0,2001,N'QUẬN 2')
INSERT INTO DOCGIA VALUES ('levanc',N'LÊ VĂN C',1,2002,N'QUẬN 3')
INSERT INTO DOCGIA VALUES ('hothid',N'HỒ THỊ D',0,2000,N'QUẬN 4')

----
INSERT INTO SACH VALUES ( N'LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG', N'KHÔNG BIẾT', N'LẬP TRÌNH', 'TDTU', 1500, 3, N'CÒN')
INSERT INTO SACH VALUES ( N'NHẬP MÔN LẬP TRÌNH', N'KHÔNG BIẾT', N'LẬP TRÌNH', 'TDTU', 1500, 10, N'CÒN')
INSERT INTO SACH VALUES ( N'KỸ THUẬT LẬP TRÌNH', N'KHÔNG BIẾT', N'LẬP TRÌNH', 'TDTU', 3000, 5, N'CÒN')
INSERT INTO SACH VALUES ( N'CÔNG NGHỆ PHẦN MỀM', N'KHÔNG BIẾT', N'LẬP TRÌNH', 'TDTU', 4000, 0, N'HẾT')
---
INSERT INTO PHIEUMUON VALUES (1,1,'1/1/2023', '1/2/2023')
INSERT INTO PHIEUMUON VALUES (2,1,'1/2/2023', '1/3/2023')
INSERT INTO PHIEUMUON VALUES (2,2,'1/3/2023', '1/4/2023')

---
INSERT INTO PHIEUTRA VALUES (1,2,'1/1/2023')
INSERT INTO PHIEUTRA VALUES (2,1,'1/2/2023')
INSERT INTO PHIEUTRA VALUES (2,2,'1/3/2023')

---
select DOCGIA.HoTen from ACCOUNT, DOCGIA where ACCOUNT.MaDocGia = DOCGIA.MaDocGia

select * from ACCOUNT
select * from DOCGIA
select * from SACH
select * from PHIEUMUON
select * from PHIEUTRA