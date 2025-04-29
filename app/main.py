import sys

def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()  # <<< flush forces the $ prompt to show immediately
    input()

if __name__ == "__main__":
    main()
