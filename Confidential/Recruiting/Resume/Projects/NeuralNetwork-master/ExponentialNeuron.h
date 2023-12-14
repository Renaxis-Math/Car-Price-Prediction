//
//  ExponentialNeuron.h
//  NeuralNetwork
//
//  Created by Pontus Ahlqvist on 6/29/16.
//  Copyright (c) 2016 PontusAhlqvist. All rights reserved.
//

#ifndef __NeuralNetwork__ExponentialNeuron__
#define __NeuralNetwork__ExponentialNeuron__

#include "Neuron.h"

class ExponentialNeuron: public Neuron{
public:
    ExponentialNeuron(int numInputs);
    double compute(std::vector<double> inputs);
    double computeDerivative();
};

#endif /* defined(__NeuralNetwork__ExponentialNeuron__) */
