// main.cpp
#include <iostream>

#include "Clinic.h"
#include "Patient.h"

using namespace std;

int main() {
    Clinic clinic(5);
    Patient patient1("John", 25);
    Patient patient2("Maria", 34);
    Patient patient3("Oleksandr", 41);
    clinic.addPatient(patient1);
    clinic.addPatient(patient2);
    clinic.addPatient(patient3);
    cout << "Список пацієнтів клініки:" << endl;
    clinic.print();
    return 0;
}