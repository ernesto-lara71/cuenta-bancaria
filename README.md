# Cuenta bancaria en Python

Sistema de cuentas bancarias que aplica los cuatro pilares de la programación orientada a objetos: abstracción, herencia, encapsulamiento y polimorfismo.

## Características
- Depósitos, retiros y transferencias con validaciones
- Cuenta de débito, que solo permite gastar el saldo
- Cuenta de cheques con límite de sobregiro
- Saldo protegido mediante encapsulamiento (`_saldo` y `@property`)

## Conceptos aplicados
- **Abstracción:** `CuentaBancaria` es una clase abstracta (hereda de `ABC`) que define lo que tienen en común todas las cuentas: depositar, retirar, transferir y mostrar el saldo. La propiedad `disponible` está marcada con `@abstractmethod`, así que cada tipo de cuenta debe definir cuánto dinero puede usar. Por eso no se puede crear una `CuentaBancaria` genérica: Python lanza un `TypeError`, como muestra la prueba al final del script
- **Herencia:** `CuentaDebito` y `CuentaCheques` extienden `CuentaBancaria` y reutilizan su lógica de depósitos, retiros y transferencias
- **Encapsulamiento:** el saldo solo se modifica mediante métodos que lo validan
- **Polimorfismo:** la propiedad `disponible` y `mostrar_saldo` se comportan distinto según el tipo de cuenta. `CuentaDebito` devuelve solo el saldo y `CuentaCheques` suma el límite de sobregiro

## Cómo ejecutarlo
```
python cuenta_bancaria.py
```

## Autor
Rodolfo Ernesto Lara Romero
