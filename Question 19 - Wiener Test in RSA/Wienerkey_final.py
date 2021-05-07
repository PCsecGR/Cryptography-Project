import owiener

e, N = 65537, 22009517030106990383763465105609899090941157494196382925533444156480589292450396529663642850138695190588855805260835175270086166355060564256148792439233592472232233056950905840539154677121486094877597472487300649250039699499067065703656740364634411636945242292939908153976592139191106268327154757211809894086104466154946604045715191337979340318964774322733014276440202233403512948667806285436385349767243073268946721052707444588507283401697641243190019700333343119537943616295162029028870293037484015297179234631401220439538481352300280727764959004584544520437625051512885404930600391580169572809550082972986630285267

d = owiener.attack(e, N)

if d is None:
    print("There is no key for this pair of e and N")
else:
    print("A key was found!")