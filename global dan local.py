#scope variabel global dan local
namakucing='doraemon'
makanankucing='pindang'
def rubahnama(namabaru):
    global namakucing
    namakucing=namabaru
    print('saya rubah nama kucing menjadi',namakucing)
def kasihmakankucing(makanan):
    global makanankucing
    makanankucing=makanan
    print('kucing saya yang bernama',namakucing,'makan dengan',makanankucing)

rubahnama('meong')
print('nama kucing menjadi',namakucing)
kasihmakankucing('kerupuk')
print('makanan kucing saya menjadi',makanankucing)