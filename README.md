# VPW

Bevat vragen van vorige jaren met een aantal oplossingen. Vragen worden
aangemaakt op basis van de `template`.

## Structuur

De oefeningen zijn georganiseerd volgens het jaar en dan de naam van de
oefening.

* Wedstrijd invoer: `wedstrijd.invoer`
* Wedstrijd (verwachte) uitvoer: `wedstrijd.uitvoer`
* Onze oplossing: `oplossing.py3`
* Symlink voor betere IDE integratie (zelfde bestand als `oplossing.py3`): `oplossing.py`
* Template test voor snel testen van code (handig in IDE): `tests.py`
* Tekst met de verwachte moeilijkheden: `README.md`
* Script dat de code test zoals de submissie servers: `run.sh`

## Run.sh

Klein scriptje dat een `diff` uitvoert tussen onze output en de verwachte
wedstrijd uitvoer bij de verwachte wedstrijd invoer zonder tijdslimiet. Dit 
scriptje verwacht de structuur van de template met `wedstrijd.input`,
`wedstrijd.uitvoer` en `oplossing.py3`
