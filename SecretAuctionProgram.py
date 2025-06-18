print(""""

                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
""")

secret_bid = {}
def simpan(nama, bid):
    secret_bid[nama]= bid

def caripemenang(bid_dict):
    pemenang = ""
    bid_tertinggi = 0

    for nama, bid in secret_bid.items():
        if bid > bid_tertinggi:
            bid_tertinggi = bid
            pemenang = nama

    print(f"Pemenang Lelangnya adalah {pemenang} dengan nilai {bid_tertinggi}")

should_continue = True
while should_continue:
    nama = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    simpan(nama, bid)
    lanjut = input("Are there any other bidders? Type 'yes or 'no'.").lower()

    if lanjut == "no":
        should_continue = False
    elif lanjut == "yes":
        should_continue = True
        print("\n" * 100)
    else:
        print("Yang bener lah, no atau yes kocak")
        continue

caripemenang(secret_bid)

    
    
