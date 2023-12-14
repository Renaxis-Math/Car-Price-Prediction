//
//  TanhNeuron.cpp
//  NeuralNetwork
//
//  Created by Pontus Ahlqvist on 6/29/16.
//  Copyright (c) 2016 PontusAhlqvist. All rights reserved.
//

#include "TanhNeuron.h"
TanhNeuron::TanhNeuron(int numInputs):Neuron(numInputs){}
double TanhNeuron::compute(std::vector<double> inputs){
    this->computeActivation(inputs);
    output = tanh(activation);
    return output;
}

double TanhNeuron::computeDerivative(){
    return 1.0 - output*output; //derivative of tanh is (ch^2-sh^2)/ch^2 = 1-th^2
}