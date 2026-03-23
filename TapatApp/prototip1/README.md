## Prototip 1
Connectar Client / Servidor.
Consultar dades d'usuari per nom.

[Digrama d'arquitectura prototip 1](TapatApp\charts\diagramaprototip.mermaid)


## End-Points WebService

Definició del End-point del WebService: 

URL Server desenvolupament: http://localhost:5000/

| URL | Method | Paràmetres | Descripció | Output |
|--------------|--------------|--------------|----------|----------|
| /user   | GET    | username <String> obligatori | Retornem la informació   de    | { "code_response=1, descripcio="", name="Gustavo Lloris", username="glloris",passwoprd="12345", rol="tutor", email="glloris@xtec.cat"}   |