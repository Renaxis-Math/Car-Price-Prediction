//
//  OptionParser.cpp
//  NeuralNetwork
//
//  Created by Pontus Ahlqvist on 7/5/16.
//  Copyright (c) 2016 PontusAhlqvist. All rights reserved.
//

#include "OptionParser.h"

OptionParser::OptionParser(){
    keys.push_back("-h");
    descriptions["-h"] = "Display this help message and exit";
}

void OptionParser::add_option(std::string key, std::string description, std::string defaultValue){
    keys.push_back(key);
    descriptions[key] = description;
    optionValues[key] = defaultValue; //will be overwritten if this option is passed
}

void OptionParser::printDescriptions(){
    std::cout << "Usage: ./[program] [options]\n";
    for(int i = 0; i < keys.size(); i++){
        std::cout << keys[i] << "\t" << descriptions[keys[i]] << "\n";
    }
    std::cout << std::endl;
}

//return type is true if parse goes ok and false if '-h' is encountered or any other issue is encountered
bool OptionParser::parse_options(int argc, const char **argv){
    for(int i = 1; i < argc; i = i+2){ //skip first input
        std::string key = argv[i];
        if(key == "-h"){
            printDescriptions();
            return false;
        }

        std::string value = argv[i+1];
        optionValues[key] = value;
    }
    return true;
}

std::vector<std::string> OptionParser::getKeys(){
    return keys;
}

std::string OptionParser::getValue(std::string key){
    std::map<std::string,std::string>::iterator it = optionValues.find(key);
    if(it != optionValues.end()){
        return optionValues[key];
    } else{
        return std::string("");
    }
}

