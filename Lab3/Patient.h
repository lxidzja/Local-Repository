// Patient.h
#ifndef PATIENT_H
#define PATIENT_H

#include <string>

class Patient {
   private:
    std::string name;
    int age;

   public:
    Patient();
    Patient(std::string name, int age);
    ~Patient();

    std::string getName() const;
    int getAge() const;
};

#endif