
import customtkinter as ctk
from tkinter import ttk, messagebox, filedialog
import pyodbc
from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side


# =========================================================
# CẤU HÌNH
# =========================================================

SERVER_NAME = r'.\SQLEXPRESS01'
DB_NAME = 'QuanLyCacTuyenDuLich'


# =========================================================
# CLASS QUẢN LÝ ĐẶT TOUR
# =========================================================

class QuanLyDatTour(ctk.CTkFrame):

    def __init__(self, master, quay_lai):
        super().__init__(master, fg_color="#F3EBDD")

        self.quay_lai = quay_lai
        self.create_interface()

    # =====================================================
    # CHUYỂN CHỨC NĂNG
    # =====================================================

    def chuyen_chuc_nang(self, ten_chuc_nang):

        ung_dung = self.winfo_toplevel()

        if hasattr(ung_dung, "mo_chuc_nang"):
            ung_dung.mo_chuc_nang(ten_chuc_nang)
        else:
            messagebox.showerror(
                "Lỗi",
                "Không tìm thấy chức năng chuyển trang!"
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

        # THANH ĐIỀU HƯỚNG

        nav_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        nav_frame.pack(fill="x", padx=15, pady=5)

        ctk.CTkButton(
            nav_frame,
            text="QUAY LẠI TRANG CHỦ",
            command=self.quay_lai,
            width=180,
            height=35,
            font=("Times New Roman", 13, "bold"),
            fg_color="#57595A",
            hover_color="#3C3F40",
            text_color="white"
        ).pack(side="left", padx=3)

        cac_chuc_nang = [
            ("QUẢN LÝ ĐIỂM ĐẾN", 165),
            ("QUẢN LÝ TUYẾN DU LỊCH", 165),
            ("QUẢN LÝ KHÁCH HÀNG", 165),
            ("QUẢN LÝ ĐẶT TOUR", 165),
            ("QUẢN LÝ TÀI KHOẢN", 165)
        ]

        for ten, chieu_rong in cac_chuc_nang:

            dang_mo = ten == "QUẢN LÝ ĐẶT TOUR"

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

        # TIÊU ĐỀ

        ctk.CTkLabel(
            self,
            text="QUẢN LÝ ĐẶT TOUR",
            font=("Times New Roman", 22, "bold"),
            text_color="#3369A7"
        ).pack(pady=10)

        # KHUNG NHẬP DỮ LIỆU

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

        # MÃ ĐẶT TOUR

        ctk.CTkLabel(
            input_frame,
            text="Mã đặt tour:",
            font=("Times New Roman", 16)
        ).grid(row=0, column=0, padx=8, pady=6, sticky="w")

        self.txtMaDatTour = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMaDatTour.grid(
            row=0,
            column=1,
            padx=8,
            pady=6
        )

        # MÃ KHÁCH HÀNG

        ctk.CTkLabel(
            input_frame,
            text="Mã khách hàng:",
            font=("Times New Roman", 16)
        ).grid(row=0, column=2, padx=8, pady=6, sticky="w")

        self.txtMaKhachHang = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMaKhachHang.grid(
            row=0,
            column=3,
            padx=8,
            pady=6
        )

        # MÃ TUYẾN

        ctk.CTkLabel(
            input_frame,
            text="Mã tuyến:",
            font=("Times New Roman", 16)
        ).grid(row=1, column=0, padx=8, pady=6, sticky="w")

        self.txtMaTuyen = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtMaTuyen.grid(
            row=1,
            column=1,
            padx=8,
            pady=6
        )

        # NGÀY ĐẶT

        ctk.CTkLabel(
            input_frame,
            text="Ngày đặt:",
            font=("Times New Roman", 16)
        ).grid(row=1, column=2, padx=8, pady=6, sticky="w")

        self.txtNgayDat = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center",
            placeholder_text="DD/MM/YYYY"
        )

        self.txtNgayDat.grid(
            row=1,
            column=3,
            padx=8,
            pady=6
        )

        # SỐ LƯỢNG NGƯỜI

        ctk.CTkLabel(
            input_frame,
            text="Số lượng người:",
            font=("Times New Roman", 16)
        ).grid(row=2, column=0, padx=8, pady=6, sticky="w")

        self.txtSoLuongNguoi = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtSoLuongNguoi.grid(
            row=2,
            column=1,
            padx=8,
            pady=6
        )

        # TỔNG TIỀN

        ctk.CTkLabel(
            input_frame,
            text="Tổng tiền:",
            font=("Times New Roman", 16)
        ).grid(row=2, column=2, padx=8, pady=6, sticky="w")

        self.txtTongTien = ctk.CTkEntry(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            justify="center"
        )

        self.txtTongTien.grid(
            row=2,
            column=3,
            padx=8,
            pady=6
        )

        # TRẠNG THÁI

        ctk.CTkLabel(
            input_frame,
            text="Trạng thái:",
            font=("Times New Roman", 16)
        ).grid(row=3, column=0, padx=8, pady=6, sticky="w")

        self.txtTrangThai = ctk.CTkComboBox(
            input_frame,
            width=270,
            height=40,
            font=("Times New Roman", 16),
            values=[
                "Chờ xác nhận",
                "Đã xác nhận",
                "Đã hủy",
                "Hoàn thành"
            ],
            justify="center"
        )

        self.txtTrangThai.grid(
            row=3,
            column=1,
            padx=8,
            pady=6
        )

        self.txtTrangThai.set("")

        # NÚT XUẤT EXCEL

        export_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        export_frame.pack(
            fill="x",
            padx=15,
            pady=5
        )

        self.btnXuatExcel = ctk.CTkButton(
            export_frame,
            text="▦  XUẤT DỮ LIỆU (EXCEL)",
            width=260,
            height=40,
            font=("Times New Roman", 15, "bold"),
            fg_color="#219653",
            hover_color="#157A3D",
            text_color="white",
            command=self.xuat_excel
        )

        self.btnXuatExcel.pack(anchor="center")

        # KHUNG BẢNG

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
            font=("Times New Roman",28, "bold"),
            background="#D9D9D9",
            foreground="black"
        )

        style.map(
            "Treeview",
            background=[("selected", "#B7D7F0")],
            foreground=[("selected", "black")]
        )

        columns = (
            "MaDatTour",
            "MaKhachHang",
            "MaTuyen",
            "NgayDat",
            "SoLuongNguoi",
            "TongTien",
            "TrangThai"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.tree.heading("MaDatTour", text="Mã đặt tour")
        self.tree.heading("MaKhachHang", text="Mã khách hàng")
        self.tree.heading("MaTuyen", text="Mã tuyến")
        self.tree.heading("NgayDat", text="Ngày đặt")
        self.tree.heading("SoLuongNguoi", text="Số lượng")
        self.tree.heading("TongTien", text="Tổng tiền")
        self.tree.heading("TrangThai", text="Trạng thái")

        self.tree.column("MaDatTour", width=120, anchor="center")
        self.tree.column("MaKhachHang", width=130, anchor="center")
        self.tree.column("MaTuyen", width=110, anchor="center")
        self.tree.column("NgayDat", width=120, anchor="center")
        self.tree.column("SoLuongNguoi", width=100, anchor="center")
        self.tree.column("TongTien", width=150, anchor="center")
        self.tree.column("TrangThai", width=180, anchor="center")

        self.tree.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

        # CHỌN DÒNG TRONG BẢNG

        self.tree.bind(
            "<ButtonRelease-1>",
            self.chon_dong
        )

        # KHUNG NÚT CHỨC NĂNG

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=15,
            pady=8
        )

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
            command=self.them
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
            command=self.sua
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
            command=self.xoa
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

        # VẠCH NGĂN

        ctk.CTkFrame(
            button_frame,
            width=2,
            height=40,
            fg_color="#B7A582"
        ).pack(side="left", padx=8)

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

        self.btnTimKiem.pack(side="left", padx=4)

        ctk.CTkLabel(
            button_frame,
            text="Tìm kiếm:",
            font=("Times New Roman", 14)
        ).pack(side="left", padx=4)

        self.txtTimKiem = ctk.CTkEntry(
            button_frame,
            width=155,
            height=40,
            font=("Times New Roman", 14),
            placeholder_text="Nhập từ khóa..."
        )

        self.txtTimKiem.pack(side="left", padx=4)

        self.txtTimKiem.bind(
            "<Return>",
            lambda event: self.tim_kiem()
        )

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

        self.hien_thi_dat_tour()

    # =====================================================
    # HIỂN THỊ DỮ LIỆU
    # =====================================================

    def hien_thi_dat_tour(self, tu_khoa=None):

        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = self.get_connection()

        if conn is None:
            return

        try:
            cursor = conn.cursor()

            if tu_khoa:

                tu_khoa_tim = f"%{tu_khoa}%"

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
                    WHERE
                        CAST(MaDatTour AS NVARCHAR(50)) LIKE ?
                        OR CAST(MaKhachHang AS NVARCHAR(50)) LIKE ?
                        OR CAST(MaTuyen AS NVARCHAR(50)) LIKE ?
                        OR CONVERT(NVARCHAR(20), NgayDat, 23) LIKE ?
                        OR CAST(SoLuongNguoi AS NVARCHAR(50)) LIKE ?
                        OR CAST(TongTien AS NVARCHAR(50)) LIKE ?
                        OR TrangThai LIKE ?
                    ORDER BY MaDatTour
                """, (
                    tu_khoa_tim,
                    tu_khoa_tim,
                    tu_khoa_tim,
                    tu_khoa_tim,
                    tu_khoa_tim,
                    tu_khoa_tim,
                    tu_khoa_tim
                ))

            else:

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

                ngay_dat = row[3]

                if ngay_dat is not None and hasattr(ngay_dat, "strftime"):
                    ngay_dat = ngay_dat.strftime("%d/%m/%Y")

                self.tree.insert(
                "",
                "end",
                values=(
                    row[0],
                    row[1],
                    row[2],
                    ngay_dat if ngay_dat else "",
                    row[4],
                    int(float(row[5])) if row[5] is not None else 0,
                    row[6]
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
    # XUẤT EXCEL
    # =====================================================

    def xuat_excel(self):

        danh_sach = []

        for item in self.tree.get_children():
            gia_tri = self.tree.item(item, "values")
            danh_sach.append(gia_tri)

        if not danh_sach:

            messagebox.showwarning(
                "Thông báo",
                "Không có dữ liệu để xuất ra Excel!"
            )
            return

        duong_dan = filedialog.asksaveasfilename(
            title="Lưu file Excel",
            defaultextension=".xlsx",
            filetypes=[("Excel Workbook", "*.xlsx")],
            initialfile="DanhSachDatTour.xlsx"
        )

        if not duong_dan:
            return

        try:

            wb = Workbook()
            ws = wb.active
            ws.title = "Danh sách đặt tour"

            tieu_de = [
                "Mã đặt tour",
                "Mã khách hàng",
                "Mã tuyến",
                "Ngày đặt",
                "Số lượng người",
                "Tổng tiền",
                "Trạng thái"
            ]

            ws.append(tieu_de)

            mau_tieu_de = PatternFill(
                fill_type="solid",
                fgColor="4472C4"
            )

            vien = Side(
                style="thin",
                color="B7B7B7"
            )

            for cell in ws[1]:

                cell.font = Font(
                    name="Times New Roman",
                    size=12,
                    bold=True,
                    color="FFFFFF"
                )

                cell.fill = mau_tieu_de

                cell.alignment = Alignment(
                    horizontal="center",
                    vertical="center"
                )

                cell.border = Border(
                    left=vien,
                    right=vien,
                    top=vien,
                    bottom=vien
                )

            for dong in danh_sach:
                ws.append(list(dong))

            for row in ws.iter_rows(
                min_row=2,
                max_row=ws.max_row
            ):

                for cell in row:

                    cell.font = Font(
                        name="Times New Roman",
                        size=12
                    )

                    cell.alignment = Alignment(
                        horizontal="center",
                        vertical="center"
                    )

                    cell.border = Border(
                        left=vien,
                        right=vien,
                        top=vien,
                        bottom=vien
                    )

            do_rong_cot = {
                "A": 18,
                "B": 20,
                "C": 15,
                "D": 18,
                "E": 20,
                "F": 20,
                "G": 22
            }

            for cot, rong in do_rong_cot.items():
                ws.column_dimensions[cot].width = rong

            ws.row_dimensions[1].height = 25

            for i in range(2, ws.max_row + 1):
                ws.row_dimensions[i].height = 22

            ws.freeze_panes = "A2"
            ws.auto_filter.ref = ws.dimensions

            wb.save(duong_dan)

            messagebox.showinfo(
                "Xuất Excel thành công",
                f"Đã xuất {len(danh_sach)} dòng dữ liệu!\n\n"
                f"File được lưu tại:\n{duong_dan}"
            )

        except PermissionError:

            messagebox.showerror(
                "Lỗi",
                "Không thể lưu file!\n"
                "Có thể file Excel đang được mở. "
                "Vui lòng đóng file rồi thử lại."
            )

        except Exception as e:

            messagebox.showerror(
                "Lỗi xuất Excel",
                f"Không thể xuất dữ liệu ra Excel:\n\n{e}"
            )

    # =====================================================
    # TÌM KIẾM
    # =====================================================

    def tim_kiem(self):

        tu_khoa = self.txtTimKiem.get().strip()

        if tu_khoa == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập nội dung cần tìm kiếm!"
            )

            self.txtTimKiem.focus()
            return

        self.hien_thi_dat_tour(tu_khoa)

        for item in self.tree.selection():
            self.tree.selection_remove(item)

        self.tree.focus("")

        self.lam_trong_o_nhap()

        if not self.tree.get_children():

            messagebox.showinfo(
                "Thông báo",
                "Không tìm thấy đặt tour phù hợp!"
            )

    # =====================================================
    # XÓA TÌM KIẾM
    # =====================================================

    def xoa_tim_kiem(self):

        self.txtTimKiem.delete(0, "end")

        for item in self.tree.selection():
            self.tree.selection_remove(item)

        self.tree.focus("")

        self.hien_thi_dat_tour()

    # =====================================================
    # XÓA TRẮNG Ô NHẬP
    # =====================================================

    def lam_trong_o_nhap(self):

        # LUÔN ĐỂ MÃ ĐẶT TOUR Ở TRẠNG THÁI CÓ THỂ NHẬP

        self.txtMaDatTour.configure(state="normal")

        self.txtMaDatTour.delete(0, "end")
        self.txtMaKhachHang.delete(0, "end")
        self.txtMaTuyen.delete(0, "end")
        self.txtNgayDat.delete(0, "end")
        self.txtSoLuongNguoi.delete(0, "end")
        self.txtTongTien.delete(0, "end")
        self.txtTrangThai.set("")

    # =====================================================
    # CHỌN DÒNG TRONG BẢNG
    # =====================================================

    def chon_dong(self, event=None):

        if event is not None:

            item = self.tree.identify_row(event.y)

            if not item:
                return

            self.tree.selection_set(item)
            self.tree.focus(item)

        selected = self.tree.focus()

        if selected == "":
            return

        values = self.tree.item(selected, "values")

        if not values:
            return

        self.lam_trong_o_nhap()

        self.txtMaDatTour.insert(0, values[0])
        self.txtMaKhachHang.insert(0, values[1])
        self.txtMaTuyen.insert(0, values[2])
        self.txtNgayDat.insert(0, values[3])
        self.txtSoLuongNguoi.insert(0, values[4])
        self.txtTongTien.insert(0, values[5])
        self.txtTrangThai.set(values[6])

        # KHÔNG KHÓA MÃ ĐẶT TOUR NỮA

        self.txtMaDatTour.configure(state="normal")

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

        if (
            not ma_dat_tour
            or not ma_khach_hang
            or not ma_tuyen
            or not ngay_dat
            or not so_luong
            or not tong_tien
        ):

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập đầy đủ thông tin!"
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

            # CHẤP NHẬN CẢ DD/MM/YYYY VÀ DD-MM-YYYY

            ngay_hop_le = None

            for dinh_dang in ("%d/%m/%Y", "%d-%m-%Y"):

                try:
                    ngay_hop_le = datetime.strptime(
                        ngay_dat,
                        dinh_dang
                    ).date()
                    break

                except ValueError:
                    continue

            if ngay_hop_le is None:
                raise ValueError("Ngày không hợp lệ")

            so_luong = int(so_luong)

            if so_luong < 1:
                raise ValueError("Số lượng không hợp lệ")

            tong_tien = int(float(tong_tien))

            if tong_tien < 0:
                raise ValueError("Tổng tiền không hợp lệ")

        except ValueError:

            messagebox.showwarning(
                "Thông báo",
                "Ngày đặt phải theo định dạng DD/MM/YYYY "
                "hoặc DD/MM/YYYY.\n"
                "Số lượng phải từ 1 trở lên và tổng tiền "
                "không được âm!"
            )
            return None

        if not trang_thai:
            trang_thai = "Chờ xác nhận"

        return (
            ma_dat_tour,
            ma_khach_hang,
            ma_tuyen,
            ngay_hop_le,
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

        conn = self.get_connection()

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

            self.lam_moi()

            cursor.close()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                f"Không thể thêm đặt tour:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # SỬA ĐẶT TOUR
    # =====================================================

    def sua(self):

        ma_dat_tour = self.txtMaDatTour.get().strip()

        if ma_dat_tour == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn hoặc nhập mã đặt tour cần sửa!"
            )
            return

        data = self.kiem_tra_du_lieu()

        if data is None:
            return

        conn = self.get_connection()

        if conn is None:
            return

        try:

            cursor = conn.cursor()

            cursor.execute("""
                UPDATE DATTOUR
                SET
                    MaDatTour = ?,
                    MaKhachHang = ?,
                    MaTuyen = ?,
                    NgayDat = ?,
                    SoLuongNguoi = ?,
                    TongTien = ?,
                    TrangThai = ?
                WHERE MaDatTour = ?
            """, (
                data[0],
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
                    "Sửa đặt tour thành công!"
                )

                self.lam_moi()

            cursor.close()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                f"Không thể sửa đặt tour:\n\n{e}"
            )

        finally:
            conn.close()

    # =====================================================
    # XÓA ĐẶT TOUR
    # =====================================================

    def xoa(self):

        ma_dat_tour = self.txtMaDatTour.get().strip()

        if ma_dat_tour == "":

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng chọn đặt tour cần xóa!"
            )
            return

        xac_nhan = messagebox.askyesno(
            "Xác nhận",
            f"Bạn có chắc muốn xóa đặt tour {ma_dat_tour} không?"
        )

        if not xac_nhan:
            return

        conn = self.get_connection()

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

                self.lam_moi()

            cursor.close()

        except Exception as e:

            conn.rollback()

            messagebox.showerror(
                "Lỗi",
                "Không thể xóa đặt tour.\n\n"
                "Có thể đặt tour đang được sử dụng ở bảng khác.\n\n"
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

        self.hien_thi_dat_tour()


# =========================================================
# CHẠY RIÊNG FILE ĐỂ KIỂM TRA
# =========================================================

if __name__ == "__main__":

    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("1100x700")
    app.title("QUẢN LÝ ĐẶT TOUR")
    app.configure(fg_color="#F3EBDD")

    giao_dien = QuanLyDatTour(
        app,
        lambda: messagebox.showinfo(
            "Thông báo",
            "Đây là chế độ chạy thử riêng."
        )
    )

    giao_dien.pack(
        fill="both",
        expand=True
    )

    app.mainloop()
