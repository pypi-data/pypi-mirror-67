# Logging tools

Une simple librairie permettant de faire des opérations de logging grâce à un décorateur

## Chronometer

Utilitaire permettant de savoir le temps d'exécution d'une fonction

```python
from logging_utils import Chronometer

@Chronometer('ma_fonction')
def function():
    print('do somethings')

```
