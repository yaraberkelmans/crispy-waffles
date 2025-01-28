# Lectures &amp; Lesroosters 
Lesroosters, of roosters in het algemeen, zijn buitengewoon lastig goed in te richten. Dienstregelingen voor treinen, vliegtuigen, multicore-processors en assembly lines hebben in dat opzicht een boel met elkaar gemeen. Zalenroostering op een universiteit is geen uitzondering. In deze case moet een weekrooster gemaakt worden voor een vakkenlijst op Science Park.

Enkele aannames en vereisten voor deze case:
Vakken bestaan uit vakactiviteiten: hoorcolleges en/of werkcolleges en/of practica.
Alle zalen zijn voor alledrie collegetypes geschikt.
Bij hoorcolleges moeten alle ingeschreven studenten ineens bedeeld worden.
Een college duurt van 9:00-11:00, 11:00-13:00, 13:00-15:00 of 15:00-17:00 op een werkdag. Eén zo’n periode van twee uur wordt een tijdsslot genoemd. 
  Alleen de grootste zaal C0.110 heeft ook een avondslot van 17:00 tot 19:00
Een geldig weekrooster is een weekrooster waarvoor aan alle roosterbare activiteiten van ieder vak een tijdsslot met een zaal hebben. We noemen het paar tijdsslot-zaal een zaalslot.
Een zaalslot kan enkel gebruikt worden voor één activiteit.

# Aan de slag

# Scores
De uiteindelijke score van een rooster wordt berekend aan de hand van maluspunten, waarbij:

- Voor iedere student die niet meer in de zaal past krijg je een maluspunt.
- Ieder vakconflict (meer dan één activiteit op hetzelfde moment) in het rooster van één student levert 1 maluspunt op.
- Het gebruik van de grote zaal tijdens het avondslot kost 5 maluspunten.
- Een tussenslot voor een student op een dag levert 1 maluspunt op. Twee tussensloten op één dag voor een student levert 3 maluspunten op. Drie tussensloten op één dag is niet toegestaan. De kans op verzuim bij meerdere        tussensloten is namelijk aanzienlijk groter dan bij één tussenslot, hiervoor rekenen we 1000 maluspunten.
