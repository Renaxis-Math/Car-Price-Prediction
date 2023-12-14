//
//  ExponentialNeuron.cpp
//  NeuralNetwork
//
//  Created by Pontus Ahlqvist on 6/29/16.
//  Copyright (c) 2016 PontusAhlqvist. All rights reserved.
//

#include "ExponentialNeuron.h"

ExponentialNeuron::ExponentialNeuron(int numInputs):Neuron(numInputs){}
double ExponentialNeuron::compute(std::vector<double> inputs){
    this->computeActivation(inputs);
    output = exp(activation);
    return output;
}

double ExponentialNeuron::computeDerivative(){
    return output; //derivative is equal to the function itself
}