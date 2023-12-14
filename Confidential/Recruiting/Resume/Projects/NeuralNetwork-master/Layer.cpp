//
//  Layer.cpp
//  NeuralNetwork
//
//  Created by Pontus Ahlqvist on 6/27/16.
//  Copyright (c) 2016 PontusAhlqvist. All rights reserved.
//

#include "Layer.h"

Layer::Layer(std::vector<Neuron*> neurons, bool normalized){
    this->neurons = neurons; //TODO: make this more efficient. Perhaps pass by reference or by pointer
    numUnits = (int)neurons.size();
    this->outputs.resize(numUnits);
    this->errors.resize(numUnits);

    prevLayer = 0;
    nextLayer = 0;
    this->normalized = normalized;
    normalization = 1.0;
}

Layer::~Layer(){
    for(int i = 0; i < numUnits; i++){
        delete neurons[i];
    }
}

void Layer::setPrevLayer(Layer *newPrevLayer){
    this->prevLayer = newPrevLayer;
    newPrevLayer->nextLayer = this;
}

void Layer::setNextLayer(Layer *newNextLayer){
    this->nextLayer = newNextLayer;
    newNextLayer->prevLayer = this;
}

void Layer::printWeightMatrix(){
    for(int i = 0; i < numUnits; i++){
        neurons[i]->printWeights();
    }
}

std::vector<double> Layer::computeLayer(){
    return computeLayer(this->prevLayer->outputs);
}

std::vector<double> Layer::computeLayer(std::vector<double> alternateInputs){
    normalization = 0.0;
    for(int i = 0; i < numUnits; i++){
        outputs[i] = neurons[i]->compute(alternateInputs);
        normalization += fabs(outputs[i]);
    }
    if(!normalized || normalization == 0.0){
        normalization = 1.0;
        return outputs;
    }
    for(int i = 0; i < numUnits; i++){
        outputs[i] /= normalization;
    }
    return outputs;
}

std::vector<double> Layer::computeError(std::vector<double> alternateOutputs){
    for(int i = 0; i < numUnits; i++){
        errors[i] = neurons[i]->computeError(alternateOutputs[i],normalization);
    }
    return errors;
}

std::vector<double> Layer::computeError(){
    for(int i = 0; i < numUnits; i++){
        std::vector<double> errorContributions = nextLayer->computeErrorContributionsForPrevLayer(i);
        errors[i] = neurons[i]->computeError(errorContributions);
    }
    return errors;
}

std::vector<double> Layer::computeErrorContributionsForPrevLayer(int inputUnitIndex){
    std::vector<double> errorContributions;
    for(int i = 0; i < numUnits; i++){
        errorContributions.push_back(neurons[i]->computeErrorContribution(inputUnitIndex));
    }
    return errorContributions;
}

double Layer::updateWeightsInLayer(std::vector<double> inputs, double learningRate){
    double largestWeightUpdateInLayer = 0.0;
    for(int i = 0; i < numUnits; i++){
        largestWeightUpdateInLayer = std::max(largestWeightUpdateInLayer, neurons[i]->incrementWeights(inputs, learningRate));
    }
    return largestWeightUpdateInLayer;
}

double Layer::updateWeightsInLayer(double learningRate){
    if(prevLayer != 0){
        return updateWeightsInLayer(prevLayer->outputs, learningRate);
    }
    return 0.0;
}



