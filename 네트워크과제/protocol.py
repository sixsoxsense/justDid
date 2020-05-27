'''
ethernet format
destinationAddress, sourceAddress, Type, Data

일단
입력값 2개(1바이트)씩 나눠서 6바이트 6바이트 로 도착지,출발지
나누고 그다음 2바이트로 뭔지 판단 하게해서
이더넷 타입까지 출력시키고
ip, tcp,udp면 그리 출력하고
arp면 arp 출력하게 한뒤
각 ip, tcp arp 함수별로 내부에 타입들이 뭔뜻하게하는지 뽑아내면 되나...?
2개당 1바이트
'''
String = ""


def ETHERNET(String):
    destiAddress = String[:12]
    sourceAddress = String[12:24]
    ethernetType = String[24:28]
    print("ETHERNET:")
    print(destiAddress, sourceAddress, ethernetType)
    return ethernetType


def strToIP(String):  # dc 5f e9 ab ==220.95.233.171
    bytes = ["".join(x) for x in zip(*[iter(String)] * 2)]
    bytes = [int(x, 16) for x in bytes]
    IP = ".".join(str(x) for x in bytes)
    return IP


def strToMAC(String):
    bytes = ["".join(x) for x in zip(*[iter(String)] * 2)]
    MAC = ":".join(str(x) for x in bytes)
    return MAC


def IP(String):
    VER = String[0]
    HLEN = String[1]
    serviceType = String[2:4]
    TotalLength = String[4:8]
    Identy = String[8:12]
    flag = String[12]
    offset = String[13:16]
    TTL = String[16:18]
    Protocol = String[18:20]
    checksum = String[20:24]
    sourceAddress = strToIP(String[24:32])
    destiAddress = strToIP(String[32:40])
    print("IP:")
    print(VER, HLEN, serviceType, TotalLength, Identy, flag, offset, TTL, Protocol, checksum, sourceAddress,
          destiAddress)
    return Protocol


def TCP(String):
    sourcePort = String[:4]
    destiPort = String[4:8]
    sequenceN = String[8:16]
    ackN = String[16:24]
    headerLength = String[24:26]
    controlBits = String[26:28]
    windowSize = String[28:32]
    checksum = String[32:36]
    urgentPoint = String[36:40]
    option = String[40:]
    print("TCP:")
    print(sourcePort, destiPort, sequenceN, ackN, headerLength, controlBits, windowSize, checksum, urgentPoint, option)


def UDP(String):
    sourcePort = int(String[:4], 16)
    destiPort = int(String[4:8], 16)
    totalLength = int(String[8:12], 16)
    checksum = String[12:16]
    print("UDP:")
    print(sourcePort, destiPort, totalLength, checksum)


def ICMP(String):
    Type = String[:2]
    Code = String[2:4]
    checksum = String[4:8]
    id = String[8:12]
    sequence = String[12:16]
    data = String[16:]
    print("ICMP:")
    print(Type, Code, checksum, id, sequence, data)


def ARP(String):
    HWType = String[0:4]
    protocolType = String[4:8]
    HWSize = String[8:10]
    protocolSize = String[10:12]
    operation = String[12:16]
    sendMacAddress = strToMAC(String[16:28])
    sendIPAddress = strToIP(String[28:36])
    targetMacAddress = strToMAC(String[36:48])
    targetIPAddress = strToIP(String[48:56])
    print("ARP:")
    print(HWType, protocolType, HWSize, protocolSize, operation, sendMacAddress, sendIPAddress, targetMacAddress,
          targetIPAddress)


def cutFrame(String):
    eType = ETHERNET(String[:28])
    if eType == "0800":
        '''
        ip인경우 
        '''
        protocol = IP(String[28:])
        if protocol == "06":
            TCP(String[68:])
        elif protocol == "01":
            ICMP(String[68:])
        elif protocol == "11":
            UDP(String[68:])
        else:
            print("IP인경우 오류")
    elif eType == "0806":
        '''
        arp인경우
        '''
        ARP(String[28:])
    else:
        print("입력프레임오류")


if __name__ == '__main__':
    String = str(input("프레임을입력하시오\n"))
    print(cutFrame(String))
