# pyFaaS

## Instrucciones

``` bash
# Tener un cluster de Kubernetes con OpenFaas instalado

# Usar faas-cli para hacer el deploy ()
faas-cli up -f pyfunction.yml --skip-push

# Hacer llamado a la funcion
echo "something"|faas-cli invoke pyfunction
```
Tambien puede tener solo la funcion entrando [aquí](https://github.com/andresma2490/pyFaaS/tree/normal-function)
