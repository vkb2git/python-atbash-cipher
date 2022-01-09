import threading
from queue import Queue

def atbash_encrypt(char):

    if char.isalpha():
        N = ord('z') + ord('a')
        if char.isupper():
            N = ord('Z') + ord('A')
        
        ans = chr(N - ord(char))
        # print('ans=',ans)
        return ans

    return char

def encrypt_line(line, enc_que):

    if line:
        enc_line = ''.join([atbash_encrypt(c) for c in line])

        enc_que.put(enc_line)



def read_file():
    threads = []

    normal_file = 'hello-world.txt'
    enc_filename = 'enc_file.txt'

    enc_que = Queue()

    with open(normal_file) as f:
        
        print(f)

        lines = f.readlines()

        if lines and len(lines) > 0:
            for line in lines:
                print(line)

                if line:

                    t = threading.Thread(target=encrypt_line, args=(line, enc_que))
                    t.start()
                    threads.append(t)

    for t in threads:
        t.join()

    enc_lines_list = []

    while not enc_que.empty():
        result = enc_que.get()
        enc_lines_list.append(result)

    enc_lines = ''.join(enc_lines_list)

    # print('enc_lines=', enc_lines)

    if enc_lines and len(enc_lines) > 0:

        enc_file = open(enc_filename, "w")
        enc_file.write(enc_lines) 
        enc_file.close()


read_file()