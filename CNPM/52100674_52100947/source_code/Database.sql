USE [master]
GO
/****** Object:  Database [QLDB]    Script Date: 4/24/2023 1:08:23 AM ******/
CREATE DATABASE [QLDB]
GO
USE [QLDB]
GO
/****** Object:  Table [dbo].[CauLacBo]    Script Date: 4/24/2023 1:08:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CauLacBo](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[TenCLB] [nvarchar](max) NULL,
	[IdSVD] [int] NULL,
	[HuanLuyenVien] [nvarchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CauThu]    Script Date: 4/24/2023 1:08:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CauThu](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[HoTen] [nvarchar](max) NULL,
	[QueQuan] [nvarchar](max) NULL,
	[NamSinh] [int] NULL,
	[SoAo] [int] NULL,
	[IdCLB] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[KetQua]    Script Date: 4/24/2023 1:08:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KetQua](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[IdLTD] [int] NULL,
	[BanThangDoi1] [int] NULL,
	[BanThangDoi2] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[LichThiDau]    Script Date: 4/24/2023 1:08:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[LichThiDau](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[IdCLB1] [int] NULL,
	[IdCLB2] [int] NULL,
	[NgayThiDau] [datetime] NULL,
	[IdSVD] [int] NULL,
	[IdMuaGiai] [int] NULL,
	[GioThiDau] [time] null,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[MuaGiai]    Script Date: 4/24/2023 1:08:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MuaGiai](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[TenMuaGiai] [nvarchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PhanQuyen]    Script Date: 4/24/2023 1:08:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PhanQuyen](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[TenPQ] [nvarchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SanVD]    Script Date: 4/24/2023 1:08:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SanVD](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[TenSVD] [nvarchar](max) NULL,
	[SucChua] [varchar](max) NULL,
	[ThanhPho] [nvarchar](max) NULL,
 CONSTRAINT [PK__SanVD__3214EC07E976AA16] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TaiKhoan]    Script Date: 4/24/2023 1:08:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TaiKhoan](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[TenDangNhap] [varchar](max) NULL,
	[MatKhau] [varchar](max) NULL,
	[IdPQ] [int] NULL,
	[Email] [nvarchar](250) NULL,
	[SDT] [varchar](10) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[XepHang]    Script Date: 4/24/2023 1:08:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[XepHang](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[IdMuaGiai] [int] NULL,
	[IdCLB] [int] NULL,
	[Diem] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[CauLacBo] ON 

INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (1, N'Manchester United', 1, N'Pep Guardiola')
INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (2, N'Norwich City', 3, N'Zinedine Zidane')
INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (3, N'Hải Phòng', 11, N'Park Hang Seo')
INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (4, N'Real Madrid', 3, N'Carlo Ancelotti')
INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (5, N'Barcelona', 2, N'Ronald Koeman')
INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (6, N'Paris Saint-Germain', 10, N'Mauricio Pochettino')
INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (7, N'AC Milan', 5, N'Stefano Pioli')
INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (8, N'Arsenal ', 9, N'Jonas Eidevall')
INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (9, N'Sài Gòn FC', 12, N'Phạm Công Lộc')
INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (10, N'Sông Lam Nghệ An FC', 11, N'Nguyễn Đức Thắng')
INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (11, N'Hà Nội FC', 11, N'Chu Đình Nghiêm')
INSERT [dbo].[CauLacBo] ([Id], [TenCLB], [IdSVD], [HuanLuyenVien]) VALUES (12, N'Becamex Bình Dương FC', 13, N'Nguyễn Thanh Sơn')
SET IDENTITY_INSERT [dbo].[CauLacBo] OFF
GO
SET IDENTITY_INSERT [dbo].[CauThu] ON 

INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (1, N'Lương Xuân Trường', N'Hưng Yên', 1995, 6, 12)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (2, N'Phan Văn Đức', N'Nghệ An', 1995, 9, 10)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (3, N'Đặng Văn Tới', N'Nghệ An', 1993, 5, 10)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (4, N'Nguyễn Văn Đại ', N'Nghệ An', 1997, 15, 10)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (5, N'Hồ Tấn Tài ', N'Nghệ An', 1998, 14, 9)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (6, N'Nguyễn Văn Quyết', N'Hà Nội', 1991, 10, 11)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (7, N'Đỗ Hùng Dũng', N'Hải Dương', 1993, 8, 11)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (8, N'Đỗ Duy Mạnh', N'Thái Bình', 1991, 2, 11)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (9, N'Nguyễn Tiến Linh', N'Hải Dương', 1997, 9, 12)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (10, N'Đỗ Văn Thuận', N'Đắk Lắk', 1993, 16, 9)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (11, N'Luke Shaw', N'Kingston upon Thames', 1995, 23, 1)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (12, N'Paul Pogba ', N'Lagny-sur-Marne', 1993, 6, 1)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (13, N'Bukayo Saka', N' London, Anh', 2001, 7, 8)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (14, N'Granit Xhaka', N'Basel, Thụy Sĩ', 1992, 34, 1)
INSERT [dbo].[CauThu] ([Id], [HoTen], [QueQuan], [NamSinh], [SoAo], [IdCLB]) VALUES (15, N'Karim Benzema', N'Lyon, Pháp', 1987, 9, 1)
SET IDENTITY_INSERT [dbo].[CauThu] OFF
GO
SET IDENTITY_INSERT [dbo].[LichThiDau] ON 

INSERT [dbo].[LichThiDau] ([Id], [IdCLB1], [IdCLB2], [NgayThiDau], [IdSVD], [IdMuaGiai]) VALUES (1, 1, 2, CAST(N'2023-08-28T00:00:00.000' AS DateTime), 1, 1)
INSERT [dbo].[LichThiDau] ([Id], [IdCLB1], [IdCLB2], [NgayThiDau], [IdSVD], [IdMuaGiai]) VALUES (2, 2, 1, CAST(N'2023-08-27T00:00:00.000' AS DateTime), 1, 1)
INSERT [dbo].[LichThiDau] ([Id], [IdCLB1], [IdCLB2], [NgayThiDau], [IdSVD], [IdMuaGiai]) VALUES (3, 1, 2, CAST(N'2023-08-26T00:00:00.000' AS DateTime), 1, 1)
INSERT [dbo].[LichThiDau] ([Id], [IdCLB1], [IdCLB2], [NgayThiDau], [IdSVD], [IdMuaGiai]) VALUES (4, 2, 1, CAST(N'2023-08-30T00:00:00.000' AS DateTime), 1, 1)
INSERT [dbo].[LichThiDau] ([Id], [IdCLB1], [IdCLB2], [NgayThiDau], [IdSVD], [IdMuaGiai]) VALUES (5, 4, 1, CAST(N'2023-08-29T00:00:00.000' AS DateTime), 1, 1)
SET IDENTITY_INSERT [dbo].[LichThiDau] OFF
GO
SET IDENTITY_INSERT [dbo].[MuaGiai] ON 

INSERT [dbo].[MuaGiai] ([Id], [TenMuaGiai]) VALUES (1, N'UEFA Champions League')
INSERT [dbo].[MuaGiai] ([Id], [TenMuaGiai]) VALUES (2, N'Premier League')
INSERT [dbo].[MuaGiai] ([Id], [TenMuaGiai]) VALUES (3, N'La Liga ')
INSERT [dbo].[MuaGiai] ([Id], [TenMuaGiai]) VALUES (4, N'Bundesliga')
INSERT [dbo].[MuaGiai] ([Id], [TenMuaGiai]) VALUES (5, N'Copa Libertadores')
INSERT [dbo].[MuaGiai] ([Id], [TenMuaGiai]) VALUES (6, N'Copa del Rey')
INSERT [dbo].[MuaGiai] ([Id], [TenMuaGiai]) VALUES (7, N'Europa League')
INSERT [dbo].[MuaGiai] ([Id], [TenMuaGiai]) VALUES (8, N'Premier League Nga')
INSERT [dbo].[MuaGiai] ([Id], [TenMuaGiai]) VALUES (9, N'Ligue 1')
INSERT [dbo].[MuaGiai] ([Id], [TenMuaGiai]) VALUES (10, N'J1 League ')
SET IDENTITY_INSERT [dbo].[MuaGiai] OFF
GO
SET IDENTITY_INSERT [dbo].[PhanQuyen] ON 

INSERT [dbo].[PhanQuyen] ([Id], [TenPQ]) VALUES (1, N'Admin')
INSERT [dbo].[PhanQuyen] ([Id], [TenPQ]) VALUES (2, N'User')
SET IDENTITY_INSERT [dbo].[PhanQuyen] OFF
GO
SET IDENTITY_INSERT [dbo].[SanVD] ON 

INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (1, N'Old tranford', N'74140', N'Manchester')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (2, N'Camp Nou', N'99354', N'Barcelona, Tây Ban Nha')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (3, N'Santiago Bernabéu', N'81044', N'Madrid, Tây Ban Nha')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (4, N'Allianz Arena', N'75024', N'Munich, Đức')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (5, N'San Siro', N'80018', N'Milan, Ý')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (6, N'Wembley', N'90000', N'London, Anh')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (7, N'Maracanã', N'78838', N'Janeiro, Brazil')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (8, N'Giuseppe Meazza', N'75923', N'Milan, Ý')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (9, N'Signal Iduna Park', N'81365', N'Dortmund, Đức')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (10, N'Parc des Princes', N'47929', N'Paris, Pháp')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (11, N'Mỹ Đình', N'40192', N'Hà Nội')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (12, N'Thống Nhất', N'25000', N'Hồ Chí Minh')
INSERT [dbo].[SanVD] ([Id], [TenSVD], [SucChua], [ThanhPho]) VALUES (13, N'Bình Dương', N'20000', N'Bình Dương')
SET IDENTITY_INSERT [dbo].[SanVD] OFF
GO
SET IDENTITY_INSERT [dbo].[TaiKhoan] ON 

INSERT [dbo].[TaiKhoan] ([Id], [TenDangNhap], [MatKhau], [IdPQ], [Email], [SDT]) VALUES (1, N'admin', N'admin', 1, N'admin@gmail.com', NULL)
INSERT [dbo].[TaiKhoan] ([Id], [TenDangNhap], [MatKhau], [IdPQ], [Email], [SDT]) VALUES (2, N'user', N'123456', 2, N'user@gmail.com', NULL)
INSERT [dbo].[TaiKhoan] ([Id], [TenDangNhap], [MatKhau], [IdPQ], [Email], [SDT]) VALUES (3, N'TranThiVen', N'123456', 2, NULL, NULL)
INSERT [dbo].[TaiKhoan] ([Id], [TenDangNhap], [MatKhau], [IdPQ], [Email], [SDT]) VALUES (4, N'VoPhuVinh', N'123456', 2, NULL, NULL)
INSERT [dbo].[TaiKhoan] ([Id], [TenDangNhap], [MatKhau], [IdPQ], [Email], [SDT]) VALUES (5, N'user123456', N'123456', 2, N'user123456@gmail.com', N'0132364637')
SET IDENTITY_INSERT [dbo].[TaiKhoan] OFF
GO
ALTER TABLE [dbo].[CauLacBo]  WITH CHECK ADD  CONSTRAINT [FK__CauLacBo__IdSVD__398D8EEE] FOREIGN KEY([IdSVD])
REFERENCES [dbo].[SanVD] ([Id])
GO
ALTER TABLE [dbo].[CauLacBo] CHECK CONSTRAINT [FK__CauLacBo__IdSVD__398D8EEE]
GO
ALTER TABLE [dbo].[CauThu]  WITH CHECK ADD FOREIGN KEY([IdCLB])
REFERENCES [dbo].[CauLacBo] ([Id])
GO
ALTER TABLE [dbo].[KetQua]  WITH CHECK ADD FOREIGN KEY([IdLTD])
REFERENCES [dbo].[LichThiDau] ([Id])
GO
ALTER TABLE [dbo].[LichThiDau]  WITH CHECK ADD FOREIGN KEY([IdCLB1])
REFERENCES [dbo].[CauLacBo] ([Id])
GO
ALTER TABLE [dbo].[LichThiDau]  WITH CHECK ADD FOREIGN KEY([IdCLB2])
REFERENCES [dbo].[CauLacBo] ([Id])
GO
ALTER TABLE [dbo].[LichThiDau]  WITH CHECK ADD FOREIGN KEY([IdMuaGiai])
REFERENCES [dbo].[MuaGiai] ([Id])
GO
ALTER TABLE [dbo].[LichThiDau]  WITH CHECK ADD  CONSTRAINT [FK__LichThiDa__IdSVD__4AB81AF0] FOREIGN KEY([IdSVD])
REFERENCES [dbo].[SanVD] ([Id])
GO
ALTER TABLE [dbo].[LichThiDau] CHECK CONSTRAINT [FK__LichThiDa__IdSVD__4AB81AF0]
GO
ALTER TABLE [dbo].[TaiKhoan]  WITH CHECK ADD FOREIGN KEY([IdPQ])
REFERENCES [dbo].[PhanQuyen] ([Id])
GO
ALTER TABLE [dbo].[XepHang]  WITH CHECK ADD FOREIGN KEY([IdCLB])
REFERENCES [dbo].[CauLacBo] ([Id])
GO
ALTER TABLE [dbo].[XepHang]  WITH CHECK ADD FOREIGN KEY([IdMuaGiai])
REFERENCES [dbo].[MuaGiai] ([Id])
GO
--ALTER TABLE [dbo].TaiKhoan ADD  [Email] nvarchar(250) null
--GO
--ALTER TABLE [dbo].TaiKhoan ADD  [SDT] varchar(10) null
--GO
--ALTER TABLE [dbo].[LichThiDau]
--ADD CONSTRAINT DateCheck CHECK (NgayThiDau >= CAST(GETDATE() AS DATE))
--GO
