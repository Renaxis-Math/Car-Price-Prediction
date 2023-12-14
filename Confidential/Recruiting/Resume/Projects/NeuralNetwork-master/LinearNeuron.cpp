//
//  LinearNeuron.cpp
//  NeuralNetwork
//
//  Created by Pontus Ahlqvist on 6/29/16.
//  Copyright (c) 2016 PontusAhlqvist. All rights reserved.
//

#include "LinearNeuron.h"

LinearNeuron::LinearNeuron(int numInputs):Neuron(numInputs){}
double LinearNeuron::compute(std::vector<double> inputs){
    this->computeActivation(inputs);
    output = activation;
    return output;
}

double LinearNeuron::computeDerivative(){
    return 1.0; //derivative of identity function is just 1.
}