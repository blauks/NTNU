from sympy import *
import gmpy2

n1 = int("51EFBD357CCB0810E114F651E3E8355BDFE25BD9EF6C6859E7493169801B3257DDADD8571BC7DC7F729A0E37AA414F6A8390084C36B97EDC478E4236AB3E83B79714E545516D82E2B62A4A98700003B35A392611B8C67858D75C00AB7B67529344CA2E3A060C1C1F814371E53B8D3560D716BF5375D04EE4D9EB95F017481C23AF65C12D6CCBE76CAF04990FF03056B671802488BE598B54FE688558B6ED76098A941DD9B24F6302DE224638142140F120742032495F9E5002AB484D75A1969D588C29B7A96F458F2C5784BF3E8946BE299B75EA74E2E6EDCDCE10C896F9531E77DF75B0C4D72CEA9D8572AB6E2E43AB7F76E760CFC87E358A8C02E784E32AD7", 16)
n2 = int("51EFBD357CCB0810E114F651E3E8355BDFE25BD9EF6C6859E7493169801B3257DDADD8571BC7DC7F729A0E37AA414F6A8390084C36B97EDC478E4236AB3E83B79714E545516D82E2B62A4A98700003B35A392611B8C67858D75C00AB7B67529344CA2E3A060C1C1F814371E53B8D3560D716BF5375D04EE4D9EB95F017481B335C68E5213795E7433FE052BBF3189214D3E57FCACCFB833DD8C5306DCFEB00EF1EB5722E7241DCE87F54DD15A98EAC436B510E5B2922FA1D4A75942EA18CA166E20222CD193AFF95E231EF8F1F334DE980CFF5FF75F319C04020C41ED547D1367AA057C153E578F416C78414AC08EC73FBC27D72411416C140C6A9D16F356C49", 16)
n3 = int("51EFBD357CCB0810E114F651E3E8355BDFE25BD9EF6C6859E7493169801B3257DDADD8571BC7DC7F729A0E37AA414F6A8390084C36B97EDC478E4236AB3E83B79714E545516D82E2B62A4A98700003B35A392611B8C67858D75C00AB7B67529344CA2E3A060C1C1F814371E53B8D3560D716BF5375D04EE4D9EB95F01748128A968894501763B76D7C8992692A5B36D28775BAB41BB4C2AEA605EAF8025640EEC854E79AC9C7ACAEF163BFBD3266E0A8984461A534ACA9E703042266524CC059A8BC93BE754CADEA78E502F8783E3EDD2813A12E822784C02D1DD743C74C6B55CB50B7CDC35E00F3E7885594CDD0731A43C62BD7617889DDC890E603F763543B", 16)
n4 = int("51EFBD357CCB0810E114F651E3E8355BDFE25BD9EF6C6859E7493169801B3257DDADD8571BC7DC7F729A0E37AA414F6A8390084C36B97EDC478E4236AB3E83B79714E545516D82E2B62A4A98700003B35A392611B8C67858D75C00AB7B67529344CA2E3A060C1C1F814371E53B8D3560D716BF5375D04EE4D9EB95F017481C8FE56235BADBCB2EFB3D1B52C6BF78EFCF2AE1CADD343136C3E0965D9993476AA1D967997D6ACBF0FF9D1D7FE4493AE0E42644D949BFF8D895EF8DE091E2C2FEBDC0A1D468A7FEC3FCDD3A8667655C923E32480E540E22AA8BA3107C2BEE4B7CFE231C5F4488430C623F81447A56B28F6023CF2B87D52038E212764A2004AD1B8D", 16)

sqrtt = n4//2
p3,b = gmpy2.iroot(sqrtt, 2)
p3 = nextprime(int(p3))
print("P: " + str(p3))

while gcd(p3, n4) == 1:
    p3 = prevprime(p3)
    print("P: " + str(p3))
