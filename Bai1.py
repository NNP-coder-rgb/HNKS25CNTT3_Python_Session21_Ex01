import logging


balance = 5000000

logging.basicConfig(
    level=logging.INFO,
    filename='momo_transactions.log',
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    encoding='utf-8'
)



def deposit_logic(current_balance, input_money):
    """Xử lý tính toán nạp tiền và trả về số dư mới hoặc chuỗi báo lỗi."""
    if input_money < 0:
        logging.error(f'InvalidAmountError: Attempted to process {input_money} VND.')
        return "Lỗi: Số tiền giao dịch phải lớn hơn 0."
    
    new_balance = current_balance + input_money
    logging.info(f'Deposit successful: +{input_money} VND. Current Balance: {new_balance} VND')
    return new_balance


def transfer_logic(current_balance, phone_number, input_money):
    """Xử lý tính toán chuyển tiền và trả về số dư mới hoặc chuỗi báo lỗi."""
    if len(phone_number) != 10:
        return "Số điện thoại phải chuẩn định dạng là 10 chữ số"
    if input_money < 0:
        logging.error(f'InvalidAmountError: Attempted to process {input_money} VND.')
        return "Lỗi: Số tiền giao dịch phải lớn hơn 0."
    if input_money > current_balance:
        logging.error(f'InsufficientBalanceError: Attempted to transfer {input_money} VND with balance {current_balance} VND.')
        return "Giao dịch thất bại: Số dư của bạn không đủ."
        
    new_balance = current_balance - input_money
    if input_money >= 10000000:
        logging.warning(f'High value transaction detected: {input_money} VND to {phone_number}')
    logging.info(f'Transfer successful: -{input_money} VND to {phone_number}. Current Balance: {new_balance} VND')
    return new_balance


def deposit_ui():
    """Giao diện nhập xuất cho chức năng nạp tiền."""
    global balance
    try:
        input_money = int(input('Nhập số tiền cần nạp: '))
        result = deposit_logic(balance, input_money)
        
        if isinstance(result, str):
            print(result)
        else:
            balance = result
            print(f'Nạp tiền thành công: +{input_money:,} VND')
            print(f'Số dư hiện tại: {balance:,} VND')
    except ValueError:
        print('Lỗi: Vui lòng nhập số tiền hợp lệ.')
        logging.error('ValueError: Invalid numeric input for deposit.')


def transfer_ui():
    """Giao diện nhập xuất cho chức năng chuyển tiền."""
    global balance
    try:
        input_phone_number = input('Nhập số điện thoại người nhận: ')
        input_money = int(input('Nhập số tiền cần chuyển: '))
        
        result = transfer_logic(balance, input_phone_number, input_money)
        
        if isinstance(result, str):
            print(result)
        else:
            balance = result
            print(f'\nChuyển tiền thành công tới số điện thoại {input_phone_number}')
            print(f'Số tiền đã chuyển: {input_money:,} VND')
            print(f'Số dư còn lại: {balance:,} VND')
    except ValueError:
        print('Lỗi: Vui lòng nhập số tiền hợp lệ.')
        logging.error('ValueError: Invalid numeric input for Transfer.')


def check_history():
    """Hiển thị 5 lịch sử giao dịch gần nhất từ file log."""
    print('--- 5 LỊCH SỬ GIAO DỊCH MỚI NHẤT ---')
    try:
        with open('momo_transactions.log', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                print('Lịch sử hệ thống đang trống.')
            else:
                for line in lines[-5:]:
                    print(line.strip())
    except FileNotFoundError:
        print('Hiện tại chưa có lịch sử giao dịch nào được ghi nhận.')


def view_balance():
    """Xem số dư tài khoản hiện tại."""
    print('--- SỐ DƯ VÍ MOMO ---')
    print(f'Số dư hiện tại: {balance:,} VND')


def display_menu():
    print('\n========== VÍ MOMO GIẢ LẬP ==========')
    print('1. Nạp tiền vào ví')
    print('2. Chuyển tiền')
    print('3. Xem lịch sử hệ thống')
    print('4. Xem số dư tài khoản')
    print('5. Thoát chương trình')
    print('===============================================')


def main():
    option = ''
    while option != '5':
        display_menu()
        option = input('Chọn chức năng (1-5): ')
        print()
        
        match option:
            case '1': 
                deposit_ui()
            case '2': 
                transfer_ui()
            case '3': 
                check_history()
            case '4': 
                view_balance()
            case '5':
                print('Cảm ơn bạn đã sử dụng dịch vụ\n')
                logging.info('System shutdown')
            case _:
                print('Lựa chọn không hợp lệ, vui lòng nhập lựa chọn từ 1-5!')


if __name__ == '__main__':
    main()
