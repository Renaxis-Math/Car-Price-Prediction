//
//  LinearNeuron.h
//  NeuralNetwork
//
//  Created by Pontus Ahlqvist on 6/29/16.
//  Copyright (c) 2016 PontusAhlqvist. All rights reserved.
//

#ifndef __NeuralNetwork__LinearNeuron__
#define __NeuralNetwork__LinearNeuron__

#include "Neuron.h"

class LinearNeuron: public Neuron{
public:
    LinearNeuron(int numInputs);
    double compute(std::vector<double> inputs);
    double computeDerivative();
};

#endif /* defined(__NeuralNetwork__LinearNeuron__) */
