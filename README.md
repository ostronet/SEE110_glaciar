# SEE110 Klimatmodellering: Glaciärer i Skandinavien under 2000-talet

Det här är repot innehåller kursmaterial för att komma igång med projekt fem: Glaciärer i Skandinavien under 2000-talet, som är en del av kursen SEE110 Klimatmodellering på [Chalmers Tekniska Högskola](https://www.chalmers.se/).


## Instruktioner för studenter som arbetar på OGGM Classroom (Rekommenderas)

1. Skapa ett konto via [denna länken](https://classroom.oggm.org/hub/signup). Ditt användarnamn ska följa mallen `cth25_{cid}`: som exempel, mitt cid är eriholmg, och då ska mitt användarnamn vara `cth25_eriholmg`. Din handledare kommer godkänna ditt nya konto så snart som möjligt.
2. När ditt konto har blivit gondkänt, logga in och välj  `oggm-v162` från "server options".
3. Öppna en terminal `File->New->Terminal` och från din hemkatalog kör följande kommandon:
    ```bash
    gitpuller https://github.com/OGGM/oggm-edu-notebooks master edu_notebooks
    gitpuller https://github.com/SEE-GEO/see110_glacier_intro.git main see110_glacier_intro
    ```
    Detta kommer ladda ner två repon med notebooks som är relevanta för att du ska komma igång med OGGM och projektet.
    Dessa kommer vara tillgängliga i mapparna `edu_notebooks` och `see110_glacier_intro` i din hemkatalog.

### Generell info
- Varje konto har 10GB lagringsutrymme. Detta är mer än tillräckligt för arbetet med era projekt. Du kan kolla hur mycket du använder genom att köra `du -h --max-depth=1 .` i hemkatalogen.
- Spara ditt i arbete direkt i hemkatalogen (`/home/jovyan`), eller en ny undermapp. Notera att du har tillgång till en delad mapp `/home/jovyan/shared`, du kommer dock **inte** behöva använda denna. 
- Upptäcker du att det mot förmodan saknas ett python-paket du behöver för din analys kan detta installeras med antingen `pip` eller `conda` i terminalen. Detta kommer du behöva göra om varje gång du startar om servern/loggar in.

## Instruktioner för att arbeta på egen dator

För att arbeta med projeketet på din egen dator kan du antingen ladda ner filerna med
```bash
git clone https://github.com/SEE-GEO/see110_glacier_intro.git
```
eller som en [zip](https://github.com/SEE-GEO/see110_glacier_intro/archive/refs/heads/main.zip).

Du behöver ha följande python-paket, och paket de är beroende av, installerade för att kunna följa med i instruktionerna:
- oggm
- NumPy
- matplotlib
- juypterlab
- xarray
- netcdf4
- cartopy


## Rapportera fel

Hittar du något du tycker verkar tokigt kan du alltid öppna ett "issue" här på GitHub.
