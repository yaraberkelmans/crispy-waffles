# Lectures &amp; Lesroosters 
Lesroosters, of roosters in het algemeen, zijn buitengewoon lastig goed in te richten. Dienstregelingen voor treinen, vliegtuigen, multicore-processors en assembly lines hebben in dat opzicht een boel met elkaar gemeen. Zalenroostering op een universiteit is geen uitzondering. In deze case moet een weekrooster gemaakt worden voor een vakkenlijst op Science Park.

Enkele aannames en vereisten voor deze case:
Vakken bestaan uit vakactiviteiten: hoorcolleges en/of werkcolleges en/of practica.
Alle zalen zijn voor alle drie collegetypes geschikt.
Bij hoorcolleges moeten alle ingeschreven studenten ineens bedeeld worden.
Een college duurt van 9:00-11:00, 11:00-13:00, 13:00-15:00 of 15:00-17:00 op een werkdag. Eén zo’n periode van twee uur wordt een tijdsslot genoemd. 
Alleen de grootste zaal C0.110 heeft ook een avondslot van 17:00 tot 19:00
Een geldig weekrooster is een weekrooster waarvoor aan alle roosterbare activiteiten van ieder vak een tijdsslot met een zaal hebben. We noemen het paar tijdsslot-zaal een zaalslot.
Een zaalslot kan enkel gebruikt worden voor één activiteit.

## Aan de slag
### Vereisten
Deze codebase is volledig geschreven in Python 3.12.4.
In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:
```
pip install -r requirements.txt
```

Of via conda:

```
conda install --file requirements.txt
```

## Scores
De uiteindelijke score van een rooster wordt berekend aan de hand van maluspunten:

- Iedere student die niet meer in een zaal past levert een maluspunt op.
- Ieder vakconflict (meer dan één activiteit op hetzelfde moment) in het rooster van één student levert 1 maluspunt op.
- Het gebruik van de grote zaal tijdens het avondslot kost 5 maluspunten.
- Een tussenslot voor een student op een dag levert 1 maluspunt op. Twee tussensloten op één dag voor een student levert 3 maluspunten op. Drie tussensloten op één dag is niet toegestaan. De kans op verzuim bij meerdere tussensloten is namelijk aanzienlijk groter dan bij één tussenslot, hiervoor worden 1000 maluspunten gerekend.

### Gebruik
Een voorbeeld kan gerund worden door het aanroepen van:

```
python main.py algorithm output_file_path 
```

Het bestand geeft een voorbeeld voor gebruik van de verschillende functies en het aanmaken van een rooster.


### Experimenten
Voor het uitvoeren van een experiment in Simulated Annealing kan een experiment class worden aangeroepen met 
bepaalde waardes. Hiervoor kan gebruik worden gemaakt van parallel running, door iedere keer de waardes aan te passen om die versie
vervolgens in een nieuwe terminal te laten runnen. Zo is het modelijk om binnen een redelijke tijd met meerdere waardes te kunnen experimenteren. 
    
De experimenten kunnen gerunt worden met (bijvoorbeeld) de volgende waardes:

- 7 neighbours en 1 swaps per neighbour
- 7 neighbours en 2 swaps per neighbour
- 7 neighbours en 3 swaps per neighbour
- 8 neighbours en 1 swaps per neighbour
- 8 neighbours en 2 swaps per neighbour
- 8 neighbours en 3 swaps per neighbour
- 9 neighbours en 1 swaps per neighbour
- 9 neighbours en 2 swaps per neighbour
- 9 neighbours en 3 swaps per neighbour

Het algoritme slaat deze experimenten automatisch op als aparte en verschillende pickle files, het geeft namelijk een naam op 
basis van de parameters, welke bij elk experiment verschillend zijn. Ook maakt de experiment automatisch een folder aan die je 
mee kan geven.

Voor het tweede experiment kan worden gekeken naar een goede Temperatuur voor Simulated Annealling. De manier van experimenteren
blijft hetzelfde, maar hierbij kan er gevarieert worden met de temperatuur. Mogelijke waardes voor temperatuur kunnen zijn: 
- 1
- 2.5
- 5
- 10
- 20
- 50

Alle resultaten van deze experimenten worden opgeslagen als pickle bestand in het mapje results/pickle_files en de 
experiment instances kunnen van daaruit worden ingeladen om te gerbuiken voor verschillende plots.

## Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de 6 benodigde classes voor deze case
  - **/code/visualisation**: bevat de code voor de visualisatie
- **/data**: bevat de verschillende databestanden die nodig zijn om experimenten en het rooster te visualiseren
- **/results**:
  - **/results/best_timetable_data**: bevat de data voor de uiteindelijk best gevonden timetable
  - **/results/pickle_files**: bevat alle folders met pickle files voor beste timetables en hun experiment
  - **/results/plots**: bevat de plots die uit de experimenten zijn gevormd

## Auteurs
- Yara Berkelmans
- Max van Beusekom
- Tijn Otto
