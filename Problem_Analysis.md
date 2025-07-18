
# Problem Analysis: AIDECK 500 Internal Error & Metrics Endpoint

## 1. Kontekstas
- **Frontend**: Veikia http://localhost:3000, statiniai failai kraunami teisingai.
- **Backend**: FastAPI startuoja be klaidų, tačiau užklausos į `/metrics` grąžina `404 Not Found`.
- **Prometheus**: Tikisi `/metrics` endpoint'o duomenų rinkimui.
- **.env**: CORS_ORIGINS nustatytas į `http://localhost:3000`, DB/Redis sukonfigūruoti, akivaizdžių konfigūracijos klaidų nėra.

## 2. Pastebėtos problemos
- **500 Internal Error**: Matoma naršyklėje bandant pasiekti UI, backend loguose tiesiogiai nematyti.
- **/metrics 404**: Backend'e nėra `/metrics` endpoint'o, todėl Prometheus negali surinkti metrikų, o frontend arba monitoringas gali gauti 500 klaidą bandant pasiekti šį API.
- **Kritinių klaidų nėra**: Visi servisai startuoja be fatališkų klaidų.

## 3. Priežastis
- **Trūksta /metrics endpoint'o**: FastAPI pagal nutylėjimą nesukuria `/metrics`. Prometheus ir galimai frontend tikisi šio API.
- **Prometheus negali surinkti metrikų**: Backend loguose kartojasi 404 klaidos dėl `/metrics`.
- **Frontend 500 klaida**: Dažniausiai kyla, kai frontend bando pasiekti trūkstamą API endpoint'ą.

## 4. Sprendimas
1. **Įdiegti priklausomybę**:
   ```bash
   pip install prometheus-fastapi-instrumentator
   ```
2. **Papildyti backend/main.py**:
   ```python
   from prometheus_fastapi_instrumentator import Instrumentator
   # ...existing FastAPI app setup...
   Instrumentator().instrument(app).expose(app)
   ```
3. **Perkompiliuoti ir paleisti backend iš naujo**, kad pakeitimai įsigaliotų.

## 5. Patikrinimas
- **/metrics**: Turi grąžinti Prometheus metrikas, nebe 404.
- **Prometheus**: Turi sėkmingai surinkti metrikas.
- **Frontend**: 500 klaida turi išnykti, jei ji buvo susijusi su trūkstamu `/metrics`.

## 6. Santraukos lentelė
| Problema             | Priežastis                  | Sprendimas                                 |
|----------------------|-----------------------------|---------------------------------------------|
| `/metrics` 404       | Endpoint'as neįgyvendintas  | Pridėti Prometheus metrics route backend'e  |
| 500 Internal Error   | Trūksta API endpoint'o      | Įgyvendinti trūkstamą endpoint'ą, tikrinti logus |

---

> Ši analizė apima pagrindinę 500 klaidos ir trūkstamo `/metrics` endpoint'o priežastį bei aiškius sprendimo žingsnius.
