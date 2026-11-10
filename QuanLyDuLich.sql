CREATE DATABASE QuanLyCacTuyenDuLich
ON 
(
    NAME = QuanLyTuyenDuLich_Data,
    FILENAME = 'D:\QuanLyTuyenDuLich.mdf',
    SIZE = 10,
    MAXSIZE = 50,
    FILEGROWTH = 5
)
LOG ON
(
    NAME = QuanLyCacTuyenDuLich_Log,
    FILENAME = 'D:\QuanLyTuyenDuLich_log.ldf',
    SIZE = 10,
    MAXSIZE = 50,
    FILEGROWTH = 5
);
USE QuanLyCacTuyenDuLich;

CREATE TABLE DIEMDEN
(
    MaDiemDen VARCHAR(10) PRIMARY KEY,
    TenDiemDen NVARCHAR(100) NOT NULL,
    TinhThanh NVARCHAR(100),
    DiaChi NVARCHAR(200),
    MoTa NVARCHAR(MAX)
);

CREATE TABLE TUYEN_DL
(
    MaTuyen VARCHAR(10) PRIMARY KEY,
    TenTuyen NVARCHAR(150) NOT NULL,
    MaDiemDen VARCHAR(10) NOT NULL,
    PhuongTien NVARCHAR(100),
    NgayKhoiHanh DATE,
    SoNgay INT DEFAULT 1,
    Gia DECIMAL(18,2) DEFAULT 0,
    MoTa NVARCHAR(MAX),

    FOREIGN KEY (MaDiemDen)
        REFERENCES DIEMDEN(MaDiemDen)
)

CREATE TABLE KHACHHANG
(
    MaKhachHang VARCHAR(10) PRIMARY KEY,
    HoTen NVARCHAR(100) NOT NULL,
    SoDienThoai VARCHAR(15),
    Email VARCHAR(100),
    DiaChi NVARCHAR(200)
);

CREATE TABLE DATTOUR
(
    MaDatTour VARCHAR(10) PRIMARY KEY,
    MaKhachHang VARCHAR(10) NOT NULL,
    MaTuyen VARCHAR(10) NOT NULL,
    NgayDat DATE,
    SoLuongNguoi INT DEFAULT 1,
    TongTien DECIMAL(18,2) DEFAULT 0,
    TrangThai NVARCHAR(50) DEFAULT N'Chờ xác nhận',

    FOREIGN KEY (MaKhachHang)
        REFERENCES KHACHHANG(MaKhachHang),

    FOREIGN KEY (MaTuyen)
        REFERENCES TUYEN_DL(MaTuyen)
);


CREATE TABLE TAIKHOAN (
    MaTaiKhoan INT IDENTITY(1,1) PRIMARY KEY,
    TenDangNhap VARCHAR(50) NOT NULL UNIQUE,
    MatKhau VARCHAR(255) NOT NULL,
    HoTen NVARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    SoDienThoai VARCHAR(15),
    Quyen NVARCHAR(20) DEFAULT N'Nhân viên',
    TrangThai BIT DEFAULT 1
);



INSERT INTO TAIKHOAN
(
   
    TenDangNhap,
    MatKhau,
    HoTen,
    Email,
    SoDienThoai,
    Quyen,
    TrangThai
)
VALUES
(
    
    'admin',
    '123456',
    N'Võ Hoàng Văn',
    'admin@gmail.com',
    '0987325414',
    N'Quản trị viên',
    1
);

INSERT INTO TAIKHOAN
(
   
    TenDangNhap,
    MatKhau,
    HoTen,
    Email,
    SoDienThoai,
    Quyen,
    TrangThai
)
VALUES
(
    
    'mt',
    '123456',
    N'Lê Trần Minh Tuệ',
    'mt@gmail.com',
    '0856321892',
    N'Nhân viên',
    1
);