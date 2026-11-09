import customtkinter as ctk
from tkinter import ttk, messagebox
import pyodbc
from datetime import datetime


# =========================================================
# CẤU HÌNH
# =========================================================

SERVER_NAME = r'.\SQLEXPRESS01'
DB_NAME = 'QuanLyCacTuyenDuLich'

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


# =========================================================
# CLASS QUẢN LÝ ĐẶT TOUR
# =========================================================

class QuanLyDatTour(ctk.CTkFrame):

    def __init__(self, master, quay_lai):
        super().__init__(master, fg_color="#F3EBDD")

        self.quay_lai = quay_lai

        self.create_interface()

    # =====================================================
    # CHUYỂN SANG CHỨC NĂNG KHÁC
    # =====================================================

    def chuyen_chuc_nang(self, ten_chuc_nang):

        ung_dung = self.winfo_toplevel()

        if hasattr(ung_dung, "mo_chuc_nang"):
            ung_dung.mo_chuc_nang(ten_chuc_nang)
        else:
            messagebox.showerror(
                "Lỗi",
                "Không tìm thấy chức năng chuyển trang! Vui lòng đăng nhập để thực hiện!"
            )

    # =====================================================
    # KẾT NỐI DATABASE
    # =====================================================

    def ket_noi(self):

        try:
            conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={SERVER_NAME};"
                f"DATABASE={DB_NAME};"
                "Trusted_Connection=yes;"
            )

            return conn

        except Exception as e:
            messagebox.showerror(
                "Lỗi kết nối",
                f"Không thể kết nối cơ sở dữ liệu!\n\n{e}"
            )

            return None

    # =====================================================
    # TẠO GIAO DIỆN
    # =====================================================

    def create_interface(self):

        # ================= THANH ĐIỀU HƯỚNG =================

        nav_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        nav_frame.pack(
            fill="x",
            padx=15,
            pady=(10, 0)
        )

        btn_quay_lai = ctk.CTkButton(
            nav_frame,
            text="QUAY LẠI TRANG CHỦ",
            width=155,
            height=35,
            font=("Times New Roman", 12, "bold"),
            fg_color="#57595A",
            hover_color="#3C3F40",
            text_color="white",
            command=self.quay_lai
        )

        btn_quay_lai.pack(side="left", padx=3)

        cac_chuc_nang = [
            ("QUẢN LÝ ĐIỂM ĐẾN", "QUẢN LÝ ĐIỂM ĐẾN"),
            ("QUẢN LÝ KHÁCH HÀNG", "QUẢN LÝ KHÁCH HÀNG"),
            ("QUẢN LÝ ĐẶT TOUR", "QUẢN LÝ ĐẶT TOUR"),
            ("QUẢN LÝ TUYẾN DU LỊCH", "QUẢN LÝ TUYẾN DU LỊCH"),
            ("QUẢN LÝ TÀI KHOẢN", "QUẢN LÝ TÀI KHOẢN")
        ]

        for ten, ma in cac_chuc_nang:

            dang_mo = ma == "QUẢN LÝ ĐẶT TOUR"

            btn = ctk.CTkButton(
                nav_frame,
                text=ten,
                width=155,
                height=35,
                font=(
                    "Times New Roman",
                    11,
                    "bold" if dang_mo else "normal"
                ),
                fg_color="#D8C7A5" if dang_mo else "#57595A",
                hover_color="#C7B38D" if dang_mo else "#3C3F40",
                text_color="#333333" if dang_mo else "white",
                command=lambda m=ma: self.chuyen_chuc_nang(m)
            )

            btn.pack(side="left", padx=3)

        # ================= TIÊU ĐỀ =================

        title = ctk.CTkLabel(
            self,
            text="QUẢN LÝ ĐẶT TOUR",
            font=("Times New Roman", 26, "bold"),
            text_color="#1565C0"
        )

        title.pack(pady=15)

        # ================= KHUNG NHẬP =================

        input_frame = ctk.CTkFrame(
            self,
            width=1050,
            height=230,
            fg_color="#FBF8F1",
            corner_radius=10
        )

        input_frame.pack(pady=5)
        input_frame.pack_propagate(False)

        # HÀNG 1

        ctk.CTkLabel(
            input_frame,
            text="Mã đặt tour:",
            font=("Times New Roman", 16)
        ).place(x=30, y=20)

        self.txtMaDatTour = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMaDatTour.place(x=150, y=15)

        ctk.CTkLabel(
            input_frame,
            text="Mã khách hàng:",
            font=("Times New Roman", 16)
        ).place(x=550, y=20)

        self.txtMaKhachHang = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMaKhachHang.place(x=700, y=15)

        # HÀNG 2

        ctk.CTkLabel(
            input_frame,
            text="Mã tuyến:",
            font=("Times New Roman", 16)
        ).place(x=30, y=75)

        self.txtMaTuyen = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 14),
            justify="center"
        )

        self.txtMaTuyen.place(x=150, y=70)

        ctk.CTkLabel(
            input_frame,
            text="Ngày đặt:",
            font=("Times New Roman", 16)
        ).place(x=550, y=75)

        self.txtNgayDat = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtNgayDat.place(x=700, y=70)

        # HÀNG 3

        ctk.CTkLabel(
            input_frame,
            text="Số lượng người:",
            font=("Times New Roman", 16)
        ).place(x=30, y=130)

        self.txtSoLuongNguoi = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtSoLuongNguoi.place(x=150, y=125)

        ctk.CTkLabel(
            input_frame,
            text="Tổng tiền:",
            font=("Times New Roman", 16)
        ).place(x=550, y=130)

        self.txtTongTien = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtTongTien.place(x=700, y=125)

        # HÀNG 4 - TRẠNG THÁI

        ctk.CTkLabel(
            input_frame,
            text="Trạng thái:",
            font=("Times New Roman", 16)
        ).place(x=30, y=185)

        self.txtTrangThai = ctk.CTkComboBox(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 15),
            values=[
                "Chờ xác nhận",
                "Đã xác nhận",
                "Đã hủy",
                "Hoàn thành"
            ],
            justify="center"
        )

        self.txtTrangThai.place(x=150, y=180)
        self.txtTrangThai.set("")

        # ================= KHUNG BẢNG =================

        table_frame = ctk.CTkFrame(
            self,
            width=1050,
            height=230,
            fg_color="white"
        )

        table_frame.pack(pady=5)
        table_frame.pack_propagate(False)

        columns = (
            "MaDatTour",
            "MaKhachHang",
            "MaTuyen",
            "NgayDat",
            "SoLuongNguoi",
            "TongTien",
            "TrangThai"
        )

        style = ttk.Style()

        style.configure(
            "Treeview.Heading",
            font=("Times New Roman", 26, "bold")
        )

        style.configure(
            "Treeview",
            font=("Times New Roman", 24),
            rowheight=45
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=8
        )

        headings = {
            "MaDatTour": "Mã đặt tour",
            "MaKhachHang": "Mã khách hàng",
            "MaTuyen": "Mã tuyến",
            "NgayDat": "Ngày đặt",
            "SoLuongNguoi": "Số lượng",
            "TongTien": "Tổng tiền",
            "TrangThai": "Trạng thái"
        }

        widths = {
            "MaDatTour": 120,
            "MaKhachHang": 130,
            "MaTuyen": 110,
            "NgayDat": 120,
            "SoLuongNguoi": 100,
            "TongTien": 150,
            "TrangThai": 180
        }

        for col in columns:

            self.tree.heading(
                col,
                text=headings[col],
                anchor="center"
            )

            self.tree.column(
                col,
                width=widths[col],
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree.bind(
            "<ButtonRelease-1>",
            self.chon_dong
        )

        # ================= NÚT CHỨC NĂNG =================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(pady=8)

        self.btnThem = ctk.CTkButton(
            button_frame,
            text="THÊM",
            width=150,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#2196F3",
            command=self.them
        )

        self.btnThem.grid(row=0, column=0, padx=10)

        self.btnSua = ctk.CTkButton(
            button_frame,
            text="SỬA",
            width=150,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#FF9800",
            command=self.sua
        )

        self.btnSua.grid(row=0, column=1, padx=10)

        self.btnXoa = ctk.CTkButton(
            button_frame,
            text="XÓA",
            width=150,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#F44336",
            command=self.xoa
        )

        self.btnXoa.grid(row=0, column=2, padx=10)

        self.btnLamMoi = ctk.CTkButton(
            button_frame,
            text="LÀM MỚI",
            width=150,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#607D8B",
            command=self.lam_moi
        )

        self.btnLamMoi.grid(row=0, column=3, padx=10)

        self.load_data()

    # =====================================================
    # HIỂN THỊ DỮ LIỆU
    # =====================================================

    def load_data(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = self.ket_noi()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    MaDatTour,
                    MaKhachHang,
                    MaTuyen,
                    NgayDat,
                    SoLuongNguoi,
                    TongTien,
                    TrangThai
                FROM DATTOUR
                ORDER BY MaDatTour
            """)

            rows = cursor.fetchall()

            for row in rows:
                self.tree.insert("", "end", values=tuple(row))

            cursor.close()

        except Exception as e:
            messagebox.showerror(
                "Lỗi tải dữ liệu",
                str(e)
            )

        finally:
            conn.close()

    # =====================================================
    # CHỌN DÒNG TRÊN BẢNG
    # =====================================================

    def chon_dong(self, event):

        selected = self.tree.selection()

        if not selected:
            return

        data = self.tree.item(selected[0], "values")

        self.lam_trong_o_nhap()

        self.txtMaDatTour.insert(0, data[0])
        self.txtMaKhachHang.insert(0, data[1])
        self.txtMaTuyen.insert(0, data[2])
        self.txtNgayDat.insert(0, data[3])
        self.txtSoLuongNguoi.insert(0, data[4])
        self.txtTongTien.insert(0, data[5])
        self.txtTrangThai.set(data[6])

        self.txtMaDatTour.configure(state="disabled")

    # =====================================================
    # XÓA TRẮNG Ô NHẬP
    # =====================================================

    def lam_trong_o_nhap(self):

        self.txtMaDatTour.configure(state="normal")

        self.txtMaDatTour.delete(0, "end")
        self.txtMaKhachHang.delete(0, "end")
        self.txtMaTuyen.delete(0, "end")
        self.txtNgayDat.delete(0, "end")
        self.txtSoLuongNguoi.delete(0, "end")
        self.txtTongTien.delete(0, "end")
        self.txtTrangThai.set("")

    # =====================================================
    # KIỂM TRA DỮ LIỆU
    # =====================================================

    def kiem_tra_du_lieu(self):

        ma_dat_tour = self.txtMaDatTour.get().strip()
        ma_khach_hang = self.txtMaKhachHang.get().strip()
        ma_tuyen = self.txtMaTuyen.get().strip()
        ngay_dat = self.txtNgayDat.get().strip()
        so_luong = self.txtSoLuongNguoi.get().strip()
        tong_tien = self.txtTongTien.get().strip()
        trang_thai = self.txtTrangThai.get().strip()

        if not ma_dat_tour or not ma_khach_hang or not ma_tuyen:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập mã đặt tour, mã khách hàng và mã tuyến!"
            )
            return None

        if (
            len(ma_dat_tour) > 10
            or len(ma_khach_hang) > 10
            or len(ma_tuyen) > 10
        ):
            messagebox.showwarning(
                "Thông báo",
                "Các mã không được vượt quá 10 ký tự!"
            )
            return None

        try:
            ngay_dat = datetime.strptime(
                ngay_dat,
                "%Y-%m-%d"
            ).date()

            so_luong = int(so_luong)

            if so_luong < 1:
                raise ValueError

            tong_tien = float(tong_tien)

            if tong_tien < 0:
                raise ValueError

        except ValueError:
            messagebox.showwarning(
                "Thông báo",
                "Ngày đặt phải theo định dạng YYYY-MM-DD, "
                "số lượng phải từ 1 trở lên và tổng tiền không được âm!"
            )
            return None

        if not trang_thai:
            trang_thai = "Chờ xác nhận"

        return (
            ma_dat_tour,
            ma_khach_hang,
            ma_tuyen,
            ngay_dat,
            so_luong,
            tong_tien,
            trang_thai
        )

    # =====================================================
    # THÊM ĐẶT TOUR
    # =====================================================

    def them(self):

        data = self.kiem_tra_du_lieu()

        if data is None:
            return

        conn = self.ket_noi()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO DATTOUR
                (
                    MaDatTour,
                    MaKhachHang,
                    MaTuyen,
                    NgayDat,
                    SoLuongNguoi,
                    TongTien,
                    TrangThai
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, data)

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Thêm đặt tour thành công!"
            )

            self.load_data()
            self.lam_moi()

            cursor.close()

        except Exception as e:
            conn.rollback()

            messagebox.showerror(
                "Lỗi thêm dữ liệu",
                f"Không thể thêm đặt tour!\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # SỬA ĐẶT TOUR
    # =====================================================

    def sua(self):

        ma_dat_tour = self.txtMaDatTour.get().strip()

        if not ma_dat_tour:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn đặt tour cần sửa!"
            )
            return

        data = self.kiem_tra_du_lieu()

        if data is None:
            return

        conn = self.ket_noi()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE DATTOUR
                SET
                    MaKhachHang = ?,
                    MaTuyen = ?,
                    NgayDat = ?,
                    SoLuongNguoi = ?,
                    TongTien = ?,
                    TrangThai = ?
                WHERE MaDatTour = ?
            """, (
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                ma_dat_tour
            ))

            if cursor.rowcount == 0:
                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy mã đặt tour cần sửa!"
                )

            else:
                conn.commit()

                messagebox.showinfo(
                    "Thông báo",
                    "Cập nhật đặt tour thành công!"
                )

                self.load_data()
                self.lam_moi()

            cursor.close()

        except Exception as e:
            conn.rollback()

            messagebox.showerror(
                "Lỗi sửa dữ liệu",
                f"Không thể sửa đặt tour!\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # XÓA ĐẶT TOUR
    # =====================================================

    def xoa(self):

        ma_dat_tour = self.txtMaDatTour.get().strip()

        if not ma_dat_tour:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn đặt tour cần xóa!"
            )
            return

        xac_nhan = messagebox.askyesno(
            "Xác nhận",
            f"Bạn có chắc chắn muốn xóa đặt tour {ma_dat_tour} không?"
        )

        if not xac_nhan:
            return

        conn = self.ket_noi()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM DATTOUR
                WHERE MaDatTour = ?
            """, (ma_dat_tour,))

            if cursor.rowcount == 0:
                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy đặt tour cần xóa!"
                )

            else:
                conn.commit()

                messagebox.showinfo(
                    "Thông báo",
                    "Xóa đặt tour thành công!"
                )

                self.load_data()
                self.lam_moi()

            cursor.close()

        except Exception as e:
            conn.rollback()

            messagebox.showerror(
                "Lỗi xóa dữ liệu",
                f"Không thể xóa đặt tour!\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # LÀM MỚI
    # =====================================================

    def lam_moi(self):

        self.lam_trong_o_nhap()

        for item in self.tree.selection():
            self.tree.selection_remove(item)

        self.load_data()


# =========================================================
# CHẠY THỬ RIÊNG
# Chức năng chuyển trang hoạt động khi chạy từ file đăng nhập
# =========================================================

if __name__ == "__main__":

    app = ctk.CTk()
    app.geometry("1100x650")
    app.title("QUẢN LÝ ĐẶT TOUR")
    app.configure(fg_color="#F3EBDD")

    giao_dien = QuanLyDatTour(
        app,
        lambda: messagebox.showinfo(
            "Thông báo",
            "Đây là chế độ chạy thử riêng."
        )
    )

    giao_dien.pack(fill="both", expand=True)

    app.mainloop()