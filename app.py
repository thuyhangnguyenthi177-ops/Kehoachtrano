import streamlit as st

st.title("KẾ HOẠCH TRẢ NỢ VAY")

STV = st.number_input("Số tiền vay", value=700_000_000)
THV = st.number_input("Thời hạn vay (năm)", value=5)
LS1 = st.number_input("Lãi suất 3 tháng đầu (%)", value=9.0) / 100
LS2 = st.number_input("Lãi suất huy động (%)", value=10.0) / 100
BM = st.number_input("Biên độ (%)", value=4.0) / 100

if st.button("TÍNH TOÁN"):
    GOC = STV / (THV * 12)
    du_no = STV

    for ky in range(1, 6):
        LS = LS1 if ky <= 3 else LS2 + BM
        ngay = 19 if ky == 1 else 30
        LAI = du_no * LS * ngay / 365
        TONG = GOC + LAI

        st.write(f"Kỳ {ky}: Lãi = {LAI:,.0f} VNĐ | "
                 f"Gốc = {GOC:,.0f} VNĐ | "
                 f"Tổng trả = {TONG:,.0f} VNĐ")

        du_no -= GOC
