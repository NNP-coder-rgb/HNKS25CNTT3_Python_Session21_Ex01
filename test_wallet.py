import pytest
# Gọi chính xác từ file Bai1 sang để thực hiện kiểm thử
from Bai1 import deposit_logic, transfer_logic

INITIAL_BALANCE = 5000000

def test_deposit_success():
    """Kiểm tra nạp tiền đúng có tăng số dư không."""
    new_balance = deposit_logic(INITIAL_BALANCE, 2000000)
    assert new_balance == 7000000


def test_transfer_insufficient_balance():
    """Kiểm tra hàm chuyển tiền có return đoạn text lỗi khi số dư không đủ."""
    result = transfer_logic(INITIAL_BALANCE, "0912345678", 6000000)
    assert result == "Giao dịch thất bại: Số dư của bạn không đủ."


def test_invalid_amount():
    """Kiểm tra xem có return đoạn text lỗi khi nạp tiền âm không."""
    result = deposit_logic(INITIAL_BALANCE, -500000)
    assert result == "Lỗi: Số tiền giao dịch phải lớn hơn 0."