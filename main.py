import HarcMenete
import JatekMenete
from Kezdoertekek import Jatekos
from SzerencseProbaja import jo_vagy_balszerencse


labirintus=JatekMenete.labirintus_generalasa()
jatekos=Jatekos(6,6,6)#jatekos generalasa
JatekMenete.jatek(labirintus, jatekos)
