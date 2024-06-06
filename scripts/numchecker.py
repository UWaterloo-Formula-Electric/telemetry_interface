# this code is used to check if the signals in the file are within the range of 10 to 30,
# or no difference between the signals. 
# If the signals are within the range, the code prints 'successed'.
def check_signals(filename: str):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            numbers = list(map(float, content.split()))

            for i in range(len(numbers) - 1):
                diff = abs(numbers[i] - numbers[i + 1])
                if not (10 <= diff <= 30 or diff == 0):
                    print('failed')
                    return

            print('successed')
    except FileNotFoundError:
        print(f'File {filename} not found')
    except ValueError:
        print('File contains non-numeric data')

if __name__ == '__main__':
    check_signals('signals.txt')
