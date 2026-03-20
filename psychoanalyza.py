# ********************** PROJEKT PSYCHOANALYZA ***********************

def zistenie_zaujmu_o_test(instrukcie):
  if instrukcie.lower() == "a":
    zakladne_otazky()
  elif instrukcie.lower() == "n":
    pass
  else:
    print("Zadany neplatný údaj!")



def zakladne_otazky():
  stres = input("Ako často sa cítiš preťažený/á alebo v strese?: ")
  uzkost = input("Ako často mávaš úzkostné pocity (napr. napätie, nepokoj, strach)?: ")
  smutok = input("Ako často sa cítiš smutný/á alebo beznádejný/á?: ")
  strata_zaujmu = input("Máš pocit, že strácaš záujem o veci, ktoré ťa kedysi bavili?: ")
  problemy_so_spankom = input("Mávaš problém so spánkom (narušený spánok, nespavosť, časté budenie)?: ")
  unava = input("Ako často sa cítiš unavený/á aj po oddychu?: ")
  pamat = input("Máš problémy so sústredením alebo pamäťou?: ")
  nezvladanie_emocii = input("Máš pocit, že tvoje emócie nezvládaš alebo nad nimi strácaš kontrolu?: ")
  osamelost = input("Cítiš sa osamelo alebo izolovane od ostatných?: ")
  kazdodenne_problemy = input("Máš pocit, že nedokážeš zvládať každodenné problémy a povinnosti?: ")

  zistenie_spravneho_formatu_zakladnych_odpovedi(stres,uzkost,smutok,strata_zaujmu,problemy_so_spankom,unava,pamat,nezvladanie_emocii,osamelost,kazdodenne_problemy)
  skore(stres,uzkost,smutok,strata_zaujmu,problemy_so_spankom,unava,pamat,nezvladanie_emocii,osamelost,kazdodenne_problemy)


def zistenie_spravneho_formatu_zakladnych_odpovedi(stres,uzkost,smutok,strata_zaujmu,problemy_so_spankom,unava,pamat,nezvladanie_emocii,osamelost,kazdodenne_problemy):
  while not (stres.isdigit() and 1 <= int(stres) <= 10):
    print("Zadaný zlý formát odpovede. Odpovedzte znova.")
    stres = input("Ako často sa cítiš preťažený/á alebo v strese?: ")

  while not (uzkost.isdigit() and 1 <= int(uzkost) <= 10):
    print("Zadaný zlý formát odpovede. Odpovedzte znova.")
    uzkost = input("Ako často mávaš úzkostné pocity (napr. napätie, nepokoj, strach)?: ")

  while not (smutok.isdigit() and 1 <= int(smutok) <= 10):
    print("Zadaný zlý formát odpovede. Odpovedzte znova.")
    smutok = input("Ako často sa cítiš smutný/á alebo beznádejný/á?: ")

  while not (strata_zaujmu.isdigit() and 1 <= int(strata_zaujmu) <= 10):
    print("Zadaný zlý formát odpovede. Odpovedzte znova.")
    strata_zaujmu = input("Máš pocit, že strácaš záujem o veci, ktoré ťa kedysi bavili?: ")

  while not (problemy_so_spankom.isdigit() and 1 <= int(problemy_so_spankom) <= 10):
    print("Zadaný zlý formát odpovede. Odpovedzte znova.")
    problemy_so_spankom = input("Mávaš problém so spánkom (narušený spánok, nespavosť, časté budenie)?: ")

  while not (unava.isdigit() and 1 <= int(unava) <= 10):
    print("Zadaný zlý formát odpovede. Odpovedzte znova.")
    unava = input("Ako často sa cítiš unavený/á aj po oddychu?: ")

  while not (pamat.isdigit() and 1 <= int(pamat) <= 10):
    print("Zadaný zlý formát odpovede. Odpovedzte znova.")
    pamat = input("Máš problémy so sústredením alebo pamäťou?: ")

  while not (nezvladanie_emocii.isdigit() and 1 <= int(nezvladanie_emocii) <= 10):
    print("Zadaný zlý formát odpovede. Odpovedzte znova.")
    nezvladanie_emocii = input("Máš pocit, že tvoje emócie nezvládaš alebo nad nimi strácaš kontrolu?: ")

  while not (osamelost.isdigit() and 1 <= int(osamelost) <= 10):
    print("Zadaný zlý formát odpovede. Odpovedzte znova.")
    osamelost = input("Cítiš sa osamelo alebo izolovane od ostatných?: ")

  while not (kazdodenne_problemy.isdigit() and 1 <= int(kazdodenne_problemy) <= 10):
    print("Zadaný zlý formát odpovede. Odpovedzte znova.")
    kazdodenne_problemy = input("Máš pocit, že nedokážeš zvládať každodenné problémy a povinnosti?: ")

def skore(stres,uzkost,smutok,strata_zaujmu,problemy_so_spankom,unava,pamat,nezvladanie_emocii,osamelost,kazdodenne_problemy):
  celkove_skore = (int(stres) + int(uzkost) + int(smutok) + int(strata_zaujmu) + int(problemy_so_spankom) + int(unava) + int(pamat) + int(nezvladanie_emocii) + int(osamelost) + int(kazdodenne_problemy)) / 10
  print("\n Celkovy počet bodov: " , celkove_skore)
  vysledky(celkove_skore, stres, uzkost, smutok, strata_zaujmu, problemy_so_spankom, unava, pamat, nezvladanie_emocii, osamelost, kazdodenne_problemy)

def vysledky(celkove_skore, stres, uzkost, smutok, strata_zaujmu, problemy_so_spankom, unava, pamat, nezvladanie_emocii, osamelost, kazdodenne_problemy):
  if celkove_skore >= 1 and celkove_skore < 3:
    print("\n Psychický stav je dobrý - zvládaš to.")
  elif celkove_skore >= 3 and celkove_skore < 5:
    print("\n Mierne ťažkosti - odporúčam oddych, rozhovor, psychohygienu.")
  elif celkove_skore >= 5 and celkove_skore < 7:
    print("\n Zvýšené riziko - premýšľaj nad odbornou pomocou (psychológ, školský psychológ).")
  else:
    print("\n Vysoké psychické zaťaženie - silne odporúčaná konzultácia s odborníkom.")
  
  odporucania_podla_problemov(stres, uzkost, smutok, strata_zaujmu, problemy_so_spankom, unava, pamat, nezvladanie_emocii, osamelost, kazdodenne_problemy)


def odporucania_podla_problemov(stres, uzkost, smutok, strata_zaujmu, problemy_so_spankom, unava, pamat, nezvladanie_emocii, osamelost, kazdodenne_problemy):
  print("\n Odporúčania na základe konkrétnych oblastí:\n")

  if int(stres) >= 8:
    print(" Máš veľmi vysokú mieru stresu. Skús dychové cvičenia, obmedziť multitasking a vytvoriť si denný režim.")
  
  if int(uzkost) >= 8:
    print(" Silná úzkosť. Pomáhajú techniky mindfulness, meditácia, a rozhovor s terapeutom.")
  
  if int(smutok) >= 8:
    print(" Pretrvávajúci smútok môže naznačovať depresívne tendencie. Pomáha rozhovor s dôveryhodnou osobou alebo odborníkom.")
  
  if int(strata_zaujmu) >= 8:
    print(" Strácaš záujem o veci, ktoré ťa kedysi bavili. To môže byť príznak depresie – zváž rozhovor s psychológom.")
  
  if int(problemy_so_spankom) >= 8:
    print(" Máš veľké problémy so spánkom. Skús pravidelný režim spánku, vyhni sa obrazovkám pred spaním.")
  
  if int(unava) >= 8:
    print(" Nadmerná únava môže súvisieť so stresom alebo vyčerpaním. Skús si vytvoriť rovnováhu medzi prácou a oddychom.")
  
  if int(pamat) >= 8:
    print(" Problémy so sústredením alebo pamäťou môžu byť dôsledkom stresu. Pomáhajú mentálne hry, zdravý spánok a oddych.")
  
  if int(nezvladanie_emocii) >= 8:
    print(" Máš pocit, že nezvládaš svoje emócie. Vyskúšaj vedenie denníka, dýchanie alebo odbornú pomoc.")
  
  if int(osamelost) >= 8:
    print(" Vysoký pocit osamelosti. Skús kontaktovať priateľov, tráviť viac času medzi ľuďmi, alebo sa zapojiť do záujmových aktivít.")
  
  if int(kazdodenne_problemy) >= 8:
    print(" Problémy so zvládaním bežných povinností môžu byť vážnym signálom. Pomáha rozvrh, podpora okolia, psychológ.")

instrukcie = input("Toto je môj psychoanalytický test vašeho psychického zdravia, nálad, \n emócii, ktorý vám pomôže zistiť, s čím máte problém, a ako s tým bojovať.\n Budete odpovedať na  nasledovné otázky číselne od 1 (vôbec) až po 10(úplne). \n Na konci testu zistíte svoje vyhodnotenie, ako aj spôsob, čo s tým spraviť. \n Chcete spustiť test? (a/n): ")

zistenie_zaujmu_o_test(instrukcie)
