//
//  SigmoidNeuron.h
//  NeuralNetwork
//
//  Created by Pontus Ahlqvist on 6/26/16.
//  Copyright (c) 2016 PontusAhlqvist. All rights reserved.
//

#ifndef __NeuralNetwork__SigmoidNeuron__
#define __NeuralNetwork__SigmoidNeuron__

#include <vector>
#include <iostream>
#include "Neuron.h"
#include "math.h"

/*

This is a child class to the parent class Neuron. Here we implement the sigmoidal computation unit.

*/

class SigmoidNeuron: public Neuron{
public:
    SigmoidNeuron(int numInputs);
    double compute(std::vector<double> inputs);
    double computeDerivative();
};

#endif /* defined(__NeuralNetwork__SigmoidNeuron__) */
