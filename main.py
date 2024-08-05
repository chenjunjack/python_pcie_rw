# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



from device import  Device

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Bind to PCI device at "0000:04:00.0"
    d = Device("0000:08:00.0")
    # Access BAR 0
    bar = d.bar[0]
    offset =0x0
    # write int data to BAR , offset 0x1004
    bar.write(offset, 0x12345678)
    for i in range(100):
        # bar.write(offset+(4*i), i)
        # print(i,"addr" ,hex(offset+(4*i))," write ",hex(i))

    # read BAR , offset 0x1004
        ret = bar.read(offset+(4*i))
        print(i,"addr",hex(offset+(4*i))," read ",hex(ret))
        print("---------")
# 
