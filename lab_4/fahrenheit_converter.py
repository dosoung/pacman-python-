def input_celsius_value():
    result_1 = float(input("변환하고 싶은 섭씨 온도를 입력해 주세요: "))

    return result_1

def convert_celsius_fahrenheit(result_1):
    result_2 = ((9/5) * result_1) + 32

    return result_2

def print_fahrenheit_value(result_1, result_2):
    print("섭씨온도 :",result_1)
    print("화씨온도 :",result_2)

    return None

def main():
    print("본 프로그램은 섭씨를 화씨로로 변환해주는 프로그램입니다")
    print("============================")
    # ===Modify codes below=================

    # ======================================
    print("===========================")
    print("프로그램이 종료 되었습니다.")


if __name__ == '__main__':

    celsius_value = input_celsius_value()
    celsius_fahrenheit = convert_celsius_fahrenheit(celsius_value)
    print_fahrenheit_value(celsius_value, celsius_fahrenheit)
    main()
