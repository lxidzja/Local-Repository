// Clinic.cpp
#include "Clinic.h"

#include <iostream>

using namespace std;

Clinic::Clinic(int capacity) {
    this->capacity = capacity;
    this->size = 0;
    this->patients = new Patient[capacity];
}

Clinic::~Clinic() { delete[] patients; }

void Clinic::addPatient(Patient& patient) {
    if (size < capacity) {
        patients[size++] = patient;
    } else {
        cout << "Clinic is full!" << endl;
    }
}

void Clinic::removePatient(int index) {
    if (index >= 0 && index < size) {
        for (int i = index; i < size - 1; i++) {
            patients[i] = patients[i + 1];
        }
        size--;
    }
}

Patient& Clinic::getPatient(int index) { return patients[index]; }

int Clinic::getSize() const { return size; }

void Clinic::print() const {
    for (int i = 0; i < size; i++) {
        cout << patients[i].getName() << " " << patients[i].getAge() << endl;
    }
}
