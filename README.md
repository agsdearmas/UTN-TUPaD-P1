# Git Flow (rebase)


## Ramas principales

- `master`: Codigo estable y listo para produccion/entrega.
- `develop`: Codigo en desarrollo, integracion principal.


## Ramas secundarias

- `feature/<nombre>`: Ramas para tareas especificas o features.
- `hotfix/<nombre>`: Ramas para arreglos o pequeños cambios.


## Ciclo de trabajo

### 1. Crear una nueva rama (feature/hotfix) desde `develop`

```bash
git checkout develop
git pull origin develop
git checkout -b feature/tp1_login
```

### 2. Hacer commits locales en tu rama feature/hotfix

```bash
# al finalizar la edicion de codigo:
git add .
git commit -m "add: nuevo componente de login"
```

### 3. Mantener tu rama actualizada con `develop` usando rebase

Antes de hacer push o armar un PR:

```bash
# opcion 1: traer ultimos cambios de develop a rama actual (esto no actualiza rama develop)
git pull --rebase origin develop
```

```bash
# opcion 2: pasarse a rama develop para actualizar cambios, y luego llevarlos a rama actual (recomendado)
git checkout develop
git pull --rebase
git checkout feature/tp1_login
git rebase develop
```

Si hay conflictos:

```bash
# resolver conflictos manualmente, luego:
git add <archivos-modificados>
git rebase --continue
```

### 4. Subir tu rama al repositorio remoto

```bash
git push origin feature/tp1_login
```

### 5. Crear un Pull Request(PR) de rama actual hacia `develop`

- En GitHub, ir al repositorio.
- Seleccionar tu rama `feature/tp1_login`.
- Crear un PR contra `develop`.
- Agregar descripción clara.
- Asignar revisor si aplica.

### 6. Limpieza post PR (opcional)

Después de aprobar el PR:

```bash
git checkout develop
git pull origin develop
git branch -d feature/tp1_-_login         # borrar rama local
```

---

*Este documento fue creado para facilitar el trabajo colaborativo en proyectos de la facultad.*