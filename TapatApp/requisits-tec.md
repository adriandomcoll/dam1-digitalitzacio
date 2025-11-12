# Requisits Técnics TapatApp

## Arquitectura

[Client Servidor](/dam1-desenvolupament/requisits.md)

## 1. Backend (Servidor i Gestió de Dades)

El backend sera el cor del sistema, encarregat de gestionar dades, usuaris i la lògica del sistema

### a. Requisits del Servidor

- Allotjament: Hosting compartit
- Base de dades: Mysql o MariaDB
- Sistema Operatiu: Linux o Windows
- WebService: RESTFul llibreria Python FLask

### b. Llenguatges de Programació

Python

### c. Seguretat

- Autenticació i autoritcació pels usuaris
- Xifratge de dades HTTPS
- Copies de seguretat automàtiques

## 2. Frontend

### a. Tipus de Clients

- App Mòbil: Android
- Consola Python
- Frameworks Multiplataforma: Flutter (Apps IOS Android, Web, Desktop)

### b. Enmagatzematge local i sincronització

- Dades guardem en local: Token, nickname
- Seguretat: HTTPS, autenticació serveis per Token

### c. Gestió d'accesibilitat

- Nivells A, AA, AAA d'accesibilitat

## 3. Requisits Generals Infraestructura

### a. Gestió d'usuari i autenticació

- Rols d'usuari: Tutor i cuidador
- Seguretat password: md5, sha256 o sha512

### b. Requisits d'Infraestructura
- Xarxa: Internet
- Espai d'enmagatzemantge a Servidor: 1TB
- APIs a tercers: No fem servir

## 4. Requisits del Procés de Desenvolupament

- IDE's: VScode Python, Android Studio, PyCharm
- Control de versions: git, GitHub
- Metodologia de desenvolupament: SCRUM
- Testing i proves de qualitat(QA): Tests i proves unitàries