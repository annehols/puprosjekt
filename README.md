# Nigiri Falls

## Kom i gang

Før du begynner å kode må fu sette opp prosjektet på din maskin. Det gjør du på denne måten:

_Linjer som starter med "$" er en kommando på kommandolinjen._
_Enkelte kommandoer er forskjellige i Windows og OS X/Linux. Jeg anbefaler derfor å bruke GitBash om du er på Windows, ettersom dette støtter UNIX-kommandoer. Denne guiden tar forbehold om at du gjør det._

### Clone dette git-repoet

Du starter gjerne med å clone dette repoet. Du kommer ikke langt uten å gjøre det først. Navigér i konsollen til mappen der du vil at "gruppe-26"-mappen skal ligge. Kjør følgende kommando:

```
$ git clone https://gitlab.stud.idi.ntnu.no/programvareutvikling-v19/gruppe-26.git
```

Når det er clonet så navigerer du inn i "gruppe-26" og bytter branch til _develop_. Du kommer til å være på _master_-branchen, men der er det ingen vits å holde på. Det er på _develop_ og dens avkom at det skjer.

```
$ cd gruppe-26
$ git checkout develop
```

Om du nå kjører `$ ls` vil du se litt av hvert. Men ingenting fungerer helt ennå.

### Lag et virtual environment

Først vil vi lage et virtual environment. Hensikten med dette er å isolere pakkene vi bruker fra resten av maskinen. Vi bruker Django, og det er viktig at vi dermed har en versjon av Django som er kompitabel med vår kode. Om man ikke bruker et virtual environment så kommer appen til å forsøke å bruke den versjonen som er installert på datamaskinen, og dette kan være feil. I et virtual environment så er våre pakker isolert fra eventuelle andre pakker på resten av maskinen, eller i andre prosjekter.

__Det er her viktig at man bruker python3!__ Det er mulig at python3 er det eneste som er installer på maskinen din. Sjekk dette med `$ python --version` - om versjonen er 3.\* så kan du bruke `$ python`. Om den sier 2.\* så må du bruke `$ python3`.

```
$ cd gruppe-26
$ python3 -m venv venv
```

Vent til prosessen fullføres. Skriv deretter `$ ls`, og du vil se en ny mappe kalt _venv_. Kjør denne kommandoen:

__UNIX__
```
$ source venv/bin/activate
```

__Windows (GitBash)__
```
$ source venv/Scripts/activate
```

Det vil nå stå "venv" ett eller annet sted i konsollen - i parantes over mappe-navnet i GitBash, og vansligvis et sted foran eller etter mappe-navnet i UNIX. Dette betyr at du er et "virtuelt miljø", en slag liten øy separert fra en del annet på maskinen din. Dette er bra, vi liker oss på denne øya.

### Installér Pip

Pip er en package manager for python. Jeg regner med alle har python på maskina si, og i så fall så skal egentlig Pip følge med. Det er dog mulig at det ikke finnes på vår lille øy. Du kan sjekke om du har Pip ved følgende kommando:

```
$ pip --version
```

Om det står ett eller annet versjonsnummer er du all good. Om ikke, følg instruksjonene på [denne siden](https://pip.pypa.io/en/stable/installing/) for å installere det. Sørg for at du kjører kommandoene i konsollen som er i vårt virtuelle miljø. Når greia er fullført, slett _get-pip.py_ (`$ rm get-pip.py`).

Kjør deretter en oppgradering for å være sikker på at du har siste versjon a Pip:

```
$ pip install --upgrade pip
```

### Installér requirements.txt

Du har nå Pip. Vi må da installere det vi trenger av moduler. Dette er særdeles enkelt. Fortsatt i venv-konsollen, i "gruppe-26"-mappen, kjør dette:

```
$ pip install -r requirements.txt
```

Litt shit skjer i konsollen. Når det er fullført har du alt du trenger av pakker for å sette i gang.

