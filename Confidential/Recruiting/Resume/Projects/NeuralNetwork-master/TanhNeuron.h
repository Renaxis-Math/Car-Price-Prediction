//
//  TanhNeuron.h
//  NeuralNetwork
//
//  Created by Pontus Ahlqvist on 6/29/16.
//  Copyright (c) 2016 PontusAhlqvist. All rights reserved.
//

#ifndef __NeuralNetwork__TanhNeuron__
#define __NeuralNetwork__TanhNeuron__

#include "Neuron.h"

class TanhNeuron: public Neuron{
public:
    TanhNeuron(int numInputs);
    double compute(std::vector<double> inputs);
    double computeDerivative();
};

#endif /* defined(__NeuralNetwork__TanhNeuron__) */
