import hashlib
import huepy
import argparse
import threading
import sys
import time
import pyfiglet

GREEN = "\033[92m"
RESET = "\033[0m"
found = False

def print_banner():
    banner = pyfiglet.figlet_format("Crack Mate")
    print(f"{GREEN}{banner}{RESET}")
    print(f"{GREEN}Developed by Ayush Kumar{RESET}")
    print(f"{GREEN}GitHub: https://github.com/0xHawkEye{RESET}")
    print(f"{GREEN}Linkedin: https://www.linkedin.com/in/ayushkr4422{RESET}")
    print()
    print()

def crack(hash_value, hash_type, wordlist_path):
    global found
    try:
        with open(wordlist_path, "r", errors="ignore") as f:
            for word in f:
                word = word.strip()
                hash_object = hashlib.new(hash_type)
                hash_object.update(word.encode())
                if hash_object.hexdigest() == hash_value:
                    print('\n', end="")
                    print(huepy.good(huepy.red("Hash cracked: ")), hash_value)
                    print(huepy.good(huepy.green("Password found: ")), word)
                    found = True
                    break
    except KeyboardInterrupt:
        print("\nCtrl+C detected, exiting...")
        sys.exit()
    except UnicodeDecodeError:
        print(f"Error decoding word: {word}")

if __name__ == "__main__":
    print_banner()
    parser = argparse.ArgumentParser(description='Hash Cracker')
    parser.add_argument('-hs', '--hash', type=str, help='Hash value to crack')
    parser.add_argument('-a', '--algorithm', type=str, help='Hash algorithm (e.g., md5, sha1)')
    parser.add_argument('-w', '--wordlist', type=str, help='Path to the wordlist file', default='rockyou1.txt')
    parser.add_argument('-all', action='store_true', help='Print all available hash algorithms')
    args = parser.parse_args()

    if args.all:
        print(huepy.good("Supported hash algorithms:"))
        for algorithm in hashlib.algorithms_available:
            print(algorithm, end=" ")
        print('\n')
        exit()

    if not args.hash or not args.algorithm:
        print("Error: Both hash value and algorithm must be specified.")
        exit(1)

    hash_value = args.hash
    hash_type = args.algorithm
    wordlist_path = args.wordlist

    start_time = time.time()
    print(huepy.good('Starting the cracking process'))
    time.sleep(1)
    print(huepy.good('Fetching all the passwords from wordlist'))

    crack_thread = threading.Thread(target=crack, args=(hash_value, hash_type, wordlist_path))
    crack_thread.start()
    crack_thread.join()

    if not found:
        print(huepy.bad("❌ Password not found in the wordlist."))

    end_time = time.time()
    ex_time = end_time - start_time
    print(huepy.good(f'Total time taken: {ex_time:.2f}s'), "\n")
