import fisika
def main():
    #membuat judul program
    print("program mencari BERAT BENDA")
    #memninta user memasukkan bilangan
    w=float(input("Masukkan w: "))
    g=float(input("Masukkan g: "))

    massa = fisika.massaBenda(w, g)
    
    #menampilkan hasil
    print("MASSA BENDA")
    print("berat benda\t:", w)
    print("percepatan gravitasi\t:", g)
    print("hasil massa\t=", massa)
if __name__=="__main__":
    main()
