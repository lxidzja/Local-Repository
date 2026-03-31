// Patient.cpp
#include "Patient.h"

using namespace std;

Patient::Patient() {
    this->name = "Unknown";
    this->age = 0;
}

Patient::Patient(std::string name, int age) {
    this->name = name;
    this->age = age;
}

Patient::~Patient() {}

std::string Patient::getName() const { return name; }

int Patient::getAge() const { return age; }