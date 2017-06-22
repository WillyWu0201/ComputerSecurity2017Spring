
import fss_initialize
import fss_2party_pf

#Generate fss Keys on client
#fClient's format = type Fss struct { @fss_util
fClient = fss_initialize.ClientInitialize(6)


#Test with if x = 5, evaluate to 1

fssKeys = fss_2party_pf.generatetreepf(fClient,5, 1)

#Simulate server

fServer = fss_initialize.ServerInitialize(fClient.PrfKeys, fClient.NumBits)

#Test 2-party Equality Function
ans0 = 0
ans1 = 0

ans0 = fss_2party_pf.evaluatepf(fServer,0, fssKeys[0], 5)
ans1 = fss_2party_pf.evaluatepf(fServer,1, fssKeys[1], 5)


print("===============")
print("ans0:", ans0)
print("ans1:", ans1)
print("Match (should be non-zero):", ans0+ans1)

ans0 = fss_2party_pf.evaluatepf(fServer,0, fssKeys[0], 11)
ans1 = fss_2party_pf.evaluatepf(fServer,1, fssKeys[1], 11)
print("===============")
print("ans0:", ans0)
print("ans1:", ans1)
print("No Match (should be 0):", ans0+ans1)
