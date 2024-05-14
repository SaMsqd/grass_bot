# Это мой файл, он будет создавать новые аккаунты в файл accounts.txt
import itertools


def main():
    i = 0
    with open('accounts.txt', 'w') as f:
        for email in itertools.permutations('abcdefghijk'):
            if i == 10:
                f.close()
            f.writelines(''.join(email) + '@gmail.com:' + 'toohardpasswordreally\n')


if __name__ == '__main__':
    main()
