def oracle_1024(circuit, quantum_reg, int_list):
    n = 1024
    ql = 9
    miss_int = bin(int(n*(n+1)/2) - sum(int_list) - 1)[2:].rjust(10, '0')
    
    for i in range(ql, -1, -1):
        #print(miss_int[i], i)
        if miss_int[i]=='0':
            circuit.x(quantum_reg[ql-i])
    
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    
    circuit.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    circuit.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    
    circuit.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    circuit.ccx(quantum_reg[14],quantum_reg[17],quantum_reg[10])
    circuit.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    
    circuit.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    circuit.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    
    circuit.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    circuit.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])
    
    for i in range(ql, -1, -1):
        if miss_int[i]=='0':
            circuit.x(quantum_reg[ql-1-i])


def inversion_1024(circuit, quantum_reg):
    
    for i in range(10):
        circuit.h(quantum_reg[i])
        circuit.x(quantum_reg[i])

    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    
    circuit.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    circuit.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    
    circuit.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    circuit.ccx(quantum_reg[14],quantum_reg[17],quantum_reg[10])
    circuit.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    
    circuit.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    circuit.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    
    circuit.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    circuit.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])

    for i in range(10):
        circuit.x(quantum_reg[i])
        circuit.h(quantum_reg[i])
    
    circuit.x(quantum_reg[10])

    
def inversion_8(circuit,quantum_reg):
    
    for i in range(3):
        circuit.h(quantum_reg[i])
        circuit.x(quantum_reg[i])
        
    circuit.ccx(quantum_reg[2],quantum_reg[1],quantum_reg[4])
    circuit.ccx(quantum_reg[4],quantum_reg[0],quantum_reg[3])
    circuit.ccx(quantum_reg[2],quantum_reg[1],quantum_reg[4])
    circuit.x(quantum_reg[3])
    
    for i in range(3):
        circuit.x(quantum_reg[i])
        circuit.h(quantum_reg[i])

def oracle_8(circuit, qreg, int_list):
    n = 8
    miss_int = bin(int(n*(n+1)/2) - sum(int_list) - 1)[2:].rjust(3, '0')
    #print(miss_int)
    
    for i in range(2, -1, -1):
        if miss_int[i]=='0':
            circuit.x(qreg[2-i])
            
    circuit.ccx(qreg[2],qreg[1],qreg[4])
    circuit.ccx(qreg[4],qreg[0],qreg[3])
    circuit.ccx(qreg[2],qreg[1],qreg[4])
            
    for i in range(2, -1, -1):
        if miss_int[i]=='0':
            circuit.x(qreg[2-i])
            
def inversion4(circuit, quantum_reg):
    
    for i in range(2):
        circuit.h(quantum_reg[i])
        circuit.x(quantum_reg[i])
        
    circuit.ccx(quantum_reg[0],quantum_reg[1], quantum_reg[2])
    circuit.x(quantum_reg[2])
    
    for i in range(2):
        circuit.x(quantum_reg[i])
        circuit.h(quantum_reg[i])