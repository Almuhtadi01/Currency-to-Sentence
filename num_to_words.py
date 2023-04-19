def satuan(bil):
    bilangan = ["", "satu ", "dua ", "tiga ", "empat ", "lima ", "enam ", "tujuh ", "delapan ", "sembilan "]
    return bilangan[bil]

def puluhan(bil, satuan):
    bilangan = ["", "satu ", "dua ", "tiga ", "empat ", "lima ", "enam ", "tujuh ", "delapan ", "sembilan "]
    if (bil == 1):
        if (satuan == 0):
            return "sepuluh "
        elif (satuan == 1):
            return "sebelas "
        else:
            return bilangan[satuan] + "belas "
    return bilangan[bil] + "puluh " + bilangan[satuan]

def ratusan(bil):
    bilangan = ["", "se", "dua ", "tiga ", "empat ", "lima ", "enam ", "tujuh ", "delapan ", "sembilan "]
    return bilangan[bil] + "ratus "

def ribuan(bil):
    bilangan = ["", "se", "dua ", "tiga ", "empat ", "lima ", "enam ", "tujuh ", "delapan ", "sembilan "]
    return bilangan[bil] + "ribu "

def puluhanribu(bil, satuan):
    bilangan = ["", "satu ", "dua ", "tiga ", "empat ", "lima ", "enam ", "tujuh ", "delapan ", "sembilan "]
    if (bil == 1):
        if (satuan == 0):
            return "sepuluh ribu "
        elif (satuan == 1):
            return "sebelas ribu "
        else:
            return bilangan[satuan] + "belas ribu "
    return bilangan[bil] + "puluh " + bilangan[satuan] + "ribu "

def ratusanribu(bil, puluhan, satuan):
    val=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    bilangan = ["", "se", "dua ", "tiga ", "empat ", "lima ", "enam ", "tujuh ", "delapan ", "sembilan "]
    if (bil == val[bil]):
       if (puluhan == 0):
          if (satuan == 0):
             return bilangan[bil] + "ratus ribu "
          elif (satuan==1):
             return bilangan[bil] + "ratus satu ribu "
          else:
             return bilangan[bil] + "ratus " + bilangan[satuan] + "ribu "
       elif (puluhan == 1):
          if (satuan == 0):
             return bilangan[bil] + "ratus sepuluh ribu "
          elif (satuan == 1):
             return bilangan[bil] + "ratus sebelas ribu "
          else:
             return bilangan[bil] + "ratus " + bilangan[satuan] + "belas ribu "
       else:
           if (satuan==1):
              return bilangan[bil] + "ratus " + bilangan[puluhan] + "puluh satu ribu "
           else:
              return bilangan[bil] + "ratus " + bilangan[puluhan] + "puluh " + bilangan[satuan] + "ribu "
           
def juta(bil):
    bilangan = ["", "satu ", "dua ", "tiga ", "empat ", "lima ", "enam ", "tujuh ", "delapan ", "sembilan "]
    return bilangan[bil] + "juta "

def puluhanjuta(bil, satuan):
    bilangan = ["", "satu ", "dua ", "tiga ", "empat ", "lima ", "enam ", "tujuh ", "delapan ", "sembilan "]
    if (bil == 1):
        if (satuan == 0):
            return "sepuluh juta "
        elif (satuan == 1):
            return "sebelas juta "
        else:
            return bilangan[satuan] + "belas juta "
    else:
        if (satuan == 0):
            return bilangan[bil] + "puluh juta "
        else:
            return bilangan[bil] + "puluh " + bilangan[satuan] + "juta "

def ratusanjuta(bil, puluhan, ratusan):
    bilangan = ["", "se", "dua ", "tiga ", "empat ", "lima ", "enam ", "tujuh ", "delapan ", "sembilan "]
    if (bil>=1):
        return bilangan[bil] + "ratus juta "
    return bilangan[bil] + "ratus "

stop = 1                                                #digunakan untuk identifikasi selesai
while (stop != 0):
    sebutan = ""                                        #tempat menyimpan hasil sebutan bilangan
    bil = input("masukkan angka (0 untuk keluar) : ")
    if (bil.isnumeric()):      
        stop = bil = int(bil);                          #input always on string, so change to integer!!!
		
        try:
	        if (bil > 99999999):				#check ratusan juta
	            sebutan += ratusanjuta(int(bil/100000000), int(bil/10000000)%10, int(bil/1000000))
	            bil = bil%100000000
	
	        if (bil > 9999999):                             #check puluhan juta
	            sebutan += puluhanjuta(int(bil/10000000), int(bil/1000000)%10)
	            bil = bil%1000000
	   
	        elif (bil > 999999):				#check juta
	            sebutan += juta(int(bil/1000000))
	            bil = bil%1000000
	        
	        if (bil > 99999):				#check ratus ribu
	            sebutan += ratusanribu(int(bil/100000), int(bil/10000)%10, int(bil/1000)%10)
	            bil = bil%1000
	
	        if (bil > 9999):                                #check puluhan ribu
	            sebutan += puluhanribu(int(bil/10000), int(bil/1000)%10)
	            bil = bil%1000
	
	        elif (bil > 999):                               #check ribuan
	            sebutan += ribuan(int(bil/1000))
	            bil = bil%1000
	    
	        if (bil > 99):                                  #check ratusan
	            sebutan += ratusan(int(bil/100))
	            bil = bil%100
	    
	        if (bil > 9):                                   #check puluhan
	            sebutan += puluhan(int(bil/10), bil%10)
	            bil = bil%10
	
	        else:                                           #check satuan
	            sebutan += satuan(bil)
	
	        if (stop == 0):                                 #sebelum keluar, tulis "NOL" dulu
	            sebutan = "nol"
	            
	        print("sebutannya:", sebutan )
	        print()
			
        except IndexError:
               print("Bilangan terlalu banyak, coba kurangi")
               pass
    else:
        print("ERROR: HANYA BILANGAN INTEGER!!!")

