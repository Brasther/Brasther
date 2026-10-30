# Gráficos del perfil

La cabecera y las cuatro portadas tienen una versión animada GIF y una versión estática SVG. Son ilustraciones del perfil, no grabaciones de las aplicaciones. El README ofrece la versión estática a quienes prefieren reducir el movimiento.

Para regenerarlas desde la raíz del repositorio:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r tools/requirements.txt
python tools/render_assets.py
```

El generador utiliza una paleta compartida entre fotogramas para evitar parpadeos de color. Los textos permanecen estáticos. Cada animación dura ocho segundos y se repite. Los SVG se generan con el primer fotograma y también sirven como fuentes editables.

Se usa Segoe UI cuando está instalada, con Arial y sans-serif como alternativas. La tipografía puede variar al regenerar en otro sistema.
