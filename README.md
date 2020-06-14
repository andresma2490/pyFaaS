# pyFaaS

## Instrucciones

``` bash
# Tener un cluster de Kubernetes con OpenFaas instalado 

# Usar faas-cli para hacer el deploy ()
faas-cli up -f pyfunction.yml --skip-push

# Hacer llamado a la funcion
echo "something"|faas-cli invoke pyfunction
```
