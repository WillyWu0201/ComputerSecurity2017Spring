
import fss_util
import binary
from Crypto.Cipher import AES

#func (f Fss) GenerateTreePF(a, b uint) []FssKeyEq2P {
def GenerateTreePF(f, a, b):
    a=0
    b=0




#func (f Fss) EvaluatePF(serverNum byte, k FssKeyEq2P, x uint) int {

def evaluatepf(f, serverNum , k , x ) :


    print("serverNum :", serverNum)
    print("k:", k)
    print("x:", x)

    #
    sCurr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sCurr = k.SInit
    tCurr = k.TInit

    for i in range(f.NumBits):
        fss_util.prf(sCurr, f.FixedBlocks, 3, f.Temp, f.Out)

        #Keep counter to ensure we are accessing CW correctly
        count = 0
        for j in range(AES.block_size*2+2):
            #Make sure we are doing G(s) ^ (t*sCW||tLCW||sCW||tRCW)
            if j == AES.block_size + 1 :
                count = 0
            elif j == AES.block_size * 2+1 :
                count = AES.block_size + 1

            f.Out[j] = f.Out[j] ^ (tCurr * k.CW[i][count])
            count = count + 1

        xBit = fss_util.getBit(x, (f.N - f.NumBits + i + 1), f.N)

        #Pick right seed expansion based on
        if xBit == 0 :
            sCurr = f.Out[AES.block_size]
            tCurr = f.Out[AES.block_size] % 2

        else :
            sCurr = f.Out[(AES.block_size+1):(AES.block_size*2+1)]
            tCurr = f.Out[AES.block_size*2+1] % 2

    sFinal, _ = binary.Varint(sCurr[:8])

    if serverNum == 0 :

        return int(sFinal) + int(tCurr) * k.FinalCW
    else :
        return -1 * (int(sFinal) + int(tCurr) * k.FinalCW)


