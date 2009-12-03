
from pygr import worldbase

def main():
    """This function returns the argument.
    Example:
    >>> main()
    ['Bio.MSA.UCSC.bosTau2ToBostau3', 'Bio.MSA.UCSC.bosTau3ToBostau4', 'Bio.MSA.UCSC
.bosTau4_multiz5way', 'Bio.MSA.UCSC.bosTau4_pairwiseCanFam2', 'Bio.MSA.UCSC.bosT
au4_pairwiseHg18', 'Bio.MSA.UCSC.bosTau4_pairwiseMm9', 'Bio.MSA.UCSC.bosTau4_pai
rwiseOrnAna1', 'Bio.MSA.UCSC.braFlo1_multiz5way', 'Bio.MSA.UCSC.braFlo1_pairwise
GalGal3', 'Bio.MSA.UCSC.braFlo1_pairwiseHg18', 'Bio.MSA.UCSC.braFlo1_pairwiseMm9
', 'Bio.MSA.UCSC.braFlo1_pairwisePetMar1', 'Bio.MSA.UCSC.calJac1_multiz9way', 'B
io.MSA.UCSC.calJac1_pairwiseCanFam2', 'Bio.MSA.UCSC.calJac1_pairwiseHg18', 'Bio.
MSA.UCSC.calJac1_pairwiseHg19', 'Bio.MSA.UCSC.calJac1_pairwiseMm9', 'Bio.MSA.UCS
C.calJac1_pairwiseMonDom4', 'Bio.MSA.UCSC.calJac1_pairwiseOrnAna1', 'Bio.MSA.UCS
C.calJac1_pairwisePanTro2', 'Bio.MSA.UCSC.calJac1_pairwisePonAbe2', 'Bio.MSA.UCS
C.calJac1_pairwiseRheMac2', 'Bio.MSA.UCSC.canFam2_multiz4way', 'Bio.MSA.UCSC.can
Fam2_pairwiseBosTau4', 'Bio.MSA.UCSC.canFam2_pairwiseCalJac1', 'Bio.MSA.UCSC.can
Fam2_pairwiseEquCab1', 'Bio.MSA.UCSC.canFam2_pairwiseFelCat3', 'Bio.MSA.UCSC.can
Fam2_pairwiseHg17', 'Bio.MSA.UCSC.canFam2_pairwiseHg18', 'Bio.MSA.UCSC.canFam2_p
airwiseMm6', 'Bio.MSA.UCSC.canFam2_pairwiseMm7', 'Bio.MSA.UCSC.canFam2_pairwiseM
m8', 'Bio.MSA.UCSC.canFam2_pairwiseMm9', 'Bio.MSA.UCSC.canFam2_pairwiseRn3', 'Bi
o.MSA.UCSC.canFam2_pairwiseRn4', 'Bio.MSA.UCSC.cavPor3_pairwiseGalGal3', 'Bio.MS
A.UCSC.cavPor3_pairwiseHg18', 'Bio.MSA.UCSC.cavPor3_pairwiseMm9', 'Bio.MSA.UCSC.
cavPor3_pairwiseMonDom4', 'Bio.MSA.UCSC.cavPor3_pairwiseOryCun1', 'Bio.MSA.UCSC.
cavPor3_pairwiseRn4', 'Bio.MSA.UCSC.ce2ToCe4', 'Bio.MSA.UCSC.ce4_multiz5way', 'B
io.MSA.UCSC.ce6_multiz6way', 'Bio.MSA.UCSC.danRer2ToDanrer3', 'Bio.MSA.UCSC.danR
er3ToDanrer2', 'Bio.MSA.UCSC.danRer3ToDanrer4', 'Bio.MSA.UCSC.danRer3_multiz5way
', 'Bio.MSA.UCSC.danRer4ToDanrer3', 'Bio.MSA.UCSC.danRer4ToDanrer5', 'Bio.MSA.UC
SC.danRer4_multiz7way', 'Bio.MSA.UCSC.danRer4_pairwiseFr1', 'Bio.MSA.UCSC.danRer
4_pairwiseFr2', 'Bio.MSA.UCSC.danRer4_pairwiseGalGal3', 'Bio.MSA.UCSC.danRer4_pa
irwiseGasAcu1', 'Bio.MSA.UCSC.danRer4_pairwiseHg18', 'Bio.MSA.UCSC.danRer4_pairw
iseMm8', 'Bio.MSA.UCSC.danRer4_pairwiseMonDom4', 'Bio.MSA.UCSC.danRer4_pairwiseO
ryLat1', 'Bio.MSA.UCSC.danRer4_pairwiseRn4', 'Bio.MSA.UCSC.danRer4_pairwiseTetNi
g1', 'Bio.MSA.UCSC.danRer4_pairwiseXenTro2', 'Bio.MSA.UCSC.danRer5ToDanrer4', 'B
io.MSA.UCSC.danRer5_pairwiseFr2', 'Bio.MSA.UCSC.danRer5_pairwiseHg18', 'Bio.MSA.
UCSC.danRer5_pairwiseMm9', 'Bio.MSA.UCSC.danRer5_pairwiseOryLat1', 'Bio.MSA.UCSC
.danRer5_pairwiseOryLat2', 'Bio.MSA.UCSC.danRer5_pairwiseTetNig1', 'Bio.MSA.UCSC
.dm2ToDm3', 'Bio.MSA.UCSC.dm2_multiz15way', 'Bio.MSA.UCSC.dm2_multiz9way', 'Bio.
MSA.UCSC.dm3_multiz15way', 'Bio.MSA.UCSC.felCat3_multiz4way', 'Bio.MSA.UCSC.felC
at3_pairwiseCanFam2', 'Bio.MSA.UCSC.felCat3_pairwiseHg18', 'Bio.MSA.UCSC.felCat3
_pairwiseMm8', 'Bio.MSA.UCSC.fr2_multiz5way', 'Bio.MSA.UCSC.fr2_pairwiseDanRer4'
, 'Bio.MSA.UCSC.fr2_pairwiseDanRer5', 'Bio.MSA.UCSC.fr2_pairwiseGalGal3', 'Bio.M
SA.UCSC.fr2_pairwiseGasAcu1', 'Bio.MSA.UCSC.fr2_pairwiseHg18', 'Bio.MSA.UCSC.fr2
_pairwiseMm9', 'Bio.MSA.UCSC.fr2_pairwiseOryLat1', 'Bio.MSA.UCSC.fr2_pairwiseOry
Lat2', 'Bio.MSA.UCSC.fr2_pairwiseTetNig1', 'Bio.MSA.UCSC.galGal2ToGalgal3', 'Bio
.MSA.UCSC.galGal2_multiz7way', 'Bio.MSA.UCSC.galGal3_multiz7way', 'Bio.MSA.UCSC.
galGal3_pairwiseAnoCar1', 'Bio.MSA.UCSC.galGal3_pairwiseBraFlo1', 'Bio.MSA.UCSC.
galGal3_pairwiseCavPor3', 'Bio.MSA.UCSC.galGal3_pairwiseDanRer4', 'Bio.MSA.UCSC.
galGal3_pairwiseEquCab1', 'Bio.MSA.UCSC.galGal3_pairwiseFr2', 'Bio.MSA.UCSC.galG
al3_pairwiseGasAcu1', 'Bio.MSA.UCSC.galGal3_pairwiseHg18', 'Bio.MSA.UCSC.galGal3
_pairwiseMm8', 'Bio.MSA.UCSC.galGal3_pairwiseMm9', 'Bio.MSA.UCSC.galGal3_pairwis
eMonDom4', 'Bio.MSA.UCSC.galGal3_pairwiseOrnAna1', 'Bio.MSA.UCSC.galGal3_pairwis
ePetMar1', 'Bio.MSA.UCSC.galGal3_pairwisePonAbe2', 'Bio.MSA.UCSC.galGal3_pairwis
eRn4', 'Bio.MSA.UCSC.galGal3_pairwiseTaeGut1', 'Bio.MSA.UCSC.galGal3_pairwiseXen
Tro2', 'Bio.MSA.UCSC.gasAcu1_multiz8way', 'Bio.MSA.UCSC.gasAcu1_pairwiseAnoCar1'
, 'Bio.MSA.UCSC.gasAcu1_pairwiseDanRer4', 'Bio.MSA.UCSC.gasAcu1_pairwiseFr1', 'B
io.MSA.UCSC.gasAcu1_pairwiseFr2', 'Bio.MSA.UCSC.gasAcu1_pairwiseGalGal3', 'Bio.M
SA.UCSC.gasAcu1_pairwiseHg18', 'Bio.MSA.UCSC.gasAcu1_pairwiseMm8', 'Bio.MSA.UCSC
.gasAcu1_pairwiseMm9', 'Bio.MSA.UCSC.gasAcu1_pairwiseOryLat1', 'Bio.MSA.UCSC.gas
Acu1_pairwiseOryLat2', 'Bio.MSA.UCSC.gasAcu1_pairwiseTetNig1', 'Bio.MSA.UCSC.hg1
7ToHg18', 'Bio.MSA.UCSC.hg17_multiz17way', 'Bio.MSA.UCSC.hg18ToHg17', 'Bio.MSA.U
CSC.hg18_multiz17way', 'Bio.MSA.UCSC.hg18_multiz28way', 'Bio.MSA.UCSC.hg18_multi
z44way', 'Bio.MSA.UCSC.hg18_pairwiseAnoCar1', 'Bio.MSA.UCSC.hg18_pairwiseBosTau2
', 'Bio.MSA.UCSC.hg18_pairwiseBosTau3', 'Bio.MSA.UCSC.hg18_pairwiseBosTau4', 'Bi
o.MSA.UCSC.hg18_pairwiseBraFlo1', 'Bio.MSA.UCSC.hg18_pairwiseCalJac1', 'Bio.MSA.
UCSC.hg18_pairwiseCanFam2', 'Bio.MSA.UCSC.hg18_pairwiseCavPor3', 'Bio.MSA.UCSC.h
g18_pairwiseDanRer3', 'Bio.MSA.UCSC.hg18_pairwiseDanRer4', 'Bio.MSA.UCSC.hg18_pa
irwiseDanRer5', 'Bio.MSA.UCSC.hg18_pairwiseEquCab1', 'Bio.MSA.UCSC.hg18_pairwise
FelCat3', 'Bio.MSA.UCSC.hg18_pairwiseFr1', 'Bio.MSA.UCSC.hg18_pairwiseFr2', 'Bio
.MSA.UCSC.hg18_pairwiseGalGal2', 'Bio.MSA.UCSC.hg18_pairwiseGalGal3', 'Bio.MSA.U
CSC.hg18_pairwiseGasAcu1', 'Bio.MSA.UCSC.hg18_pairwiseMm7', 'Bio.MSA.UCSC.hg18_p
airwiseMm8', 'Bio.MSA.UCSC.hg18_pairwiseMm9', 'Bio.MSA.UCSC.hg18_pairwiseMonDom4
', 'Bio.MSA.UCSC.hg18_pairwiseOrnAna1', 'Bio.MSA.UCSC.hg18_pairwiseOryCun1', 'Bi
o.MSA.UCSC.hg18_pairwiseOryLat1', 'Bio.MSA.UCSC.hg18_pairwiseOryLat2', 'Bio.MSA.
UCSC.hg18_pairwisePanTro1', 'Bio.MSA.UCSC.hg18_pairwisePanTro2', 'Bio.MSA.UCSC.h
g18_pairwisePetMar1', 'Bio.MSA.UCSC.hg18_pairwisePonAbe2', 'Bio.MSA.UCSC.hg18_pa
irwiseRheMac2', 'Bio.MSA.UCSC.hg18_pairwiseRn4', 'Bio.MSA.UCSC.hg18_pairwiseSelf
', 'Bio.MSA.UCSC.hg18_pairwiseSorAra1', 'Bio.MSA.UCSC.hg18_pairwiseStrPur2', 'Bi
o.MSA.UCSC.hg18_pairwiseTaeGut1', 'Bio.MSA.UCSC.hg18_pairwiseTetNig1', 'Bio.MSA.
UCSC.hg18_pairwiseXenTro1', 'Bio.MSA.UCSC.hg18_pairwiseXenTro2', 'Bio.MSA.UCSC.h
g19_pairwiseCalJac1', 'Bio.MSA.UCSC.hg19_pairwiseGorGor1', 'Bio.MSA.UCSC.hg19_pa
irwiseMicMur1', 'Bio.MSA.UCSC.hg19_pairwiseOtoGar1', 'Bio.MSA.UCSC.hg19_pairwise
PanTro2', 'Bio.MSA.UCSC.hg19_pairwisePonAbe2', 'Bio.MSA.UCSC.hg19_pairwiseRheMac
2', 'Bio.MSA.UCSC.hg19_pairwiseTarSyr1', 'Bio.MSA.UCSC.mm5ToMm6', 'Bio.MSA.UCSC.
mm5ToMm7', 'Bio.MSA.UCSC.mm5ToMm8', 'Bio.MSA.UCSC.mm7ToMm5', 'Bio.MSA.UCSC.mm7To
Mm6', 'Bio.MSA.UCSC.mm7ToMm8', 'Bio.MSA.UCSC.mm7_multiz17way', 'Bio.MSA.UCSC.mm8
ToMm7', 'Bio.MSA.UCSC.mm8ToMm9', 'Bio.MSA.UCSC.mm8_multiz17way', 'Bio.MSA.UCSC.m
m8_pairwiseAnoCar1', 'Bio.MSA.UCSC.mm8_pairwiseBosTau2', 'Bio.MSA.UCSC.mm8_pairw
iseBosTau3', 'Bio.MSA.UCSC.mm8_pairwiseCanFam2', 'Bio.MSA.UCSC.mm8_pairwiseDanRe
r3', 'Bio.MSA.UCSC.mm8_pairwiseDanRer4', 'Bio.MSA.UCSC.mm8_pairwiseEquCab1', 'Bi
o.MSA.UCSC.mm8_pairwiseFelCat3', 'Bio.MSA.UCSC.mm8_pairwiseFr1', 'Bio.MSA.UCSC.m
m8_pairwiseGalGal2', 'Bio.MSA.UCSC.mm8_pairwiseGalGal3', 'Bio.MSA.UCSC.mm8_pairw
iseGasAcu1', 'Bio.MSA.UCSC.mm8_pairwiseHg17', 'Bio.MSA.UCSC.mm8_pairwiseHg18', '
Bio.MSA.UCSC.mm8_pairwiseMonDom4', 'Bio.MSA.UCSC.mm8_pairwiseOrnAna1', 'Bio.MSA.
UCSC.mm8_pairwisePanTro1', 'Bio.MSA.UCSC.mm8_pairwisePanTro2', 'Bio.MSA.UCSC.mm8
_pairwiseRheMac2', 'Bio.MSA.UCSC.mm8_pairwiseRn4', 'Bio.MSA.UCSC.mm8_pairwiseTet
Nig1', 'Bio.MSA.UCSC.mm8_pairwiseXenTro1', 'Bio.MSA.UCSC.mm8_pairwiseXenTro2', '
Bio.MSA.UCSC.mm9ToMm8', 'Bio.MSA.UCSC.mm9_multiz30way', 'Bio.MSA.UCSC.mm9_pairwi
seAnoCar1', 'Bio.MSA.UCSC.mm9_pairwiseBosTau3', 'Bio.MSA.UCSC.mm9_pairwiseBosTau
4', 'Bio.MSA.UCSC.mm9_pairwiseBraFlo1', 'Bio.MSA.UCSC.mm9_pairwiseCalJac1', 'Bio
.MSA.UCSC.mm9_pairwiseCanFam2', 'Bio.MSA.UCSC.mm9_pairwiseCavPor3', 'Bio.MSA.UCS
C.mm9_pairwiseDanRer5', 'Bio.MSA.UCSC.mm9_pairwiseEquCab1', 'Bio.MSA.UCSC.mm9_pa
irwiseFr2', 'Bio.MSA.UCSC.mm9_pairwiseGalGal3', 'Bio.MSA.UCSC.mm9_pairwiseGasAcu
1', 'Bio.MSA.UCSC.mm9_pairwiseHg18', 'Bio.MSA.UCSC.mm9_pairwiseMonDom4', 'Bio.MS
A.UCSC.mm9_pairwiseOrnAna1', 'Bio.MSA.UCSC.mm9_pairwiseOryLat1', 'Bio.MSA.UCSC.m
m9_pairwiseOryLat2', 'Bio.MSA.UCSC.mm9_pairwisePanTro2', 'Bio.MSA.UCSC.mm9_pairw
isePetMar1', 'Bio.MSA.UCSC.mm9_pairwisePonAbe2', 'Bio.MSA.UCSC.mm9_pairwiseRheMa
c2', 'Bio.MSA.UCSC.mm9_pairwiseRn4', 'Bio.MSA.UCSC.mm9_pairwiseTetNig1', 'Bio.MS
A.UCSC.mm9_pairwiseXenTro2', 'Bio.MSA.UCSC.monDom4_multiz7way', 'Bio.MSA.UCSC.mo
nDom4_pairwiseCalJac1', 'Bio.MSA.UCSC.monDom4_pairwiseCavPor3', 'Bio.MSA.UCSC.mo
nDom4_pairwiseDanRer3', 'Bio.MSA.UCSC.monDom4_pairwiseDanRer4', 'Bio.MSA.UCSC.mo
nDom4_pairwiseGalGal2', 'Bio.MSA.UCSC.monDom4_pairwiseGalGal3', 'Bio.MSA.UCSC.mo
nDom4_pairwiseHg18', 'Bio.MSA.UCSC.monDom4_pairwiseMm8', 'Bio.MSA.UCSC.monDom4_p
airwiseMm9', 'Bio.MSA.UCSC.monDom4_pairwiseOrnAna1', 'Bio.MSA.UCSC.monDom4_pairw
isePanTro2', 'Bio.MSA.UCSC.monDom4_pairwisePonAbe2', 'Bio.MSA.UCSC.monDom4_pairw
iseRn4', 'Bio.MSA.UCSC.monDom4_pairwiseXenTro2', 'Bio.MSA.UCSC.ornAna1_multiz6wa
y', 'Bio.MSA.UCSC.ornAna1_pairwiseAnoCar1', 'Bio.MSA.UCSC.ornAna1_pairwiseBosTau
4', 'Bio.MSA.UCSC.ornAna1_pairwiseCalJac1', 'Bio.MSA.UCSC.ornAna1_pairwiseGalGal
3', 'Bio.MSA.UCSC.ornAna1_pairwiseHg18', 'Bio.MSA.UCSC.ornAna1_pairwiseMm8', 'Bi
o.MSA.UCSC.ornAna1_pairwiseMm9', 'Bio.MSA.UCSC.ornAna1_pairwiseMonDom4', 'Bio.MS
A.UCSC.ornAna1_pairwisePonAbe2', 'Bio.MSA.UCSC.oryLat1_multiz5way', 'Bio.MSA.UCS
C.oryLat2_multiz5way', 'Bio.MSA.UCSC.oryLat2_pairwiseDanRer5', 'Bio.MSA.UCSC.ory
Lat2_pairwiseFr2', 'Bio.MSA.UCSC.oryLat2_pairwiseGasAcu1', 'Bio.MSA.UCSC.oryLat2
_pairwiseHg18', 'Bio.MSA.UCSC.oryLat2_pairwiseMm9', 'Bio.MSA.UCSC.oryLat2_pairwi
sePetMar1', 'Bio.MSA.UCSC.oryLat2_pairwiseTetNig1', 'Bio.MSA.UCSC.panTro1ToPantr
o2', 'Bio.MSA.UCSC.panTro2ToPantro1', 'Bio.MSA.UCSC.panTro2_pairwiseCalJac1', 'B
io.MSA.UCSC.panTro2_pairwiseCanFam2', 'Bio.MSA.UCSC.panTro2_pairwiseDanRer4', 'B
io.MSA.UCSC.panTro2_pairwiseEquCab1', 'Bio.MSA.UCSC.panTro2_pairwiseGalGal2', 'B
io.MSA.UCSC.panTro2_pairwiseHg17', 'Bio.MSA.UCSC.panTro2_pairwiseHg18', 'Bio.MSA
.UCSC.panTro2_pairwiseHg19', 'Bio.MSA.UCSC.panTro2_pairwiseMm8', 'Bio.MSA.UCSC.p
anTro2_pairwiseMm9', 'Bio.MSA.UCSC.panTro2_pairwiseMonDom4', 'Bio.MSA.UCSC.panTr
o2_pairwisePonAbe2', 'Bio.MSA.UCSC.panTro2_pairwiseRheMac2', 'Bio.MSA.UCSC.panTr
o2_pairwiseRn4', 'Bio.MSA.UCSC.petMar1_multiz6way', 'Bio.MSA.UCSC.petMar1_pairwi
seBraFlo1', 'Bio.MSA.UCSC.petMar1_pairwiseGalGal3', 'Bio.MSA.UCSC.petMar1_pairwi
seHg18', 'Bio.MSA.UCSC.petMar1_pairwiseMm9', 'Bio.MSA.UCSC.petMar1_pairwiseOryLa
t1', 'Bio.MSA.UCSC.petMar1_pairwiseOryLat2', 'Bio.MSA.UCSC.ponAbe2_multiz8way',
'Bio.MSA.UCSC.ponAbe2_pairwiseCalJac1', 'Bio.MSA.UCSC.ponAbe2_pairwiseGalGal3',
'Bio.MSA.UCSC.ponAbe2_pairwiseHg18', 'Bio.MSA.UCSC.ponAbe2_pairwiseHg19', 'Bio.M
SA.UCSC.ponAbe2_pairwiseMm9', 'Bio.MSA.UCSC.ponAbe2_pairwiseMonDom4', 'Bio.MSA.U
CSC.ponAbe2_pairwiseOrnAna1', 'Bio.MSA.UCSC.ponAbe2_pairwisePanTro2', 'Bio.MSA.U
CSC.ponAbe2_pairwiseRheMac2', 'Bio.MSA.UCSC.rheMac2_pairwiseCalJac1', 'Bio.MSA.U
CSC.rheMac2_pairwiseHg18', 'Bio.MSA.UCSC.rheMac2_pairwiseHg19', 'Bio.MSA.UCSC.rh
eMac2_pairwiseMm8', 'Bio.MSA.UCSC.rheMac2_pairwiseMm9', 'Bio.MSA.UCSC.rheMac2_pa
irwisePanTro2', 'Bio.MSA.UCSC.rheMac2_pairwisePonAbe2', 'Bio.MSA.UCSC.rheMac2_pa
irwiseRn4', 'Bio.MSA.UCSC.rn3ToRn4', 'Bio.MSA.UCSC.rn4ToRn3', 'Bio.MSA.UCSC.rn4_
multiz9way', 'Bio.MSA.UCSC.rn4_pairwiseBosTau2', 'Bio.MSA.UCSC.rn4_pairwiseBosTa
u3', 'Bio.MSA.UCSC.rn4_pairwiseCanFam2', 'Bio.MSA.UCSC.rn4_pairwiseCavPor3', 'Bi
o.MSA.UCSC.rn4_pairwiseDanRer3', 'Bio.MSA.UCSC.rn4_pairwiseDanRer4', 'Bio.MSA.UC
SC.rn4_pairwiseEquCab1', 'Bio.MSA.UCSC.rn4_pairwiseGalGal2', 'Bio.MSA.UCSC.rn4_p
airwiseGalGal3', 'Bio.MSA.UCSC.rn4_pairwiseHg18', 'Bio.MSA.UCSC.rn4_pairwiseMm8'
, 'Bio.MSA.UCSC.rn4_pairwiseMm9', 'Bio.MSA.UCSC.rn4_pairwiseMonDom4', 'Bio.MSA.U
CSC.rn4_pairwisePanTro2', 'Bio.MSA.UCSC.rn4_pairwiseRheMac2', 'Bio.MSA.UCSC.rn4_
pairwiseXenTro1', 'Bio.MSA.UCSC.rn4_pairwiseXenTro2', 'Bio.MSA.UCSC.tetNig1_pair
wiseDanRer3', 'Bio.MSA.UCSC.tetNig1_pairwiseDanRer4', 'Bio.MSA.UCSC.tetNig1_pair
wiseDanRer5', 'Bio.MSA.UCSC.tetNig1_pairwiseFr2', 'Bio.MSA.UCSC.tetNig1_pairwise
GasAcu1', 'Bio.MSA.UCSC.tetNig1_pairwiseHg18', 'Bio.MSA.UCSC.tetNig1_pairwiseMm6
', 'Bio.MSA.UCSC.tetNig1_pairwiseMm7', 'Bio.MSA.UCSC.tetNig1_pairwiseMm8', 'Bio.
MSA.UCSC.tetNig1_pairwiseMm9', 'Bio.MSA.UCSC.tetNig1_pairwiseOryLat1', 'Bio.MSA.
UCSC.tetNig1_pairwiseOryLat2', 'Bio.MSA.UCSC.xenTro1ToXentro2', 'Bio.MSA.UCSC.xe
nTro1_multiz5way', 'Bio.MSA.UCSC.xenTro2_multiz7way', 'Bio.MSA.UCSC.xenTro2_pair
wiseAnoCar1', 'Bio.MSA.UCSC.xenTro2_pairwiseDanRer4', 'Bio.MSA.UCSC.xenTro2_pair
wiseGalGal2', 'Bio.MSA.UCSC.xenTro2_pairwiseGalGal3', 'Bio.MSA.UCSC.xenTro2_pair
wiseHg18', 'Bio.MSA.UCSC.xenTro2_pairwiseMm8', 'Bio.MSA.UCSC.xenTro2_pairwiseMm9
', 'Bio.MSA.UCSC.xenTro2_pairwiseMonDom4', 'Bio.MSA.UCSC.xenTro2_pairwiseRn4', '
Bio.Seq.Genome.ANOCA.anoCar1', 'Bio.Seq.Genome.ANOGA.anoGam1', 'Bio.Seq.Genome.A
PIME.apiMel2', 'Bio.Seq.Genome.APIME.apiMel3', 'Bio.Seq.Genome.BOVIN.bosTau2', '
Bio.Seq.Genome.BOVIN.bosTau3', 'Bio.Seq.Genome.BOVIN.bosTau4', 'Bio.Seq.Genome.B
RAFL.braFlo1', 'Bio.Seq.Genome.CAEBR.cb3', 'Bio.Seq.Genome.CAEEL.ce2', 'Bio.Seq.
Genome.CAEEL.ce4', 'Bio.Seq.Genome.CAEEL.ce6', 'Bio.Seq.Genome.CAEJA.caeJap1', '
Bio.Seq.Genome.CAEPB.caePb1', 'Bio.Seq.Genome.CAEPB.caePb2', 'Bio.Seq.Genome.CAE
RE.caeRem2', 'Bio.Seq.Genome.CAERE.caeRem3', 'Bio.Seq.Genome.CALJA.calJac1', 'Bi
o.Seq.Genome.CANFA.canFam2', 'Bio.Seq.Genome.CAVPO.cavPor2', 'Bio.Seq.Genome.CAV
PO.cavPor3', 'Bio.Seq.Genome.CHICK.galGal2', 'Bio.Seq.Genome.CHICK.galGal3', 'Bi
o.Seq.Genome.CHOHO.choHof1', 'Bio.Seq.Genome.CIOIN.ci2', 'Bio.Seq.Genome.DANRE.d
anRer1', 'Bio.Seq.Genome.DANRE.danRer2', 'Bio.Seq.Genome.DANRE.danRer3', 'Bio.Se
q.Genome.DANRE.danRer4', 'Bio.Seq.Genome.DANRE.danRer5', 'Bio.Seq.Genome.DASNO.d
asNov1', 'Bio.Seq.Genome.DASNO.dasNov2', 'Bio.Seq.Genome.DIPOR.dipOrd1', 'Bio.Se
q.Genome.DROAN.droAna1', 'Bio.Seq.Genome.DROAN.droAna2', 'Bio.Seq.Genome.DROAN.d
roAna3', 'Bio.Seq.Genome.DROER.droEre1', 'Bio.Seq.Genome.DROER.droEre2', 'Bio.Se
q.Genome.DROGR.droGri1', 'Bio.Seq.Genome.DROGR.droGri2', 'Bio.Seq.Genome.DROME.d
m2', 'Bio.Seq.Genome.DROME.dm3', 'Bio.Seq.Genome.DROMO.droMoj1', 'Bio.Seq.Genome
.DROMO.droMoj2', 'Bio.Seq.Genome.DROMO.droMoj3', 'Bio.Seq.Genome.DROPE.droPer1',
 'Bio.Seq.Genome.DROPS.dp3', 'Bio.Seq.Genome.DROPS.dp4', 'Bio.Seq.Genome.DROSE.d
roSec1', 'Bio.Seq.Genome.DROSI.droSim1', 'Bio.Seq.Genome.DROVI.droVir1', 'Bio.Se
q.Genome.DROVI.droVir2', 'Bio.Seq.Genome.DROVI.droVir3', 'Bio.Seq.Genome.DROWI.d
roWil1', 'Bio.Seq.Genome.DROYA.droYak1', 'Bio.Seq.Genome.DROYA.droYak2', 'Bio.Se
q.Genome.ECHTE.echTel1', 'Bio.Seq.Genome.ERIEU.eriEur1', 'Bio.Seq.Genome.FELCA.f
elCat3', 'Bio.Seq.Genome.FUGRU.fr1', 'Bio.Seq.Genome.FUGRU.fr2', 'Bio.Seq.Genome
.GASAC.gasAcu1', 'Bio.Seq.Genome.GORGO.gorGor1', 'Bio.Seq.Genome.HORSE.equCab1',
 'Bio.Seq.Genome.HORSE.equCab2', 'Bio.Seq.Genome.HUMAN.hg17', 'Bio.Seq.Genome.HU
MAN.hg18', 'Bio.Seq.Genome.HUMAN.hg19', 'Bio.Seq.Genome.LAMPA.vicPac1', 'Bio.Seq
.Genome.LOXAF.loxAfr1', 'Bio.Seq.Genome.LOXAF.loxAfr2', 'Bio.Seq.Genome.MACMU.rh
eMac1', 'Bio.Seq.Genome.MACMU.rheMac2', 'Bio.Seq.Genome.MICMU.micMur1', 'Bio.Seq
.Genome.MONDO.monDom1', 'Bio.Seq.Genome.MONDO.monDom2', 'Bio.Seq.Genome.MONDO.mo
nDom4', 'Bio.Seq.Genome.MOUSE.mm5', 'Bio.Seq.Genome.MOUSE.mm6', 'Bio.Seq.Genome.
MOUSE.mm7', 'Bio.Seq.Genome.MOUSE.mm8', 'Bio.Seq.Genome.MOUSE.mm9', 'Bio.Seq.Gen
ome.MYOLU.myoLuc1', 'Bio.Seq.Genome.OCHPR.ochPri2', 'Bio.Seq.Genome.ORNAN.ornAna
1', 'Bio.Seq.Genome.ORYLA.oryLat1', 'Bio.Seq.Genome.ORYLA.oryLat2', 'Bio.Seq.Gen
ome.OTOGA.otoGar1', 'Bio.Seq.Genome.PANTR.panTro1', 'Bio.Seq.Genome.PANTR.panTro
2', 'Bio.Seq.Genome.PETMA.petMar1', 'Bio.Seq.Genome.PONAB.ponAbe2', 'Bio.Seq.Gen
ome.PONPA.ponAbe2', 'Bio.Seq.Genome.PRIPA.priPac1', 'Bio.Seq.Genome.PROCA.proCap
1', 'Bio.Seq.Genome.PTEVA.pteVam1', 'Bio.Seq.Genome.RABIT.oryCun1', 'Bio.Seq.Gen
ome.RAT.rn3', 'Bio.Seq.Genome.RAT.rn4', 'Bio.Seq.Genome.SORAR.sorAra1', 'Bio.Seq
.Genome.SPETR.speTri1', 'Bio.Seq.Genome.STRPU.strPur1', 'Bio.Seq.Genome.STRPU.st
rPur2', 'Bio.Seq.Genome.TAEGU.taeGut1', 'Bio.Seq.Genome.TARSY.tarSyr1', 'Bio.Seq
.Genome.TETNG.tetNig1', 'Bio.Seq.Genome.TRICA.triCas2', 'Bio.Seq.Genome.TUPGB.tu
pBel1', 'Bio.Seq.Genome.TURTR.turTru1', 'Bio.Seq.Genome.XENTR.xenTro1', 'Bio.Seq
.Genome.XENTR.xenTro2', 'Bio.Seq.Genome.YEAST.sacCer1']
    462
    """
    print worldbase.dir()
 
    print len(worldbase.dir())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
