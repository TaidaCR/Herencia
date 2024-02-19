from cesar import Cesar
import pytest

def test_create_cesar():
    cesar=Cesar(3)
    assert cesar.clave==3

def test_clave_must_be_integer():
    with pytest.raises(AttributeError) as exc:
        Cesar("algo que no es entero")
    assert "debe ser un entero" in str(exc.value)

    try:
        cesar=Cesar("algo que no es un entero")
        variable_de_comprobacion= 0
    
    except AttributeError:
        variable_de_comprobacion= 1

    assert variable_de_comprobacion== 1 #Se ha lanzado un AttributeError
   
def test_encriptar():
    cesar=Cesar (3)
    assert cesar.encriptar("HOLA")=="KRÑD"