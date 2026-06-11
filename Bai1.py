import logging

balance = 5000000

logging.basicConfig(
    level = logging.INFO,
    filename = 'momo_transactions.log',
    format = "%(asctime)s - [%(levelname)s] - %(message)s"
)

def deposit():
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
        except:
            print('Lỗi: Vui lòng nhập số tiền hợp lệ.')
            logging.error('ValueError: Invalid numeric input for deposit.')
            continue

def transfer():
    while True:
        try:
            global balance
            input_phone_number = input('Nhập số điện thoại người nhận: ')
            if len(input_phone_number) > 10 or len(input_phone_number) < 10:
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
        except:
            print('Lỗi: Vui lòng nhập số tiền hợp lệ.')
            logging.error('ValueError: Invalid numeric input for Transfer.')
            continue

def check_history():
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
    global balance
    print('--- SỐ DƯ VI MOMO ---')
    print(f'Số dư hiện tại: {balance:,} VMD')
    logging.info(f'Balance checked. Current Balance: {balance:,} VND')

def display_menu():
    print()
    print('========== VÍ MOMO GIẢ LẬP ==========')
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

main()
