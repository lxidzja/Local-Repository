// Clinic.h
#ifndef CLINIC_H
#define CLINIC_H

#include "Patient.h"

class Clinic {
   private:
    Patient* patients;
    int size;
    int capacity;

   public:
    Clinic(int capacity);
    ~Clinic();
    void addPatient(Patient& patient);
    void removePatient(int index);
    Patient& getPatient(int index);
    int getSize() const;
    void print() const;
};

#endif