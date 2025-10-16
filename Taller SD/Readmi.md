#  Taller SD - Calculadora Remota (RMI con Pyro5)

## 
Este proyecto implementa un ejemplo de **Remote Method Invocation (RMI)** en **Python** utilizando la librería **Pyro5**.  
Permite ejecutar operaciones de una **calculadora remota** (sumar, restar, multiplicar y dividir) en un servidor, mientras el cliente las invoca como si fueran locales.  
Funciona de forma similar al **RMI de Java**, con un *Name Server* que actúa como registro.

---

## Estructura del proyecto
```
pyro_rmi_calculator/
├── calculator.py   # Clase remota expuesta (@expose)
├── server.py       # Publica el objeto remoto en el Name Server
└── client.py       # Cliente interactivo para invocar métodos
```

---

##  Ejecución

Se abrieron **tres terminales** en la carpeta del proyecto:

### 1 Inicia el Name Server (registro RMI)
```bash
python -m Pyro5.nameserver
```
Donde se vio:
```
NS running on localhost:9090
URI = PYRO:Pyro.NameServer@localhost:9090
```

### 2 Inicia el servidor
```bash
python server.py
```
Donde se vio:
```
Servidor listo. URI: PYRO:obj_f5df5ac15d654ddc8c166b4b311beb8d@localhost:53364
```

### 3 Inicia el cliente
```bash
python client.py
```
Aparecerá el menú interactivo:
```
=== Calculadora Remota (RMI con Pyro5) ===
Operaciones: add/sumar/+, subtract/restar/-, multiply/multiplicar/*, divide/dividir/
Escribe 'exit' para salir.
```

Ejemplo:
```
Operación: multiplicar
Primer número: 3
Segundo número: 4
Resultado: 12.0
```

---

##  Ejecución en distintas máquinas (opcional)

### 🖥️ Máquina 1 — Name Server
```bash
python -m Pyro5.nameserver -n IP_DEL_NAMESERVER
```

### 🖥️ Máquina 2 — Servidor
```bash
set PYRO_HOST=IP_DEL_SERVIDOR
set PYRO_NS_HOST=IP_DEL_NAMESERVER
python server.py
```

### 🖥️ Máquina 3 — Cliente
```bash
set PYRO_NS_HOST=IP_DEL_NAMESERVER
python client.py
```
---

## Explicación técnica

| Componente | Función | Equivalente en Java RMI |
|-------------|----------|--------------------------|
| `@expose` | Expone los métodos del objeto para invocación remota | `implements Remote` |
| `Pyro5.nameserver` | Registro de objetos remotos | `rmiregistry` |
| `Daemon()` | Servidor que recibe invocaciones | `UnicastRemoteObject` |
| `Proxy("PYRONAME:...")` | Busca y conecta al objeto remoto | `Naming.lookup()` |
| `remote.add(2,3)` | Invoca método remoto | `obj.add(2,3)` remoto |

s