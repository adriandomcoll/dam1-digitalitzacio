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

## Requisits funcionals RF i Requisits No Funcionals RNF
- RF1: Login/Autenticació
Per poder fer servir la app, s'ha de auntentificar la persona amb l'email y una contraseña.
Actors: Admin, metges, tutors, cuidadors, infant

- RF2: Registre Tutor
Que el tutor doni d'alta a l'infant, al seus medics y als altres cuidadors  

- RF3: Desar l'informació a la base de dades
Enregistrar les dades de cada usuari una base de dades
Actors: Admin