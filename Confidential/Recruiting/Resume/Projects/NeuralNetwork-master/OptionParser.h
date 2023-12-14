//
//  OptionParser.h
//  NeuralNetwork
//
//  Created by Pontus Ahlqvist on 7/5/16.
//  Copyright (c) 2016 PontusAhlqvist. All rights reserved.
//

#ifndef __NeuralNetwork__OptionParser__
#define __NeuralNetwork__OptionParser__

#include <map>
#include <vector>
#include <string>
#include <iostream>

class OptionParser{
protected:
    std::vector<std::string> keys;
    std::map<std::string, std::string> optionValues; //from key to value
    std::map<std::string, std::string> descriptions;
    void printDescriptions();
public:
    OptionParser();
    void add_option(std::string key, std::string description, std::string defaultValue = "");
    bool parse_options(int argc, const char** argv);
    //Three different methods to return value for various
    std::vector<std::string> getKeys();
    std::string getValue(std::string key);
};

#endif /* defined(__NeuralNetwork__OptionParser__) */
