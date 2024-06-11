# This code is used to check if the signals in the file are within the range of 10 to 30,
# or no difference between the signals. 
# If the signals are within the range, the code prints 'successed'.
def check_signals(filename: str):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            numbers = list(map(float, content.split()))

            i = 1
            while i < len(numbers) - 1:
                # Skip if the number or the next number is 1000
                if abs(numbers[i]) == 1000:
                    i += 2
                    continue
                
                diff = abs(numbers[i] - numbers[i -1])
                if not (5 <= diff <= 7 or diff == 0):
                    print('failed')
                    return
                
                i += 1

            print('successed')
    except FileNotFoundError:
        print(f'File {filename} not found')
    except ValueError:
        print('File contains non-numeric data')

if __name__ == '__main__':
    check_signals('signals.txt')
