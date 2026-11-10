import customtkinter as ctk
from tkinter import ttk, messagebox
import pyodbc


# =========================================================
# CẤU HÌNH
# =========================================================

SERVER_NAME = r'.\SQLEXPRESS01'
DB_NAME = 'QuanLyCacTuyenDuLich'


# =========================================================
# CLASS QUẢN LÝ ĐIỂM ĐẾN
# =========================================================

class QuanLyDiemDen(ctk.CTkFrame):

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
    # KẾT NỐI SQL SERVER
    # =====================================================

    def get_connection(self):

        try:
            conn_str = (
                "DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={SERVER_NAME};"
                f"DATABASE={DB_NAME};"
                "Trusted_Connection=yes;"
            )

            return pyodbc.connect(conn_str)

        except Exception as e:
            messagebox.showerror(
                "Lỗi kết nối",
                f"Không thể kết nối SQL Server:\n\n{e}"
            )

            return None

    # =====================================================
    # TẠO GIAO DIỆN
    # =====================================================

    def create_interface(self):

        # =================================================
        # THANH ĐIỀU HƯỚNG
        # =================================================

        nav_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        nav_frame.pack(
            fill="x",
            padx=15,
            pady=5
        )

        btn_quay_lai = ctk.CTkButton(
            nav_frame,
            text="QUAY LẠI TRANG CHỦ",
            command=self.quay_lai,
            width=180,
            height=35,
            font=("Times New Roman", 13, "bold"),
            fg_color="#57595A",
            hover_color="#3C3F40",
            text_color="white"
        )

        btn_quay_lai.pack(side="left", padx=3)

        cac_chuc_nang = [
            ("QUẢN LÝ ĐIỂM ĐẾN", 165),
            ("QUẢN LÝ TUYẾN DU LỊCH", 165),
            ("QUẢN LÝ KHÁCH HÀNG", 165),
            ("QUẢN LÝ ĐẶT TOUR", 165),
            ("QUẢN LÝ TÀI KHOẢN", 165)
        ]

        for ten, chieu_rong in cac_chuc_nang:

            dang_mo = ten == "QUẢN LÝ ĐIỂM ĐẾN"

            ctk.CTkButton(
                nav_frame,
                text=ten,
                command=lambda t=ten: self.chuyen_chuc_nang(t),
                width=chieu_rong,
                height=35,
                font=(
                    "Times New Roman",
                    13,
                    "bold" if dang_mo else "normal"
                ),
                fg_color="#C8B99A" if dang_mo else "#57595A",
                hover_color="#B7A582" if dang_mo else "#3C3F40",
                text_color="#333333" if dang_mo else "white"
            ).pack(side="left", padx=3)

        # =================================================
        # TIÊU ĐỀ
        # =================================================

        title = ctk.CTkLabel(
            self,
            text="QUẢN LÝ CÁC ĐIỂM ĐẾN",
            font=("Times New Roman", 22, "bold"),
            text_color="#3369A7"
        )

        title.pack(pady=10)

        # =================================================
        # KHUNG NHẬP DỮ LIỆU
        # =================================================

        input_frame = ctk.CTkFrame(
            self,
            fg_color="#FBF8F1",
            corner_radius=12
        )

        input_frame.pack(
            fill="x",
            padx=15,
            pady=5
        )

        # MÃ ĐIỂM ĐẾN

        ctk.CTkLabel(
            input_frame,
            text="Mã điểm đến:",
            font=("Times New Roman", 16)
        ).grid(row=0, column=0, padx=8, pady=6, sticky="w")

        self.txtMaDiemDen = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMaDiemDen.grid(row=0, column=1, padx=8, pady=6)

        # TÊN ĐIỂM ĐẾN

        ctk.CTkLabel(
            input_frame,
            text="Tên điểm đến:",
            font=("Times New Roman", 16)
        ).grid(row=0, column=2, padx=8, pady=6, sticky="w")

        self.txtTenDiemDen = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtTenDiemDen.grid(row=0, column=3, padx=8, pady=6)

        # TỈNH / THÀNH PHỐ

        ctk.CTkLabel(
            input_frame,
            text="Tỉnh/Thành phố:",
            font=("Times New Roman", 16)
        ).grid(row=1, column=0, padx=8, pady=6, sticky="w")

        self.txtTinhThanh = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtTinhThanh.grid(row=1, column=1, padx=8, pady=6)

        # ĐỊA CHỈ

        ctk.CTkLabel(
            input_frame,
            text="Địa chỉ:",
            font=("Times New Roman", 16)
        ).grid(row=1, column=2, padx=8, pady=6, sticky="w")

        self.txtDiaChi = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtDiaChi.grid(row=1, column=3, padx=8, pady=6)

        # MÔ TẢ

        ctk.CTkLabel(
            input_frame,
            text="Mô tả:",
            font=("Times New Roman", 16)
        ).grid(row=2, column=0, padx=8, pady=6, sticky="w")

        self.txtMoTa = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMoTa.grid(row=2, column=1, padx=8, pady=6)

        # =================================================
        # KHUNG BẢNG
        # =================================================

        table_frame = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=12
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=5
        )

        # CẤU HÌNH BẢNG

        style = ttk.Style()

        style.configure(
            "Treeview",
            font=("Times New Roman", 30),
            rowheight=45,
            background="white",
            foreground="black",
            fieldbackground="white"
        )

        style.configure(
            "Treeview.Heading",
            font=("Times New Roman", 28, "bold"),
            background="#D9D9D9",
            foreground="black"
        )

        style.map(
            "Treeview",
            background=[("selected", "#B7D7F0")],
            foreground=[("selected", "black")]
        )

        # CỘT BẢNG

        columns = (
            "MaDiemDen",
            "TenDiemDen",
            "TinhThanh",
            "DiaChi",
            "MoTa"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        # TÊN CỘT

        self.tree.heading("MaDiemDen", text="Mã điểm đến")
        self.tree.heading("TenDiemDen", text="Tên điểm đến")
        self.tree.heading("TinhThanh", text="Tỉnh/Thành")
        self.tree.heading("DiaChi", text="Địa chỉ")
        self.tree.heading("MoTa", text="Mô tả")

        # ĐỘ RỘNG CỘT

        self.tree.column("MaDiemDen", width=90, anchor="center")
        self.tree.column("TenDiemDen", width=200, anchor="center")
        self.tree.column("TinhThanh", width=100, anchor="center")
        self.tree.column("DiaChi", width=200, anchor="center")
        self.tree.column("MoTa", width=400, anchor="center")

        self.tree.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

        # CHỌN DÒNG

        self.tree.bind(
            "<ButtonRelease-1>",
            self.chon_dong
        )

        # =================================================
        # KHUNG NÚT CHỨC NĂNG
        # =================================================

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=15,
            pady=8
        )

        # NHÓM 4 NÚT BÊN TRÁI

        left_frame = ctk.CTkFrame(
            button_frame,
            fg_color="transparent"
        )

        left_frame.pack(side="left")

        self.btnThem = ctk.CTkButton(
            left_frame,
            text="THÊM",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#2196F3",
            hover_color="#1976D2",
            command=self.them_diem_den
        )

        self.btnThem.pack(side="left", padx=4)

        self.btnSua = ctk.CTkButton(
            left_frame,
            text="SỬA",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#FF9800",
            hover_color="#E68900",
            command=self.sua_diem_den
        )

        self.btnSua.pack(side="left", padx=4)

        self.btnXoa = ctk.CTkButton(
            left_frame,
            text="XÓA",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#F44336",
            hover_color="#D32F2F",
            command=self.xoa_diem_den
        )

        self.btnXoa.pack(side="left", padx=4)

        self.btnLamMoi = ctk.CTkButton(
            left_frame,
            text="LÀM MỚI",
            width=130,
            height=40,
            font=("Times New Roman", 14, "bold"),
            fg_color="#607D8B",
            hover_color="#455A64",
            command=self.lam_moi
        )

        self.btnLamMoi.pack(side="left", padx=4)

        # ĐƯỜNG KẺ PHÂN CÁCH

        vach_ngan = ctk.CTkFrame(
            button_frame,
            width=2,
            height=40,
            fg_color="#B7A582"
        )

        vach_ngan.pack(
            side="left",
            padx=8
        )

        # NÚT TÌM KIẾM

        self.btnTimKiem = ctk.CTkButton(
            button_frame,
            text="⌕  TÌM KIẾM",
            width=130,
            height=40,
            font=("Times New Roman", 13, "bold"),
            fg_color="#D6E8F8",
            hover_color="#B8D8F5",
            text_color="#1565C0",
            command=self.tim_kiem
        )

        self.btnTimKiem.pack(
            side="left",
            padx=4
        )

        # CHỮ TÌM KIẾM

        lblTimKiem = ctk.CTkLabel(
            button_frame,
            text="Tìm kiếm:",
            font=("Times New Roman", 14)
        )

        lblTimKiem.pack(
            side="left",
            padx=4
        )

        # Ô NHẬP TỪ KHÓA

        self.txtTimKiem = ctk.CTkEntry(
            button_frame,
            width=155,
            height=40,
            font=("Times New Roman", 14),
            placeholder_text="Nhập từ khóa..."
        )

        self.txtTimKiem.pack(
            side="left",
            padx=4
        )

        # NHẤN ENTER ĐỂ TÌM KIẾM

        self.txtTimKiem.bind(
            "<Return>",
            lambda event: self.tim_kiem()
        )

        # NÚT XÓA TÌM KIẾM

        self.btnXoaTimKiem = ctk.CTkButton(
            button_frame,
            text="✖  XÓA TÌM KIẾM",
            width=130,
            height=40,
            font=("Times New Roman", 12, "bold"),
            fg_color="#F5A3A3",
            hover_color="#E88B8B",
            text_color="#A32222",
            command=self.xoa_tim_kiem
        )

        self.btnXoaTimKiem.pack(
            side="right",
            padx=4
        )

        # HIỂN THỊ DỮ LIỆU BAN ĐẦU

        self.hien_thi_diem_den()

    # =====================================================
    # HIỂN THỊ DỮ LIỆU
    # =====================================================

    def hien_thi_diem_den(self, tu_khoa=None):

        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            if tu_khoa:

                cursor.execute("""
                    SELECT
                        MaDiemDen,
                        TenDiemDen,
                        TinhThanh,
                        DiaChi,
                        MoTa
                    FROM DIEMDEN
                    WHERE
                        CAST(MaDiemDen AS NVARCHAR(50)) LIKE ?
                        OR TenDiemDen LIKE ?
                        OR TinhThanh LIKE ?
                        OR DiaChi LIKE ?
                        OR MoTa LIKE ?
                    ORDER BY MaDiemDen
                """, (
                    f"%{tu_khoa}%",
                    f"%{tu_khoa}%",
                    f"%{tu_khoa}%",
                    f"%{tu_khoa}%",
                    f"%{tu_khoa}%"
                ))

            else:

                cursor.execute("""
                    SELECT
                        MaDiemDen,
                        TenDiemDen,
                        TinhThanh,
                        DiaChi,
                        MoTa
                    FROM DIEMDEN
                    ORDER BY MaDiemDen
                """)

            rows = cursor.fetchall()

            for row in rows:

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2] if row[2] else "",
                        row[3] if row[3] else "",
                        row[4] if row[4] else ""
                    )
                )

            cursor.close()

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                f"Không thể hiển thị dữ liệu:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # TÌM KIẾM ĐIỂM ĐẾN
    # =====================================================

    def tim_kiem(self):

        tu_khoa = self.txtTimKiem.get().strip()

        if tu_khoa == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập nội dung cần tìm kiếm!"
            )
            return

        self.hien_thi_diem_den(tu_khoa)

        for item in self.tree.selection():
            self.tree.selection_remove(item)

        self.lam_trong_o_nhap()

        if not self.tree.get_children():
            messagebox.showinfo(
                "Thông báo",
                "Không tìm thấy điểm đến phù hợp!"
            )

    # =====================================================
    # XÓA TÌM KIẾM
    # =====================================================

    def xoa_tim_kiem(self):

        # Chỉ xóa nội dung ô tìm kiếm
        self.txtTimKiem.delete(0, "end")

        # Bỏ chọn dòng đang chọn trên bảng
        for item in self.tree.selection():
            self.tree.selection_remove(item)

        # Bỏ focus khỏi dòng đang chọn
        self.tree.focus("")

        # Hiển thị lại toàn bộ điểm đến
        self.hien_thi_diem_den()

    # =====================================================
    # XÓA TRỐNG CÁC Ô NHẬP
    # =====================================================

    def lam_trong_o_nhap(self):

        self.txtMaDiemDen.delete(0, "end")
        self.txtTenDiemDen.delete(0, "end")
        self.txtTinhThanh.delete(0, "end")
        self.txtDiaChi.delete(0, "end")
        self.txtMoTa.delete(0, "end")

    # =====================================================
    # CHỌN DÒNG
    # =====================================================

    def chon_dong(self, event):

        selected = self.tree.focus()

        if selected == "":
            return

        values = self.tree.item(selected, "values")

        if not values:
            return

        self.lam_trong_o_nhap()

        self.txtMaDiemDen.insert(0, values[0])
        self.txtTenDiemDen.insert(0, values[1])
        self.txtTinhThanh.insert(0, values[2])
        self.txtDiaChi.insert(0, values[3])
        self.txtMoTa.insert(0, values[4])

    # =====================================================
    # THÊM ĐIỂM ĐẾN
    # =====================================================

    def them_diem_den(self):

        MaDiemDen = self.txtMaDiemDen.get().strip()
        TenDiemDen = self.txtTenDiemDen.get().strip()
        TinhThanh = self.txtTinhThanh.get().strip()
        DiaChi = self.txtDiaChi.get().strip()
        MoTa = self.txtMoTa.get().strip()

        if MaDiemDen == "" or TenDiemDen == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập mã điểm đến và tên điểm đến!"
            )
            return

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM DIEMDEN
                WHERE MaDiemDen = ?
                """,
                (MaDiemDen,)
            )

            if cursor.fetchone()[0] > 0:
                messagebox.showwarning(
                    "Thông báo",
                    "Mã điểm đến này đã tồn tại!"
                )
                return

            cursor.execute(
                """
                INSERT INTO DIEMDEN
                (
                    MaDiemDen,
                    TenDiemDen,
                    TinhThanh,
                    DiaChi,
                    MoTa
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (MaDiemDen, TenDiemDen, TinhThanh, DiaChi, MoTa)
            )

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Thêm điểm đến thành công!"
            )

            self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                f"Không thể thêm điểm đến:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # SỬA ĐIỂM ĐẾN
    # =====================================================

    def sua_diem_den(self):

        MaDiemDen = self.txtMaDiemDen.get().strip()
        TenDiemDen = self.txtTenDiemDen.get().strip()
        TinhThanh = self.txtTinhThanh.get().strip()
        DiaChi = self.txtDiaChi.get().strip()
        MoTa = self.txtMoTa.get().strip()

        if MaDiemDen == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn điểm đến cần sửa!"
            )
            return

        if TenDiemDen == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập tên điểm đến!"
            )
            return

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE DIEMDEN
                SET
                    TenDiemDen = ?,
                    TinhThanh = ?,
                    DiaChi = ?,
                    MoTa = ?
                WHERE MaDiemDen = ?
                """,
                (TenDiemDen, TinhThanh, DiaChi, MoTa, MaDiemDen)
            )

            if cursor.rowcount == 0:
                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy mã điểm đến cần sửa!"
                )
                return

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Sửa điểm đến thành công!"
            )

            self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                f"Không thể sửa điểm đến:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # XÓA ĐIỂM ĐẾN
    # =====================================================

    def xoa_diem_den(self):

        MaDiemDen = self.txtMaDiemDen.get().strip()

        if MaDiemDen == "":
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn điểm đến cần xóa!"
            )
            return

        xac_nhan = messagebox.askyesno(
            "Xác nhận",
            "Bạn có chắc muốn xóa điểm đến này không?"
        )

        if not xac_nhan:
            return

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM DIEMDEN
                WHERE MaDiemDen = ?
                """,
                (MaDiemDen,)
            )

            if cursor.rowcount == 0:
                messagebox.showwarning(
                    "Thông báo",
                    "Không tìm thấy mã điểm đến cần xóa!"
                )
                return

            conn.commit()

            messagebox.showinfo(
                "Thông báo",
                "Xóa điểm đến thành công!"
            )

            self.lam_moi()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa điểm đến này.\n\n"
                "Có thể điểm đến đang được sử dụng ở bảng TUYEN_DL.\n\n"
                f"Chi tiết:\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # LÀM MỚI
    # =====================================================

    def lam_moi(self):

        self.lam_trong_o_nhap()

        self.txtTimKiem.delete(0, "end")

        for item in self.tree.selection():
            self.tree.selection_remove(item)

        self.tree.focus("")

        self.hien_thi_diem_den()


# =========================================================
# CHẠY RIÊNG FILE ĐỂ KIỂM TRA
# =========================================================

if __name__ == "__main__":

    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("1100x650")
    app.configure(fg_color="#F3EBDD")

    giao_dien = QuanLyDiemDen(
        app,
        lambda: messagebox.showinfo(
            "Thông báo",
            "Đây là chế độ chạy thử riêng."
        )
    )

    giao_dien.pack(fill="both", expand=True)

    app.mainloop()