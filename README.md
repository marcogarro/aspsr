# Meteo App con Autenticazione

Questa semplice applicazione web scritta in Python utilizza Flask per gestire
l'autenticazione di base e consentire la visualizzazione del meteo di una città
italiana. L'interfaccia grafica sfrutta Bootstrap tramite CDN.

## Requisiti

- Python 3.8+
- Le dipendenze indicate in `requirements.txt`

## Installazione

1. Creare un ambiente virtuale (opzionale):

```bash
python -m venv venv
source venv/bin/activate
```

2. Installare le dipendenze:

```bash
pip install -r requirements.txt
```

3. Avviare l'applicazione:

```bash
python app.py
```

## Utilizzo

- Accedere con le credenziali di default `admin` / `password`.
- Inserire una città italiana nella pagina "Consulta il meteo" per ottenere le
  informazioni dal servizio [Open‑Meteo](https://open-meteo.com/).

## Note

Questa applicazione è a solo scopo dimostrativo. In un ambiente di produzione
è consigliabile utilizzare una gestione sicura delle password e un segreto più
robusto per le sessioni.
