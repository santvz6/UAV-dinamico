# Simulación y Control de un Dron Quadrotor (UAV)

Este proyecto implementa la simulación en tiempo continuo de la dinámica no lineal de un dron Quadrotor y diseña un sistema de control PD en cascada para estabilizarlo y guiarlo a una posición objetivo.

## Estructura del Proyecto

El proyecto está modularizado en Python (POO) para manejar la complejidad del sistema de 12 EDOs (Ecuaciones Diferenciales Ordinarias) y la lógica de control.

| Fichero | Clase Principal | Descripción y Responsabilidad |
| :--- | :--- | :--- |
| `dynamics.py` | `QuadrotorDynamics` | Contiene las **12 EDOs no lineales** que rigen el movimiento del dron (posición, velocidad, ángulos y velocidad angular). |
| `controller.py` | `CascadedController` | Implementa el **control PD en cascada**. El bucle interno estabiliza la actitud, y el bucle externo calcula los ángulos necesarios para alcanzar la posición deseada. |
| `visualizer.py` | `Plotter` | Genera la **visualización 3D** de la trayectoria y las gráficas 2D de series de tiempo para evaluar el rendimiento del control (errores de posición y ángulos de actitud). |
| `main.py` | `main()` | Script principal que inicializa el sistema, define la misión (punto objetivo) y ejecuta el bucle de integración numérica. |

## Metodología y Modelo

### 1. Sistema Dinámico

El Quadrotor es modelado como un sistema de **12 estados** con **seis grados de libertad (6-DOF)**, regido por las leyes de Newton-Euler. El sistema es **sub-actuado** (4 fuerzas de control para 6-DOF), lo que lo hace inherentemente inestable y un desafío de control. 

* **Vector de Estado (X):**
    $$X = [x, y, z, \dot{x}, \dot{y}, \dot{z}, \phi, \theta, \psi, p, q, r]^T$$
* **Vector de Control (U):** Las fuerzas de empuje de los cuatro rotores ($F_1, F_2, F_3, F_4$).

### 2. Control en Cascada (PD)

Se utiliza un enfoque de control en cascada, donde los bucles internos operan más rápido que los externos .
* **Controlador de Posición (Bucle Externo):** Calcula la **fuerza de empuje total ($T$)** requerida para el eje Z y los **ángulos de actitud deseados ($\phi_d, \theta_d$)** requeridos para moverse en X e Y.
* **Controlador de Actitud (Bucle Interno):** Utiliza un control PD para calcular los **torques ($\tau_\phi, \tau_\theta, \tau_\psi$)** necesarios para corregir la actitud hacia los ángulos deseados, manteniendo la estabilidad.

## Herramientas y Ejecución

### Requisitos

El proyecto requiere las siguientes librerías de Python:
* `numpy` (Cálculo vectorial)
* `scipy` (Integración numérica de EDOs, `solve_ivp`)
* `matplotlib` (Visualización 2D y 3D)

### Estructura de Ficheros

La simulación asume la siguiente estructura de directorios para la correcta importación de los módulos:

```bash
/sistema dinamico
├── app
│   ├── dynamics.py
│   ├── controller.py
│   ├── visualizer.py
│   └── main.py
└── README.md
```

### Ejecución

El proyecto se ejecuta desde el script principal ubicado en el subdirectorio `app`.

``` bash
python3 app/main.py
```

### Resultados Esperados
La simulación generará las siguientes salidas visuales:

- Gráfica 3D (Trayectoria): Muestra cómo el dron vuela desde la posición inicial hasta el punto objetivo (definido en main.py), demostrando la capacidad de seguimiento de trayectoria.

- Gráficas 2D (Errores de Posición): Muestra cómo los errores en X, Y y Z convergen a cero en el tiempo, demostrando que el controlador es estable y logra el objetivo.

- Gráficas 2D (Ángulos de Actitud): Muestra cómo los ángulos de Roll ($\phi$) y Pitch ($\theta$) son forzados a cero (o a los ángulos calculados por el bucle externo) para mantener el vuelo estable.