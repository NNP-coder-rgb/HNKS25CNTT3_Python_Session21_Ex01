import logging

balance = 5000000

logging.basicConfig(
    level = logging.INFO,
    filename = 'momo_transactions.log',
    format = "%(asctime)s - [%(levelname)s] - %(message)s"
)

def deposit():
    """
    Xử lý chức năng nạp tiền vào ví MoMo.
    
    Hàm sẽ yêu cầu người dùng nhập số tiền từ bàn phím. Nếu số tiền hợp lệ 
    (là số nguyên dương), hệ thống sẽ cập nhật số dư, ghi log thành công và thoát.
    Nếu nhập sai định dạng hoặc số tiền âm, hệ thống sẽ báo lỗi và yêu cầu nhập lại.
    """
    while True:
        try:
            input_money = int(input('Nhập số tiền cần nạp: '))
            if input_money < 0:
                print('Lỗi: Số tiền giao dịch phải lớn hơn 0.')
                logging.error(f'InvalidAmountError: Attempted to process {input_money} VND.')
            else:
                global balance
                balance += input_money
                print(f'Nạp tiền thành công: +{input_money:,} VND')
                print(f'Số dư hiện tại: {balance:,} VND')
                logging.info(f'Deposit successful: +{input_money} VND. Current Balance: {balance} VND')
                break
        except ValueError:
            print('Lỗi: Vui lòng nhập số tiền hợp lệ.')
            logging.error('ValueError: Invalid numeric input for deposit.')
            continue

def transfer():
    """
    Xử lý chức năng chuyển tiền đến số điện thoại khác.
    
    Hàm kiểm tra tính hợp lệ của số điện thoại (phải đủ 10 ký tự) và số tiền chuyển 
    (phải lớn hơn 0 và nhỏ hơn hoặc bằng số dư hiện tại). 
    Nếu giao dịch lớn hơn hoặc bằng 10,000,000 VND, một cảnh báo (WARNING) sẽ được ghi lại.
    """
    while True:
        try:
            global balance
            input_phone_number = input('Nhập số điện thoại người nhận: ')
            if len(input_phone_number) != 10:
                print('Số điện thoại phải chuẩn định dạng là 10 chữ số')
            else:
                input_money = int(input('Nhập số tiền cần chuyển: '))
                if input_money < 0:
                    print('Lỗi: Số tiền giao dịch phải lớn hơn 0.')
                    logging.error(f'InvalidAmountError: Attempted to process {input_money} VND.')
                elif input_money > balance:
                    print('Giao dịch thất bại: Số dư của bạn không đủ.')
                    print(f'Số dư hiện tại: {balance}')
                    logging.error(f'InsufficientBalanceError: Attempted to transfer {input_money} VND with balance {balance} VND.')
                else:
                    balance -= input_money
                    print(f'\nChuyển tiền thành công tới số điện thoại {input_phone_number}')
                    print(f'Số tiền đã chuyển: {input_money:,} VND')
                    print(f'Số dư còn lại: {balance:,} VND')
                    if input_money >= 10000000:
                        logging.warning(f'High value transaction detected: {input_money} VND to {input_phone_number}')
                    logging.info(f'Transfer successful: -{input_money:,} VND to {input_phone_number}. Current Balance: {balance:,} VND')
                    break
        except ValueError:
            print('Lỗi: Vui lòng nhập số tiền hợp lệ.')
            logging.error('ValueError: Invalid numeric input for Transfer.')
            continue

def check_history():
    """
    Đọc và hiển thị lịch sử giao dịch.
    
    Hàm mở file log 'momo_transactions.log' để đọc và in ra màn hình 
    5 dòng nhật ký giao dịch mới nhất. Nếu file chưa được tạo, hàm sẽ đưa ra thông báo phù hợp.
    """
    print('--- 5 LỊCH SỬ GIAO DỊCH MỚI NHẤT ---')
    try:
        with open('momo_transactions.log', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                print('Lịch sử hệ thống đang trống.')
            else:
                latest_logs = lines[-5:]
                for line in latest_logs:
                    print(line.strip())
    except FileNotFoundError:
        print('Hiện tại chưa có lịch sử giao dịch nào được ghi nhận.')
    except Exception as e:
        print(f'Lỗi khi đọc file lịch sử: {e}')

def view_balance():
    """
    Hiển thị số dư hiện tại của ví MoMo.
    
    Đồng thời ghi nhận một log INFO về việc người dùng kiểm tra số dư.
    """
    global balance
    print('--- SỐ DƯ VÍ MOMO ---')
    print(f'Số dư hiện tại: {balance:,} VND')
    logging.info(f'Balance checked. Current Balance: {balance:,} VND')

def display_menu():
    """
    Hiển thị danh sách các chức năng (Menu) của ứng dụng giả lập Ví MoMo.
    """
    print()
    print('========== VÍ MOMO GIẢ LẬP ==========')
    print('1. Nạp tiền vào ví')
    print('2. Chuyển tiền')
    print('3. Xem lịch sử hệ thống')
    print('4. Xem số dư tài khoản')
    print('5. Thoát chương trình')
    print('===============================================')

def main():
    """
    Hàm khởi chạy chính của chương trình.
    
    Điều hướng người dùng đến các chức năng tương ứng dựa trên lựa chọn từ 1 đến 5.
    Vòng lặp sẽ liên tục chạy cho đến khi người dùng chọn '5' để thoát.
    """
    option = ''
    while option != '5':
        display_menu()

        option = input('Chọn chức năng (1-5): ')

        match option:
            case '1':
                print()
                deposit()
                print()
            case '2':
                print()
                transfer()
                print()
            case '3':
                print()
                check_history()
                print()
            case '4':
                print()
                view_balance()
                print()
            case '5':
                print('\nCảm ơn bạn đã sử dụng dịch vụ\n')
                logging.info('System shutdown')
            case _:
                print('Lựa chọn không hợp lệ, vui lòng nhập lựa chọn từ 1-5!')

if __name__ == '__main__':
    main()
