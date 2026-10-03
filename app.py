import streamlit as st
st.image("logo.jpg.jpg")

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính lãi tiền gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("💰 APP TÍNH LÃI GỬI TIẾT KIỆM_PHAN LÊ THU HIỀN")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi và tổng số tiền nhận được.")

st.divider()

# =========================
# NHẬP THÔNG TIN
# =========================

# Số tiền gửi
so_tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0,
    value=10_000_000,
    step=1_000_000,
    format="%d"
)

# Kỳ hạn
ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

# Lãi suất
lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1
)

# Hình thức nhận lãi
hinh_thuc_nhan_lai = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# =========================
# TÍNH TOÁN
# =========================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Quy đổi lãi suất từ % sang số thập phân
    lai_suat_nam = lai_suat / 100

    # Thời gian gửi tính theo năm
    thoi_gian_nam = ky_han / 12

    # Tổng tiền lãi
    tong_tien_lai = so_tien_gui * lai_suat_nam * thoi_gian_nam

    # Số kỳ nhận lãi
    if hinh_thuc_nhan_lai == "Cuối kỳ":
        so_ky = 1

    elif hinh_thuc_nhan_lai == "Hàng tháng":
        so_ky = ky_han

    else:  # Hàng quý
        so_ky = ky_han / 3

    # Tiền lãi định kỳ
    tien_lai_dinh_ky = tong_tien_lai / so_ky

    # Tổng tiền gốc + lãi
    tong_tien_nhan = so_tien_gui + tong_tien_lai

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

    st.success("✅ TÍNH TOÁN THÀNH CÔNG")

    st.subheader("📊 Kết quả")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "💰 Tiền lãi định kỳ",
            f"{tien_lai_dinh_ky:,.0f} VNĐ"
        )

        st.metric(
            "📈 Tổng tiền lãi",
            f"{tong_tien_lai:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "💵 Tiền gốc",
            f"{so_tien_gui:,.0f} VNĐ"
        )

        st.metric(
            "🏦 Tổng gốc + lãi",
            f"{tong_tien_nhan:,.0f} VNĐ"
        )

    st.divider()

    # =========================
    # THÔNG TIN CHI TIẾT
    # =========================

    st.subheader("📋 Thông tin khoản gửi")

    st.write(f"**Số tiền gửi:** {so_tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc_nhan_lai}")

    if hinh_thuc_nhan_lai == "Cuối kỳ":
        st.info(
            f"Bạn nhận toàn bộ tiền lãi vào cuối kỳ: "
            f"**{tong_tien_lai:,.0f} VNĐ**"
        )

    elif hinh_thuc_nhan_lai == "Hàng tháng":
        st.info(
            f"Mỗi tháng bạn nhận khoảng: "
            f"**{tien_lai_dinh_ky:,.0f} VNĐ**"
        )

    else:
        st.info(
            f"Mỗi quý bạn nhận khoảng: "
            f"**{tien_lai_dinh_ky:,.0f} VNĐ**"
        )

# =========================
# GHI CHÚ
# =========================

st.caption(
    "ℹ️ Công thức: Tiền lãi = Tiền gửi × Lãi suất năm × Số tháng / 12. "
    "Kết quả mang tính tham khảo và chưa tính thuế/phí hoặc các điều kiện đặc biệt của ngân hàng."
)
