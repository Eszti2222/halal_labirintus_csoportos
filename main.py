import HarcMenete
import JatekMenete
import Kezdoertekek
from Kezdoertekek import Kezdoertekek
import SzerencseProbaja

kezdo_lista=[]
kezdo_lista.append(Kezdoertekek("Ügyesség"), )

labirintus=JatekMenete.labirintus_generalasa()
jatekos=Kezdoertekek.Kezdoertekek(6,6,6)#jatekos generalasa
JatekMenete.jatek(labirintus, jatekos)