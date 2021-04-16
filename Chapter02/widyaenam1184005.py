from threading import Barrier, Thread
import os
import requests
from time import ctime, sleep

count = 1
barrier = Barrier(count)
file = "tipe_cuaca_harian_"
filename = os.path.join(os.path.dirname(__file__), file)

def apirandom():  

    apipangkat = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    headers = {
    'accept': "application/json",
    'x-rapidapi-key': "8888b67700msh488af957b858844p1af3aejsn43f5d508931b",
    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }

    response = requests.request("GET", apipangkat, headers=headers)

    buatfile(response.text)
def buatfile(tipecuaca):
       for a in range(3):
           print('buat file : '+file+str(a)+'.txt \n')
           f = open(filename+str(a)+".txt", "w")
           f.write(str(tipecuaca))
           print('baca file: '+file+str(a)+'.txt')
           r = open(filename+str(a)+".txt", "r")
           if r.mode == "r":
               contents = r.read()
               print(contents)
           r.close()
           print('Pada Akhirnya Membuat dan Membaca File rekapan tipe cuaca harian '+file+str(a)+' reached the barrier at: %s \n' % (ctime()))
           sleep(4)
           barrier.wait()
def eksekusi():
    apirandom()
    sleep(4)
    barrier.wait()
    print('All reached the barrier at: %s \n' % (ctime()))
def main():
    threads = []
    print('Cek Tipe Cuaca Harian Sekarang')
    for a in range(count):
        threads.append(Thread(target=eksekusi))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Data Tipe Cuaca telah direkap')
    return True

if __name__ == "__main__":
 main() fg