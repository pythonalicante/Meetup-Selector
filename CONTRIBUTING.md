# Contributing guidelines

Para contribuir en este proyecto, puedes hacerlo de dos maneras:
- Hacer un `fork` del proyecto
- Pedir que te añadamos al proyecto, en el grupo [Hacktoberfest](https://github.com/orgs/pythonalicante/teams/hacktoberfest) y tener acceso al repositorio.

Una vez tengas acceso al repositorio, debes crear una rama a partir de `dev` con el siguiente formato: `númerodeissue-pequeña_descripción`, e.g.: `006-topic-proposal`. Una vez hayas acabado de hacer las tareas correspondientes del `issue` tienes que crear la `Pull Request`.

Este estilo de ramas se conoce como [GitFlow](https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow), por si quieres profundizar más.

Para asignarte un `issue`, comenta en la que quieras realizar, y se te asignara.

## Estilo

El estilo que seguimos en este proyecto es el descrito por el [PEP8](https://www.python.org/dev/peps/pep-0008/), el cual checkeamos en nuestro sístema de `CI/CD` con la herramienta `flake8`. Tambien comentar que excluimos ciertos errores:
- E501: Line too long
- E722: Multiple statements on one line

Además, tienes el comando `make prepush` para comprobar que todo esta correcto antes de subir el proyecto.

Para los `commits` usaremos el estilo de `commits`: [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
