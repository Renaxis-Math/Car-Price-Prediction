//
//  Layer.h
//  NeuralNetwork
//
//  Created by Pontus Ahlqvist on 6/27/16.
//  Copyright (c) 2016 PontusAhlqvist. All rights reserved.
//

#ifndef __NeuralNetwork__Layer__
#define __NeuralNetwork__Layer__

#include <vector>
#include <iostream>
#include "Neuron.h"

/*

Each Layer contains a std::vector<Neuron*> which represents the neurons in the layer. Each layer has a previous layer and next layer (except first and last one). There are two types of compute methods depending on if it's an input layer (in which case the alternateInputs overloading is used) or a regular hidden/output layer (in which case the standard computeLayer() method is called without arguments).
*/

class Layer{
protected:
    Layer* prevLayer;
    Layer* nextLayer;

    int numUnits;
    bool normalized;

    std::vector<Neuron*> neurons;
    std::vector<double> outputs;
    std::vector<double> errors;
    double normalization;
public:
    Layer(std::vector<Neuron*> neurons, bool normalized);
    ~Layer();
    void setPrevLayer(Layer* newPrevLayer);
    void setNextLayer(Layer* newNextLayer);
    virtual std::vector<double> computeLayer();
    virtual std::vector<double> computeLayer(std::vector<double> alternateInputs); //this allows the layer to also be used as an input layer.
    void printWeightMatrix();
    std::vector<double> computeError();
    std::vector<double> computeError(std::vector<double> alternateOutputs); //this allows the layer to also be used as an output layer.
    std::vector<double> computeErrorContributionsForPrevLayer(int inputUnitIndex); //this computes the contribution of each neuron's error for use in prior layer

    double updateWeightsInLayer(std::vector<double> inputs, double learningRate);
    double updateWeightsInLayer(double learningRate);
};

#endif /* defined(__NeuralNetwork__Layer__) */
