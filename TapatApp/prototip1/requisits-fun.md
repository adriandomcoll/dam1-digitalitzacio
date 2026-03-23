# Requisits Funcionals TapatApp
## Descripció del projecte:
Una cataracta congènita és l'opacitat del cristal·lí de l'ull que està present en néixer. La incidència de cataracta congènita està al voltant dels 3 / 10.000 nens, a l'any de vida. A l'Hospital de Sant Joan de Déu s'han operat en l'últim any al voltant de 100 cataractes infantils.

Les cataractes són la causa més freqüent de ceguesa tractable en la infància i es podria fer una estimació de 200.000 nens cecs per cataracta al món.
L'ull amb cataracta congènita, un cop operat, ha de seguir un exhaustiu règim de rehabilitació per evitar l'ambliopia, el que coneixem comunament com "ull gandul", i aquí és on pretén ajudar TapatApp! 

L’objectiu de TapatApp consisteix en proporcionar a totes les famílies afectades per cataracta congènita, o qualsevol patologia que faci servir pedaç ocular, una eina senzilla i gratuïta que els ajudi a portar aquest tractament de la forma més equilibrada possible i, com a conseqüència, obtenir el màxim desenvolupament d’agudesa visual.

## Objectius del projecte

- Desarollar una app que compleixi amb el seguent:
- Controlar el temps que l'infant porta el tapat despert 
- Que s'adapti a l'edat de l'infant i segons el tractament, s'aplica un mètode o un altre
- Controlar el temps passat dormint amb el pegat.
- Permitir que diferents usuaris fiquen les horas que el nen a pasat amb el tapat baix la seva supervisió
- Poder compartir aquesta informació amb els metges 
- Acces restringit per tipus d'usuari al control del pegat. Aplicació Multiusuari

## Actors del sistema
- Administrador
- Servei Medic (Metges, oftalmòlegs)
- Tutors (mares/pares)
- Cuidadors (mestres, avis...)
- Infant
- Part pública

# Requisits funcionals RF i Requisits No Funcionals RNF
## RF1
### Login/Autenticació
Per poder fer servir la app, s'ha de auntentificar la persona amb l'email y una contraseña.

Actors: Admin, metges, tutors, cuidadors, infant

## RF2
### Registre Tutor
Que el tutor doni d'alta a l'infant, al seus medics y als altres cuidadors  

Actors: Tutor, Servei Medic

## RF3
### Desar l'informació a la base de dades
Enregistrar les dades de cada usuari una base de dades

Actors: Admin

## RF4 
### Registre de cuidador principal
Que els tutors puguin registrar una persona a l'aplicació com a cuidador/a principal per poder portar el control de les hores de pegat d’un infant amb cataracta congènita.

Actors: Tutors, Cuidadors

## RF5
### Registre d'hores
Que l'aplicació porti el control del temps del pegat a l'ull dels infants per a que qualsevol cuidador que hagués d’estar al càrrec del nostre fill, ja sigui per un temps llarg o curt, podria veure l’estat del tractament i portar-ne el control.
Actors: Tutor, Cuidadors

## RF6
### Notificar de retirar el tapat quan toca
Que el cuidador rebi un alerta a través de l’aplicació cada vegada que calculi, l’app, que el pegat s’ha de retirar per a que no sigui molt complicat saber quan de temps ha portat el pegat mentre està despert ja que quan està amb els avis molts cops no sabem de les hores que porta despert amb el pegat.

Actors: Tutors, cuidadors

## RF7
### Registre del tractament
Que les dades acumulades de seguiment del tractament que ha seguit l'infant per a que així poder donar-li directament a l'oftalmòleg quan tingui visites de seguiment del tractament.

Actors: Metges, Tutors, Cuidadors

## RNF1
### Sistema de pacients (SGP)
A la consulta treballen amb un sistema de gestió de pacients (SGP). Tenim que representar les dades de la mateixa manera que la SGP per compartir aquesta informació amb el seu sistema

Actors: Metges, Admin

## RNF2
### Recursos de l'aplicació
Que fer l'aplicació no demani molta memòria per que sigui simple d’anar en la majoria de dispositius mòbils

Actors: Admin

## RNF3
### Protecció de Dades
El Reglament General de la Protecció de Dades és de compliment obligat i estableix que totes les dades personals han de ser confidencials i no es poden distribuir a entitats externes sense un consentiment explícit de l’individu afectat.

Actors: Admin, Metges