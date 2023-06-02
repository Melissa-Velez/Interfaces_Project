//**
 // @param multiply_coordinates Se define una función externa escrita en C++ que multiplica las coordenadas pasadas ('x' y 'y') como referencia por 100.
//

extern "C" {
    void multiply_coordinates(int& x, int& y) {
        x *= 100;
        y *= 100;
    }
}
