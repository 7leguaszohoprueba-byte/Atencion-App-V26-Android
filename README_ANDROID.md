# Atención V26 — versión Android

Esta carpeta contiene una adaptación Android de Atención V26. La lógica de
negocio se conserva, pero la interfaz deja de usar Tkinter/Windows y utiliza
Kivy para controles táctiles.

## Funciones incluidas

- Configuración inicial con sucursal y administrador.
- Registro público sin pedir autorización.
- Casilla **Sin Datos**: limpia y bloquea Cliente, Teléfono y Correo.
- Regla Lead/Consulta compartida con la versión de escritorio.
- Registros limitados automáticamente a la sucursal configurada.
- Filtros de búsqueda, Atendió, Tipo, Solicitud, Estado y rango de fechas.
- Edición de registros.
- Historial de cambios.
- Importación de Excel con selector encima de cada columna y mapeo manual.
- La sucursal no se importa desde Excel: se asigna automáticamente la sucursal del dispositivo.
- Exportación a Excel de los registros visibles.
- Sincronización con Zoho Leads y Consultas.
- Conversión Lead → Consulta y Consulta → Lead.
- Actualización de registros existentes.
- Borrado remoto/local con manejo del caso en que el registro ya no exista en Zoho.
- Administración, usuarios gerentes, modo administrador y credenciales Zoho.

## Datos locales

Android utiliza una base SQLite dentro del almacenamiento privado de la aplicación.
No depende del Registro de Windows.

## Generar el APK

El proyecto está preparado para Buildozer. En un entorno Linux con las
herramientas de Android instaladas:

```bash
pip install buildozer
buildozer android debug
```

El APK aparecerá en `bin/`.

También se incluye un workflow de GitHub Actions para generar el APK sin
configurar el SDK manualmente en una PC Windows.

## Nota sobre esta entrega

El entorno de trabajo usado para preparar este proyecto no tiene el SDK/NDK de
Android ni Buildozer instalados, por lo que aquí se entrega el proyecto Android
listo para compilación, no un APK ya compilado.
