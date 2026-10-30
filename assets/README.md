# Gráficos del perfil

La cabecera utiliza capturas reales de Flutter Shop, Sentinel, Rocket Tracking y AnyShirt. La animación alterna capturas estáticas de los cuatro proyectos; no representa una grabación de las aplicaciones. Su procedencia está documentada en [screenshots/README.md](screenshots/README.md).

Las cuatro portadas de proyectos son ilustraciones animadas, no grabaciones de interfaz. El README ofrece versiones estáticas a quienes prefieren reducir el movimiento: PNG para la cabecera y SVG para las portadas.

Para regenerar los gráficos desde la raíz del repositorio:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r tools/requirements.txt
python tools/render_assets.py
```

Para regenerar solamente la cabecera:

```bash
python tools/render_assets.py --only header
```

El generador utiliza una paleta compartida y un patrón de tramado fijo para reducir las bandas de color. Los textos permanecen estáticos. El bucle de la cabecera dura dieciséis segundos (cuatro por proyecto); los de las portadas duran ocho segundos. Se conservan el SVG y la imagen estática del primer fotograma.

Se usa Segoe UI cuando está instalada, con Arial y sans-serif como alternativas. La tipografía puede variar al regenerar en otro sistema.
