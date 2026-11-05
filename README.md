# Cuenta bancaria en Python

Sistema de cuentas bancarias que aplica los cuatro pilares de la programación orientada a objetos.

## Características
- Depositos, retiros y transferencias con validaciones
- Cuenta de cheques con límite de sobregiro
- Saldo protegido mediante encapsulamiento (`_saldo` y `@property`)

## Conceptos aplicados
- **Herencia:** `CuentaCheques` extiende `CuentaBancaria`
- **Encapsulamiento:** el saldo solo se modifica mediante métodos que lo validan
- **Polimorfismo:** `retirar` y `mostrar_saldo` se comportan distinto según el tipo de cuenta

## Cómo ejecutarlo
```python cuenta_bancaria.py```

## Autor
Rodolfo Ernesto Lara Romero