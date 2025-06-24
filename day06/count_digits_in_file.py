from pathlib import Path


def report_txt():
    # Read numbers from file and convert to integers
    numbers = [int(x) for x in Path(r'C:\Users\aaronf\python\numbers.txt').read_text().split()]

    # Digits from 0 to 9
    strange = list(range(10))

    # Initialize digit counts
    amount = [0 for _ in range(10)]

    # Count digit frequencies
    for num in numbers:
        for digit_char in str(num):
            digit_int = int(digit_char)
            if 0 <= digit_int < 10:
                amount[digit_int] += 1

    # Prepare output
    output_lines = [f"{digit} {count}" for digit, count in zip(strange, amount)]

    # Save to report.txt
    Path(r'C:\Users\aaronf\python\report.txt').write_text("\n".join(output_lines))

    for lines in output_lines:
        print(f"{lines}")
# Call the function
report_txt()


